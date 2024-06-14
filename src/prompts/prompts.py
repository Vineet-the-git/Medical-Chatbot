# This file will contain prompts for all the tasks in the project

from langchain.prompts import PromptTemplate


DIAGNOSIS_PROMPT = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Chat History: {chat_history}
Question: {question}

Only return the helpful answer. Answer must be detailed and well explained.
Helpful answer:
"""