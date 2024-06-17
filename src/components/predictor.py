import os
from langchain_pinecone import PineconeVectorStore
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import HumanMessage, AIMessage

from src.utils.common import download_embedding_model, set_env_variables
from src.prompts.question_maker import question_maker_prompt
from src.prompts.qna import qa_prompt

set_env_variables()

PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

embeddings = download_embedding_model()

vectorStore = PineconeVectorStore(index_name=PINECONE_INDEX_NAME, embedding=embeddings)
retriever = vectorStore.as_retriever(search_kwargs={"k":3})

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest")

output_parser = StrOutputParser()

question_chain = question_maker_prompt | llm | StrOutputParser()

def contextualized_question(inp: dict):
    if inp.get("chat_history"):
        return question_chain
    else:
        return inp["question"]
    
retriever_chain = RunnablePassthrough.assign(
        context=contextualized_question | retriever #| format_docs
    )
rag_chain = (
    retriever_chain
    | qa_prompt
    | llm
)

def predict(message, history):
    history_langchain_format = []
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))
    history_langchain_format.append(HumanMessage(content=message))
    ai_response = rag_chain.invoke({"question": message, "chat_history": history_langchain_format})
    return ai_response.content