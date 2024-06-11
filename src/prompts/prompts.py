# This file will contain prompts for all the tasks in the project

from langchain.prompts import PromptTemplate


DIAGNOSIS_PROMPT = """
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

def get_prompt(pipeline_name: str):
    if pipeline_name == "diagnosis":
        return PromptTemplate(intput_variables=["context", "question"], template=DIAGNOSIS_PROMPT)
    else:
        raise Exception("Invalid pipeline name")