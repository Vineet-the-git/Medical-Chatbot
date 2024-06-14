# Healthcare Diagnosis Chatbot

This repo will contain my solution for MS hackathon 2024.

**Problem Statement:** Build a chatbot capable of diagnosing common medical conditions based on user symptoms input. Utilize machine learning models trained on medical data to provide accurate suggestions and recommendations for further action.

**Solution:** I will build a chatbot using Python and Langchain. The chatbot will be able to take user input in the form of symptoms, history of patient, pathology reports, etc. and provide a diagnosis based on the input. The chatbot will also ask follow-up questions to gather more information if needed. The chatbot will also provide recommendations for further action such as seeing a doctor, getting tests done, etc. The chatbot will use LLMs fine-tuned on medical data to provide accurate suggestions. The chatbot will also fetch answer from credible sources like books, research papers, etc. to provide accurate information. The chatbot will be deployed on a web interface for easy access.


## How to setup the project locally

1. Clone the repository
2. Install the required dependencies using `pip install -r requirements.txt`
3. Create a `.env` file in the root directory and add the following environment variables:
    ```
    PINECONE_API_KEY=<your_pinecone_api_key>
    ```

    To create a Pinecone API key, sign up on the Pinecone website and create a new API key. Copy the API key and add it to the `.env` file.
    Create a new Pinecone index named `medicine` and add the index name to the `.env` file as well.

4. Store the data in the Pinecone index using the `store_to_index.py` script:
    ```
    python store_to_index.py
    ```
5. Download the pre-trained models from Hugging Face to the `models` directory.


## To do of the project

- [x] Setup the project structure template
- [x] Build the data injestion part to store the data in Pinecone from the pdf files
- [x] Build the chatbot using Langchain
    - [ ] The chatbot should be able to take user input in the form of symptoms, history of patient etc.
    - [ ] The chatbot should have a history of the conversation with the user
- [ ] Build the web interface for the chatbot

## Things to do next:
- [ ] Make sure which chain to use, RetrievalQA or ConversationalRetrieval
- [ ] Also make an interface using simple html, css.
- [ ] Start adding functionalities once base bot is working.