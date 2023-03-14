from dotenv import load_dotenv
from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader, LLMPredictor
from langchain.llms import OpenAI
import os

# import parameters
from parameters import *

# Load environment variables
load_dotenv()

# set Open AI API key
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# parameters

# creating the LLM
llm = OpenAI(temperature=temperature, model_name=model_name, max_tokens=max_tokens)

# token counter
llm_predictor = LLMPredictor(llm=llm)

# if creating index
if (creating_index):
  # loading the document from the directory
  documents = SimpleDirectoryReader(documents_directory).load_data()

  # creating the index
  index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor)

  # print token utilization for building index
  print('Document indexing token utilization: ', llm_predictor.last_token_usage)

  # save index to a index.json file
  index.save_to_disk(index_file_name)  

# load index from a index.json file
index = GPTSimpleVectorIndex.load_from_disk(index_file_name)

# function to query the index and display the results
def query_model(query_txt):
  # querying the index
  response = index.query(
    query_txt,
    llm_predictor=llm_predictor)
  print(f'Query: {query_txt}')
  # display response
  print(response.response)

  print('Tokens used for last query: ', llm_predictor.last_token_usage)

# making queries
for query in queries:
  query_model(query)