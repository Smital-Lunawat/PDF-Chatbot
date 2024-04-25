# PDF-Chatbot

The application should allow users to ask questions related to a specific PDF document, with the LLM providing accurate answers.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed (Download from [python.org](https://www.python.org/downloads/))
- Node.js and npm installed (Download from [nodejs.org](https://nodejs.org/en/download/))

## Installation

Follow these steps to get your development environment set up:

## Set Up the Virtual Environment

Follow these steps to create and activate a virtual environment for your project:

### Create the Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

- For Unix or MacOS:
```bash
source venv/bin/activate
```

- For Windows:
```bash
venv\Scripts\activate
```
## Backend Server
- Start the backend server
```bash
python app.py
```


## Frontend Setup

### Install npm packages
```bash
npm install
```

### Start the frontend application
```bash
npm start
```
## Configuration

### Environment Variables

- Create a `.env` file in the root directory of your project.
- Add the following environment variable to the `.env` file:

```plaintext
GOOGLE_API_KEY=your_google_api_key_here
```

## Aechitecture and Technologies used
The chat application utilizes a client-server architecture with a React frontend for the client-side interface and a Python backend for the server-side logic. 

### Frontend (Client-side):
- React
- npm Packages


### Backend (Server-side):
- Python
- Flask 
- langchain-google-genai 
- Langchain
- Faiss-CPU 
- PyPDF

## Assumptions and Limitations
- There can only be one question asked at a time after that is answered, another question can be asked.
- It takes a little time to answer so hold tight.

## Bonus
- Any pdf file can be read. A file can be choosen and then uploaded file is used using RESTAPI. 





