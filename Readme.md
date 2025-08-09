# RAG-Based AI Chatbot for General and Domain-Specific Queries

## Introduction
This repository contains a Retrieval-Augmented Generation (RAG) chatbot built with [LangChain](https://python.langchain.com) and [Streamlit](https://streamlit.io). The application exposes two interaction modes: a general knowledge assistant powered by Groq's Llama model and a document-aware assistant that answers questions from a supplied PDF. Both modes run in the browser via Streamlit and preserve conversation history for the current session.

## Features
- **General Knowledge Mode:** Uses the Llama model through the `ChatGroq` API to answer open‑ended questions.
- **Document QA Mode:** Loads a PDF, builds a vector index, and retrieves passages relevant to the user's question.
- **Streamlit Interface:** Simple web UI with persistent message history within a session.
- **Environment Isolation:** Dependencies are managed with `pipenv` for reproducible setups.

## Repository Structure
| File | Description |
| --- | --- |
| `phase.py` | Streamlit app for the general knowledge chatbot. |
| `phase1.py` | Streamlit app for document‑based question answering. |
| `Research_1.pdf` | Sample document used by `phase1.py`. |
| `Pipfile`, `Pipfile.lock` | Dependency definitions for `pipenv`. |

## Prerequisites
- Python 3.8 or later
- [pipenv](https://pipenv.pypa.io/)
- A Groq API key saved in a `.env` file

## Installation
```bash
git clone https://github.com/Pavankumarmanagoli/Projects.git
cd Projects/"RAG-Based AI Chatbot for General and Domain-Specific Queries"
pipenv install
```

## Configuration
Create a file named `.env` in the project root and add:
```env
GROQ_API_Key=<your_api_key>
```

## Running the Applications
Activate the virtual environment and launch the desired Streamlit app:
```bash
pipenv shell
streamlit run phase.py      # general knowledge chatbot
streamlit run phase1.py     # domain-specific chatbot
```
Ensure `Research_1.pdf` is available in the project directory when running `phase1.py`.

## Usage Tips
- Ask concise, direct questions for best results.
- In Document QA mode, limit queries to the scope of the provided PDF.
- Restart the Streamlit app to clear the session history.

## Future Enhancements
- Support for indexing multiple documents.
- File upload capability directly from the Streamlit interface.
- Integration with additional large language models.

## License
This project is released under the MIT License.
