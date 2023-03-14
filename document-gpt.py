from dotenv import load_dotenv
from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader, LLMPredictor
from langchain.llms import OpenAI
import os

# Load environment variables
load_dotenv()

# set Open AI API key
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# loading the document from the directory
# documents = SimpleDirectoryReader('data/documents').load_data()

# creating the LLM
llm = OpenAI(temperature=0.6, model_name="gpt-3.5-turbo")

# token counter
llm_predictor = LLMPredictor(llm=llm)

# creating the index
# index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor)

# print token utilization for building index
# print('Document indexing token utilization: ', llm_predictor.last_token_usage)

# save index to a index.json file
# index.save_to_disk('ai_benefit_text_index_gpt.json')

# load index from a index.json file
index = GPTSimpleVectorIndex.load_from_disk('ai_benefit_text_index_gpt.json')

query_text = "What are benefits of IDPS systems built using AI?"

# querying the index
response = index.query(
  query_text,
  llm_predictor=llm_predictor)
print(f'Query: {query_text}')
print(response.response)

print('Tokens used for last query: ', llm_predictor.last_token_usage)