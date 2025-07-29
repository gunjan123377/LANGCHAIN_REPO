import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

endpoint=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",             # or conversational
    max_new_tokens=256,
    temperature=0.7,
    provider="auto",                    # or specify provider
    # huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

chat = ChatHuggingFace(llm=endpoint)
resp = chat.invoke("Write me a short poem about Patna.")
print(resp.content)
