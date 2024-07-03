import os
from dotenv import load_dotenv
from llama_index.core.response.pprint_utils import pprint_response
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Load environment variables from .env file
load_dotenv()

# Check if the API key is loaded correctly
api_key = os.getenv("OPENAI_API_KEY")

# Set the API key (if necessary for the library, otherwise it can be omitted)
os.environ["OPENAI_API_KEY"] = api_key

# Load documents using SimpleDirectoryReader
documents = SimpleDirectoryReader("data").load_data()

index = VectorStoreIndex.from_documents(documents, show_progress=True)
query_engine = index.as_query_engine()

response = query_engine.query("who is youssef tarek?")
print(response)
pprint_response(response, show_source=True)