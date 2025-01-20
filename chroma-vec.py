import getpass
import os
import json

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document

from dotenv import load_dotenv
load_dotenv()

with open("singpass_data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

documents = []
for data in loaded_data:
    doc = Document(page_content=data['title'] + data['answer']['body'])
    documents.append(doc)

# from langchain_text_splitters import RecursiveCharacterTextSplitter

# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=3000,  # chunk size (characters)
#     chunk_overlap=200,  # chunk overlap (characters)
#     add_start_index=True,  # track index in original document
# )
# all_splits = text_splitter.split_documents(documents)    

# print(len(all_splits))

persist_directory = "./chroma_db"

vectorstore = Chroma.from_documents(
    documents=documents,
    collection_name='singpass',
    embedding=OpenAIEmbeddings(),
    persist_directory=persist_directory
)
