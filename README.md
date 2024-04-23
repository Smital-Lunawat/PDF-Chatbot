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
OPENAI_API_KEY=your_openai_api_key_here
```



