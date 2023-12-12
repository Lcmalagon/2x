import streamlit as st
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
import tempfile
import os

# Set API key for OpenAI
os.environ["OPENAI_API_KEY"] = "api-key"

# Streamlit UI setup
st.set_page_config(layout="wide", page_icon="💬")
st.title("Gideon")
st.markdown("---")

# Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>I'm your Alumni Database Chatbot, powered by LangChain and Streamlit. 
    I leverage advanced language models to provide insightful answers from your alumni database. 
    Upload a CSV file and ask me questions about the alumni data.</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload", type="csv")

if 'initialized' not in st.session_state:
    st.session_state['initialized'] = False
    st.session_state['history'] = []

# Process file only once
if uploaded_file and not st.session_state['initialized']:
    print("Uploaded file detected.")
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name
        print(f"Temporary file path: {tmp_file_path}")

    loader = CSVLoader(file_path=tmp_file_path, encoding="utf-8", csv_args={'delimiter': ','})
    data = loader.load()
    print(f"Number of documents loaded: {len(data)}")

    if data:
        embeddings = OpenAIEmbeddings()
        print("Embeddings created.")
        vectorstore = FAISS.from_documents(data, embeddings)
        print("Vectorstore created.")
        st.session_state['chain'] = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(temperature=0.0, model_name='gpt-4-1106-preview'),
            retriever=vectorstore.as_retriever()
        )
        print("Conversational retrieval chain created.")
        st.session_state['initialized'] = True
    else:
        print("No data loaded.")

# Chat function
def conversational_chat(query):
    print(f"Received query: {query}")
    if st.session_state['chain']:
        result = st.session_state['chain']({"question": query, "chat_history": st.session_state['history']})
        print(f"Result from chain: {result}")
        st.session_state['history'].append((query, result["answer"]))
        return result["answer"]
    else:
        print("Chain is None, returning default message.")
        return "Sorry, no data is available."

# Chat UI
response_container = st.container()
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_input("Query:", placeholder="Ask questions about your alumni database here", key='input')
        submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        print(f"User input submitted: {user_input}")
        output = conversational_chat(user_input)
        print(f"Output generated: {output}")
        st.session_state['history'].append(("Question", user_input))
        st.session_state['history'].append(("Answer", output))

# Display chat history
with response_container:
    for role, message in st.session_state['history']:
        if role == "Question":
            st.markdown(f"**Question:** {message}")
        elif role == "Answer":
            st.markdown(f"**Answer:** {message}")
