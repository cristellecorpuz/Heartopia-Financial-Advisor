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

<h2> 2.2 Set up virtual environment (optional) </h2>
It is highly recommended to use a virtual environment to manage dependencies.

```bash
python -m venv .venv

.venv\Scripts\activate

source .venv/bin/activate
```
<h2> 2.3 Install dependencies </h2>
With your virtual environment activated, install the required Python packages:

```bash
pip install -r requirements.txt
```
<h2> 2.4 Start the Vector Database (Docker) </h2>
The application relies on ChromaDB running in a Docker container. Spin up the background service using Docker Compose:
Ensure Docker Desktop is running before executing this command. The ChromaDB server will run on localhost:8000.

```bash
docker-compose up -d
```
<h2> 2.5 Ingest the Data </h2>
Before asking questions, you need to populate the database with the Heartopia game data. You can do this by opening the ingest2.ipynb notebook in your preferred editor (like VS Code or Jupyter) and running all the cells.
Alternatively, you can execute the notebook directly from your terminal:

```bash
jupyter nbconvert --to notebook --execute ingest2.ipynb
```

<h2> Run the App </h2>
Once the data is ingested and the database is running, you can launch the frontend application.
Run the following command to start the Streamlit UI:

```bash
streamlit run chat.py
```

If you encounter any error, feel free to message me on linkedIn 📧.

