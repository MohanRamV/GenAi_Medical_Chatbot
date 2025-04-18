from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate


system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that"
    "Sorry, That information is not availabe in the materila provided,Try with different keywords." 
    "Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)