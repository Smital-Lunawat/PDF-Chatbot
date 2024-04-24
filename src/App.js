import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [uploadStatus, setUploadStatus] = useState('');

  const handleFileChange = event => {
    setSelectedFile(event.target.files[0]);
  };

  const handleFileUpload = async () => {
    const formData = new FormData();
    formData.append('pdf', selectedFile);

    try {
      const response = await axios.post('http://localhost:10000/upload-pdf', formData);
      console.log(response.data);
      setUploadStatus('File uploaded successfully!');
    } catch (error) {
      console.error('Error uploading PDF:', error);
      setUploadStatus('Error uploading file. Please try again.');
    }
  };

  const handleQuestionChange = event => {
    setQuestion(event.target.value);
  };

  const handleAskQuestion = async () => {
    try {
      const response = await axios.post('http://localhost:10000/ask-question', { question });
      setAnswer(response.data.answer);
    } catch (error) {
      console.error('Error asking question:', error);
    }
  };

  return (
    <div className="app">
      <h1>PDF Question Answering System</h1>
      <div className="file-upload">
        <input type="file" onChange={handleFileChange} accept=".pdf" />
        <button onClick={handleFileUpload}>Upload PDF</button>
        {uploadStatus && <p className="upload-status">{uploadStatus}</p>}
      </div>
      <div className="chat-container">
        <div className="chat-history">
          {answer && (
            <div className="chat-message">
              <p className="question">{question}</p>
              <p className="answer">{answer}</p>
            </div>
          )}
        </div>
        <div className="chat-input">
          <textarea
            value={question}
            onChange={handleQuestionChange}
            placeholder="Enter your question here"
          />
          <button onClick={handleAskQuestion} disabled={!question}>
            Ask Question
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;