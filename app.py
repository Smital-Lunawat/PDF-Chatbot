from flask import Flask, request, jsonify
from flask_cors import CORS  # To handle Cross-Origin Resource Sharing (CORS)
from PyPDF2 import PdfReader
import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

load_dotenv()
os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)  # Enable CORS on all routes

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#filepath = "New"

def text_split(raw_text):
    text_splitter = CharacterTextSplitter(        
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap  = 200,
        length_function = len,
    )
    texts = text_splitter.split_text(raw_text)
    return texts

def read_pdf(pdf):
    reader = PdfReader(pdf)
    raw_text = ''
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            raw_text += text    
    
    return raw_text

def get_vector_store(text_chunks):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("OpenAI_VectorDatabase")

def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    
    chain = load_qa_chain(OpenAI(), chain_type="stuff")

    return chain


def allowed_file(filename):
    """Check if the uploaded file has a valid extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    """Handle the upload of a PDF file."""
    if 'pdf' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['pdf']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        pdf_loc = filepath
        texts_chunks = text_split(read_pdf(pdf_loc))
        get_vector_store(texts_chunks)

        return jsonify({'message': 'PDF uploaded successfully', 'filepath': filepath}), 200
    return jsonify({'error': 'Allowed file types are .pdf'}), 400

@app.route('/ask-question', methods=['POST'])
def ask_question():
    """Receive a question and return an answer based on the PDF content."""
    data = request.get_json()
    question = data.get('question', '')
    embeddings = OpenAIEmbeddings()
    
    new_db = FAISS.load_local("OpenAI_VectorDatabase", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(question)

    chain = get_conversational_chain()    

    response = chain({"input_documents":docs, "question": question}, return_only_outputs=True)

    # Here you would add your logic to process the question against the PDF content
    # For demonstration, let's just echo the question
    answer = response["output_text"]

    #ans = answer+filepath
    
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
