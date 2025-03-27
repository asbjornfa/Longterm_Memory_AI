from fastapi import FastAPI, APIRouter
from langchain.chains.llm import LLMChain
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from pymongo import MongoClient
from mongoMemory import MongoMemory

# Initializes the API router for handling endpoint registrations.
router = APIRouter()


# Establishes a connection to the MongoDB server. Using environment variables for the URI would improve security.
client = MongoClient("mongodb://localhost:27017/")
db = client["chat_memory"]
collection = db["conversations"]
model = "gemma2:9b"


# Defines the structure of user input received by the API.
class UserInput(BaseModel):
    prompt: str

# Defines the structure of the bot's response sent back to the user.
class BotOutput(BaseModel):
    prompt_response: str


# Template with history. Also used to prompt the AI before user input (system prompt).
template = """You are a helpful assistant.
Here is our conversation history:
{history}
User: {input}
Assistant:"""


# Defines a prompt template for conversations, incorporating chat history.
prompt = PromptTemplate(input_variables=["history", "input"], template=template)


# Initializes memory storage using MongoDB to persist chat history.
mongo_memory = MongoMemory(collection)


# Initializes an in-memory conversation buffer to store recent messages.
memory = ConversationBufferMemory()


# Loads previous messages from MongoDB and adds them to the conversation memory.
previous_messages = mongo_memory.load_messages()
for msg in previous_messages:
    parts = msg.split("\n")
    memory.chat_memory.add_user_message(parts[0].replace("User: ", ""))
    memory.chat_memory.add_ai_message(parts[1].replace("Bot: ", ""))


# Initializes a conversational AI chain with the selected model and memory.
conversation = LLMChain(llm=ChatOllama(model=model), memory=memory, prompt=prompt, verbose=True)


# Function to generate a response from the AI based on the user's input.
def response_func(prompt: str) -> str:
    response = conversation.predict(input=prompt)
    mongo_memory.save_message(prompt, response)
    return response.content if hasattr(response, "content") else str(response)


# API endpoint to handle user input and return AI-generated responses.
@router.post("/Communicate", response_model=BotOutput)
async def process_endpoint(request: UserInput):
    response = response_func(request.prompt)
    return BotOutput(prompt_response=response)




