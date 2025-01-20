from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from src.llm import LLM

loaded_vectorstore = Chroma(
    persist_directory='./chroma_db',
    collection_name='singpass',
    embedding_function=OpenAIEmbeddings()
)

retriever = loaded_vectorstore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
    "k": 3,
    "score_threshold": 0.5
    })

def get_answer(question):

    docs = retriever.invoke(question)

    relevant_document_string = ""
    for ii, doc in enumerate(docs):
        relevant_document_string += f"Document {ii+1}: {doc.page_content}\n\n"

    messages = [
                {
                    'role': 'developer',
                    'content': f"""
                        You are a helpful customer service agent. 
                        A user has asked you for help.
                        Given some reference documents, provide a response.
                        The response should be able to be parsed as markdown.
                        """
                },
                {
                    'role': 'user',
                    'content': f"""

                        Based on the relevant documents below, you must reply to a user's question.
                        The response should be able to be parsed as markdown so it can include links.
                        You can include links to websites in your response, but not to images.
                        Be as helpful and friendly as possible.

                        Relevant Documents:
                        {relevant_document_string}

                        User Question:
                        {question}

                        Now reply to the user's question and only the reply should be returned:
                        """
                }
    ]

    llm = LLM()
    response = llm.invoke(messages)
    return response