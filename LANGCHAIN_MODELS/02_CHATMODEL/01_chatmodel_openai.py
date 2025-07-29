from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model = "gpt-4", temperature=0.8)

# result = model.invoke("What is the capital of India")
result = model.invoke("Suggest me a 5 line poem on cricket")
print(result.content)