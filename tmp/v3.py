import random
import os
import re

import json

from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from rich.console import Console
from rich.markdown import Markdown

from typing import List, Dict, Tuple 
from pydantic import BaseModel, conlist
import yaml

from langchain_ibm import ChatWatsonx
from langchain_core.messages import HumanMessage


file_path = "markdowns/AML_regulations/canada/kyc/methods_to_verify/Methods_to_verify_the_identity_of_persons_and_entities.md" #load_dotenv("credentials.env")

credentials= {
    "url" : "https://us-south.ml.cloud.ibm.com",
    "apikey" : cloud_api_key
}

parameters = {
    "decoding": 'greedy',
    "max_tokens": 2000,
}

project_id= watsonx_project_id

from langchain_ibm import ChatWatsonx

chat = ChatWatsonx(
    model_id="mistralai/mistral-large",
    url="https://us-south.ml.cloud.ibm.com",
    params=parameters,
)


result = {}

filename = file_path.split("/")[-1].split(".")[0]

with open(file_path, 'r') as file:
    manually_cleaned_markdown = file.read()

result["markdown_cleaned"] = manually_cleaned_markdown


headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
    ("####", "Header 4"),
    ("#####", "Header 5"),
    ('######', "Header 6"),
]

# MD splits
markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on, strip_headers=False
)
md_header_splits = markdown_splitter.split_text(manually_cleaned_markdown)

chunk_size = 2000
chunk_overlap = 0
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size, chunk_overlap=chunk_overlap
)

# Split
splits = text_splitter.split_documents(md_header_splits)

print ("Splitted based on " + str(len(md_header_splits)) + " headers")

print("Broken down to " + str(len(splits)) + " chunks")

console = Console()
md = Markdown(splits[0].page_content + "\n" + splits[1].page_content + "\n" + splits[2].page_content + "\n" + splits[3].page_content + "\n" + splits[4].page_content)
#console.print(md)

from rich import print
from rich.layout import Layout

layout = Layout()




layout.split_row(
    Layout(name="left"),
    Layout(name="right")
)

layout["left"].size = None
layout["left"].ratio = 2


from rich import print
from rich.console import Group
from rich.panel import Panel

panel_group = Group(
    Panel(Markdown(splits[0].page_content), style="on blue"),
    Panel(Markdown(splits[1].page_content)),
    Panel(Markdown(splits[2].page_content)),
    Panel(Markdown(splits[3].page_content)),
    Panel(Markdown(splits[4].page_content)),
)
#print(Panel(panel_group))

layout["left"].update(Panel(panel_group))
print(layout)
