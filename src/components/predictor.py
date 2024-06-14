import os
from langchain_pinecone import PineconeVectorStore
from langchain import PromptTemplate
from langchain_community.llms import LlamaCpp
from langchain.chains import ConversationalRetrievalChain
from regex import P

from src.utils.common import download_embedding_model
from src.prompts.prompts import DIAGNOSIS_PROMPT

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_API_ENV = os.getenv("PINECONE_API_ENV")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

embeddings = download_embedding_model()
vectorStore = PineconeVectorStore(index_name=PINECONE_INDEX_NAME, embedding=embeddings)

local_llm = "C:/Users/vinee/Desktop/Challenges/Medical-Chatbot/models/BioMistral-7B.Q4_K_M.gguf"
llm = LlamaCpp(model_path= 
local_llm,temperature=0.3,max_tokens=4096,top_p=1,n_ctx= 4096, verbose=False)

retriever = vectorStore.as_retriever(search_kwargs={"k":3})

chat_history = []

# Create the custom chain
if llm is not None and retriever is not None:   
    chain = ConversationalRetrievalChain.from_llm(llm=llm,retriever=retriever)	
else:     
    print("LLM or Vector Database not initialized")

def predict(message, history):
    history_langchain_format = []
    response = chain({"question": message, "chat_history": chat_history})
    answer = response['answer']
    chat_history.append((message, answer))

    temp = []
    for input_question, bot_answer in history:
        temp.append(input_question)
        temp.append(bot_answer)	
        history_langchain_format.append(temp)
    temp.clear()
    temp.append(message)
    temp.append(answer)
    history_langchain_format.append(temp)
    return answer
