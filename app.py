from flask import Flask, render_template, request, session
from dotenv import load_dotenv
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__, template_folder='templates')
app.secret_key = os.getenv("FLASK_SECRET_KEY", "supersecret")  # Required for session context

# Environment Variables
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Initialize embeddings
embeddings = download_hugging_face_embeddings()

# Load Pinecone vector store
index_name = "medibot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# Set up Gemini LLM chain
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=GOOGLE_API_KEY)

nice_prompt = """
You are Medibot, a helpful and knowledgeable AI medical assistant. Your job is to provide clear, friendly, and factual responses to users' health-related questions using only the context provided from trusted medical sources.

⚠️ If any medicines or treatments are present in the provided context, **you must include them clearly in your response** and explain how they relate to the user’s question (e.g., fever, pain, infection, etc.).

Do not guess or hallucinate answers. If a treatment or medicine is not found in the context, say: \"I'm Medibot, and I couldn't find treatment information for your query in my reference material.\"

Be concise, fact-based, and act like a knowledgeable friend who respects user safety and refers them to professionals when needed.
"""

prompt = ChatPromptTemplate.from_template(nice_prompt + "\nContext:\n{context}\n\nConversation History:\n{chat_history}\n\nQuestion:\n{input}")

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/")
def index():
    session.clear()  # Clear conversation on reload
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    print("User input:", msg)  # Debug log

    # Retrieve or initialize chat history
    if "chat_history" not in session:
        session["chat_history"] = ""
    session["chat_history"] += f"User: {msg}\n"

    # Call RAG chain with history
    response = rag_chain.invoke({
        "input": msg,
        "chat_history": session["chat_history"]
    })
    answer = response["answer"]
    session["chat_history"] += f"Medibot: {answer}\n"

    print("Bot response:", answer)  # Debug log
    return str(answer)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
