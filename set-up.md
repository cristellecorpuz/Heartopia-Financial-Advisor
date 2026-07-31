# Set up and Installation Guide
<h2> 1.1 Prerequisites </h2>
Before you begin, ensure you have the following installed on your system:
- Python 3.10+
- Docker Desktop (and Docker Compose) to run the ChromaDB container.
- Git
You will also need active API keys for the language models:
- Google Gemini API Key (Primary LLM)
- OpenAI API Key (Fallback LLM & Evaluation)

<h2> 1.2 Environment Variables </h2>
Create a .env file in the root directory of the project. This file will securely store your API keys so the application can authenticate with the model providers.
Add the following structure to your .env file:

```
GEMINI_API_KEY="your_gemini_api_key_here"
OPENAI_API_KEY="your_openai_api_key_here"
```

<h2> 2.1 Clone repo </h2>
Open the terminal and clone this repo to your local machine:

```bash
git clone [https://github.com/cristellecorpuz/Heartopia-Financial-Advisor.git](https://github.com/cristellecorpuz/Heartopia-Financial-Advisor.git)
cd Heartopia-Financial-Advisor
```

<h2> 2.2 Launch the Application </h2>
Because this application is fully containerized, you can spin up both the Streamlit frontend and the ChromaDB vector database with a single command:
Ensure Docker Desktop is running before executing this command. Once built, the Streamlit app will be available at http://localhost:8501 and ChromaDB will run in the background on localhost:8000.

```bash
docker-compose up -d --build
```
<h2> 2.3 Ingest Data </h2>
Before asking questions in the UI, you need to populate the database with the Heartopia game data. To run the ingestion notebook safely without polluting your global Python environment, set up a quick virtual environment:

```bash
# Create and activate the virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install the dependencies
pip install -r requirements.txt

# Run the ingestion notebook
jupyter nbconvert --to notebook --execute ingest2.ipynb
```

If you encounter any error, feel free to message me on linkedIn 📧.

