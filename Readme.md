# RAG-Based AI Chatbot for General and Domain-Specific Queries


## Overview
This project implements a Retrieval-Augmented Generation (RAG) AI chatbot using LangChain and Streamlit. The chatbot provides two functionalities:

1. **General Knowledge Chatbot**: Uses the Llama model for general question answering.
2. **Domain-Specific Chatbot**: Trained on a specific corpus to provide precise answers related to the uploaded documents.

The application uses a virtual environment created with `pipenv` and leverages LangChain's APIs to enable accurate and context-aware responses.

## Features
- General knowledge chatbot using the Llama model.
- Retrieval-based chatbot trained on specific document(s).
- Easy-to-use Streamlit interface.
- Persistent session for historical messages.

## Project Structure
- **`phase.py`**: Implements the general knowledge chatbot.
- **`phase1.py`**: Implements the domain-specific chatbot with document-based retrieval.
- **`.env`**: Stores the required API key for the Groq model.

## Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `pipenv` for virtual environment management
- Required libraries specified in `Pipfile`.

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   pipenv install
   ```
3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```
4. Add your Groq API key to the `.env` file:
   ```
   GROQ_API_Key=<your_api_key>
   ```

## Running the Application
1. Run the general knowledge chatbot (`phase.py`):
   ```bash
   streamlit run phase.py
   ```
2. Run the domain-specific chatbot (`phase1.py`):
   ```bash
   streamlit run phase1.py
   ```

## Usage
### General Knowledge Chatbot (phase.py)
- Open the Streamlit app.
- Enter your query in the input box.
- The chatbot will respond with contextually accurate answers.

### Domain-Specific Chatbot (phase1.py)
- Open the Streamlit app.
- Ensure the `Research_1.pdf` file is placed in the correct directory (`/Users/pavanmanagoli/Documents/AI_Chatbot_RAG/`).
- Enter your query in the input box.
- The chatbot will retrieve and answer based on the document content.

## Code Breakdown
### phase.py
- **LangChain Integration**: Uses the `ChatGroq` class with the Llama model to generate answers.
- **Session Management**: Streamlit manages user interactions and displays historical messages.
- **Prompt Template**: A predefined prompt ensures consistent responses.

### phase1.py
- **Document Loader**: Loads PDF files using `PyPDFLoader`.
- **Vector Database**: Uses `VectorstoreIndexCreator` to create embeddings from the document.
- **Retrieval QA**: Enables retrieval-augmented responses from the vector database.

## Troubleshooting
- Ensure the `.env` file contains the correct API key.
- Verify the path to `Research_1.pdf` is correct in `phase1.py`.
- Check Python and library versions to match the project requirements.

## Future Enhancements
- Add support for multiple documents.
- Enhance the Streamlit UI with file upload functionality.
- Integrate additional language models for improved performance.


