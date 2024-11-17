import random
import os
import re

import json

from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

from typing import List, Dict, Tuple 
from pydantic import BaseModel, conlist
import yaml

from langchain_ibm import ChatWatsonx
from langchain_core.messages import HumanMessage


file_path = "markdowns/AML_regulations/canada/kyc/methods_to_verify/Methods_to_verify_the_identity_of_persons_and_entities.md" #load_dotenv("credentials.env")
cloud_api_key= "" #os.getenv("CLOUD_API_KEY")
watsonx_project_id= ""#os.getenv("WATSONX_PROJECT_ID")

os.environ["WATSONX_URL"] = "https://us-south.ml.cloud.ibm.com"
os.environ["WATSONX_API_KEY"] = ""
os.environ["WATSONX_APIKEY"] = ""
os.environ["WATSONX_PROJECT_ID"] = ""

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
    project_id="",
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
from rich.console import Console
from rich.markdown import Markdown
console = Console()
md = Markdown(splits[0].page_content)
console.print(md)
#print(splits[0])
print("================")
print(splits[1])
print("================")
print(splits[2])
print("================")
print(splits[3])
print("================")
print(splits[4])
print("================")



for s in splits:
    print(len(s.page_content))
def calculate_word_count(text):
    words = text.split()
    return len(words)

def calculate_bullet_point_ratio(text: str) -> float:
    """
    Calculate the ratio of bullet points to total lines in the given text.
    
    Args:
        text (str): The input text to analyze.
        
    Returns:
        float: The bullet point ratio.
    """
    # Split the text into lines
    lines = text.split('\n')
    total_lines = len(lines) if lines else 0
    if total_lines == 0:
        return 0.0
    
    # Define bullet indicators with regex patterns to match at the start of a line after optional whitespace
    bullet_patterns = [
        r'^\s*-\s+',   # -, e.g., "- Item"
        r'^\s*\*\s+',  # *, e.g., "* Item"
        r'^\s*\+\s+',  # +, e.g., "+ Item"
        r'^\s*\d+\.\s+' # Ordered lists, e.g., "1. Item", "2. Item", etc.
    ]
    
    # Compile the regex patterns for efficiency
    compiled_patterns = [re.compile(pattern) for pattern in bullet_patterns]
    
    # Count lines that start with any bullet indicator
    bullet_count = 0
    for line in lines:
        for pattern in compiled_patterns:
            if pattern.match(line):
                bullet_count += 1
                break  # Avoid multiple counts per line
    
    # Calculate the ratio
    ratio = bullet_count / total_lines
    return ratio

def process_chunks(chunks):
    # Step 1: Process all chunks and store their metrics
    processed_chunks = []
    for idx, chunk in enumerate(chunks):
        content = chunk.page_content
        metadata = chunk.metadata
        word_count = calculate_word_count(content)
        bullet_point_ratio = calculate_bullet_point_ratio(content)
        
        processed_chunks.append({
            'idx': idx,
            'content': content,
            'metadata': metadata,
            'word_count': word_count,
            'bullet_point_ratio': bullet_point_ratio
        })

    if not processed_chunks:
        # Handle empty chunks list
        return {}
    
    # Step 2: Determine the word count threshold (median)
    word_counts = sorted(chunk['word_count'] for chunk in processed_chunks)
    median_index = len(word_counts) // 2
    word_count_threshold = word_counts[median_index]
    
    # Step 3: Filter out chunks below the median word count and with high bullet point ratio
    filtered_chunks = [
        chunk for chunk in processed_chunks
        if chunk['word_count'] >= word_count_threshold and chunk['bullet_point_ratio'] <= 90
    ]
    
    if not filtered_chunks:
        # Handle case where no chunks meet the criteria
        return {}
    
    # Step 4: Select up to 5 random chunks from the filtered set
    num_chunks_to_select = min(5, len(filtered_chunks))
    selected_chunks = random.sample(filtered_chunks, num_chunks_to_select)
    

    return processed_chunks, selected_chunks


chunks, selected_chunks = process_chunks(splits)
result["chunks"] = chunks
result["selected_chunks"] = selected_chunks


DOCUMENT_SUMMARY_PROMPT = """
Your objective is to generate a concise description of a chapter from Mastercard Transaction Processing Rules.

Here is the beggining of the document:

{first_part}

respond with a concise sentence that explains the purpose of this document
"""

summary = chat.invoke([HumanMessage(content=DOCUMENT_SUMMARY_PROMPT.format(first_part=result['markdown_cleaned'][:2000]))]).content

print(summary)

result["summary"] = summary


CONTEXT_PROMPT = """
This chunk is from Mastercard Transaction Processing Rules document.

Your objective is to generate context for splitted markdown chunks so that can be located in document.
Carefully analyze the provided chunk, document description, and headers leading to the chunk.

Here is an AI generated description of the document being analyzed:

[DESCRIPTION]
{desc}
[END DESCRIPTION]

This chunk is situated under following md headers:

[HEADERS]
{headers}
[END HEADERS]

[CHUNK]
{chunk}
[END CHUNK]


respond with a concise sentence
""".strip()

#TODO: explore adding neighbour contexts for more info!

for chunk in result["selected_chunks"]:
    messages = []
    context =  chat.invoke([HumanMessage(content=CONTEXT_PROMPT.format(desc=result["summary"], headers=chunk['metadata'], chunk=chunk['content']))]).content
    print(context)
    chunk['context'] = context

QUESTION_PROMPT = """
Please generate 3 questions based on the provided chunk of document. DO NOT generate the answer, just questions.

Anticipate the scenarios where a regulatory officer in a bank might have a question where the answers could be found in the chunk being assessed.

The questions should:
* Be self-contained, not requiring references to tables, figures, or specific sections in the text for understanding.
* Focus on teaching and reinforcing the key knowledge and concepts presented in the document.
* Be formulated to allow for independent answers, avoiding direct references to specific theorems or text sections. For example, rather than asking 'Under what conditions is the fixed point of a function unique according to Theorem 3.1.5?', ask 'How does the Fixed Point Iteration method contribute to understanding function uniqueness?'
* Span a range of difficulty levels to accommodate a diverse audience, from basic understanding to advanced comprehension.

{format_instructions}

Here is the description of the specific chunk being analyzed:

{context}

In you questions, start with According to Mastercard Transaction Processing Rules,

Chunk:

{chunk}
""".strip()

class QuestionList(BaseModel):
    questions: conlist(str, min_length=3, max_length=3)

# Set up a parser + inject instructions into the prompt template.
parser = PydanticOutputParser(pydantic_object=QuestionList)

prompt = PromptTemplate(
    template=QUESTION_PROMPT,
    input_variables=["context", "chunk"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | chat | parser
for chunk in result["selected_chunks"]:
    chunk["questions"] = chain.invoke({"context": chunk["context"], "chunk":chunk['content'] }).questions

ANSWER_PROMPT = """
Please generate a concise answer for the following question based on the provided chunk of document.

{question}

Here is the description of the specific chunk being analyzed:

{context}

[DOCUMENT]
{chunk}
[END DOCUMENT]

Your answer shouldn't say based on the document or chunk, it should reference to the governing body or rule mentioned in the description
""".strip()

for chunk in result["selected_chunks"]:
    messages = []
    qnas = {"qnas": [{"question": q, "answer": chat.invoke([HumanMessage(content=ANSWER_PROMPT.format(question=q, context=chunk['context'], chunk=chunk['content']))]).content.strip()} for q in chunk['questions']]}
    print(qnas['qnas'])
    chunk['qnas'] = (qnas['qnas'])

yaml_data = {
    "created_by": "CE",
    "version": 3,
    "domain":"USA Regulations",
    "seed_examples": [],
    "document_outline": result['summary'].strip()
}

for chunk in result['selected_chunks']:
    example = {
        "context": f"{chunk['content']}",
        "questions_and_answers": []
    }
    for qa in chunk["qnas"]:
        example["questions_and_answers"].append({
            "question": qa["question"],
            "answer": qa["answer"]
        })
    yaml_data["seed_examples"].append(example)

# Convert to YAML
yaml_output = yaml.dump(yaml_data, sort_keys=False, default_flow_style=False)
print(yaml_output)

with open('qna.yaml', 'w') as file:
    yaml.dump(yaml_data, file, sort_keys=False, default_flow_style=False)

with open(filename + ".json", "w") as file:
    json.dump(result, file, indent=4)
print("Json file saved successfully!")
