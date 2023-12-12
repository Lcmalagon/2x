
# Gideon: Alumni Database Chatbot


## Overview

Gideon is an advanced Alumni Database Chatbot, designed to provide insightful answers from alumni data. It's built using the LangChain library and Streamlit, leveraging the power of OpenAI's language models. Users can upload a CSV file containing alumni data and interact with the chatbot to get information and insights.

## Features

- **Alumni Data Interaction:** Users can upload their alumni database in CSV format.
- **Intelligent Chat Interface:** Utilizes OpenAI's GPT-4 model for understanding and generating responses.
- **Streamlit Web Interface:** Easy-to-use and intuitive web interface for users to interact with the chatbot.
- **Conversational Context Awareness:** Maintains chat history for context in conversations.

## How to Use

1. **Setup:**
   - Clone the repository.
   - Install required dependencies: `streamlit`, `langchain`, `FAISS`.
   - Set your OpenAI API key in the environment variables.

2. **Running the Application:**
   - Start the Streamlit app by running `streamlit run app.py` (replace `app.py` with the name of your main Python file).
   - The web interface will be hosted locally for interaction.

3. **Using the Chatbot:**
   - Upload your alumni database CSV through the web interface.
   
      <img width="349" alt="Screenshot 2023-12-11 at 23 10 04" src="https://github.com/Lcmalagon/Gideon/assets/42157414/6bdba954-2da6-4aed-bc63-d4d9cae18f0c">

      <img width="879" alt="Screenshot 2023-12-11 at 23 10 08" src="https://github.com/Lcmalagon/Gideon/assets/42157414/33f41bd9-4414-4734-8b9a-9ef3af0c80db">
   - Start asking questions about the alumni data.
   - The chatbot will respond with information based on the uploaded data.

## Requirements

- Python 3.x
- Streamlit
- LangChain
- OpenAI API Key
- FAISS for vector storage

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](link-to-your-issues-page).

## License

Specify your license or if the project is open-source.

## Acknowledgments

- LangChain Library
- OpenAI's GPT-4 Model
- Streamlit Community
