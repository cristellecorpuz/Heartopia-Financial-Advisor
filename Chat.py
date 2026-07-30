import streamlit as st
import os
import chromadb
from sentence_transformers import SentenceTransformer
from google import genai
from dotenv import load_dotenv
import csv
from datetime import datetime

def save_feedback(question, answer, feedback_value):
    """Saves user feedback to a local CSV 'database'."""
    file_exists = os.path.isfile("feedback.csv")
    
    with open("feedback.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "Question", "Answer", "Rating"])
            
        rating_str = "Thumbs Up" if feedback_value == 1 else "Thumbs Down"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        writer.writerow([timestamp, question, answer, rating_str])

st.set_page_config(page_title="Heartopia Assistant", page_icon="🎮")
st.title("🎮 Heartopia Financial Advisor")
st.caption("Hi! Do you need Heartopia financial assistance?")

with st.sidebar:
    st.header("About This Project")
    st.markdown(
        "This is an AI-powered Retrieval-Augmented Generation (RAG) pipeline designed "
        "to calculate profit margins and retrieve item data for Heartopia only."
    )

    st.divider()

    st.warning(
        "**⚠️ AI Safety Disclaimer**\n\n"
        "This assistant is powered by an LLM. While it retrieves context directly "
        "from the game's database, AI can occasionally hallucinate or make mathematical "
        "errors."
    )

@st.cache_resource
def load_backend():
    load_dotenv(override=True)
    db_host = os.getenv("CHROMA_HOST", "localhost")
    client = chromadb.HttpClient(host=db_host, port=8000)
    collection = client.get_collection(name="heartopia_knowledge")
    
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return collection, model

collection, model = load_backend()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def retrieve_docs(user_query: str, top_k: int = 5):
    query_vector = model.encode(user_query).tolist()
    results = collection.query(query_embeddings=[query_vector], n_results=top_k)
    return results['documents'][0] if results['documents'] else []

def generate_rag_response(prompt_text: str):
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=gemini_api_key)
    
    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=prompt_text
    )
    return response.text


if user_input := st.chat_input("Try: How much profit for Blueberry Jam?"):

    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Searching database..."):
            
            docs = retrieve_docs(user_input)
            full_context = "\n".join(docs)
            
            prompt = f"""You are an expert Heartopia game assistant and financial advisor. 
            Use the following Context to answer the User's question. Perform step-by-step math if needed but do not display the solution unless requested by the user.
            If the answer is not explicitly contained within the Context below, respond with "I don't have data for that."
            
            Context:
            {full_context}
            
            User Question: {user_input}
            """
            
            try:
                answer = generate_rag_response(prompt)
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})

                st.session_state.last_question = user_input
                st.session_state.last_answer = answer
                
            except Exception as e:
                st.error(f"Generation Failed: {e}")
                st.session_state.last_question = user_input
                st.session_state.last_answer = str(e)

if "last_answer" in st.session_state:
    st.write("---")
    st.caption("How did I do on that last answer?")
    
    feedback = st.feedback("thumbs")
    
    if feedback is not None:
        save_feedback(
            st.session_state.last_question, 
            st.session_state.last_answer, 
            feedback
        )
        st.success("Feedback recorded in database! Thank you ><.")