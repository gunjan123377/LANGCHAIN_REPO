from langchain_openai import ChatOpenAI
from langchain_core.prompts import load_prompt, PromptTemplate
from dotenv import load_dotenv
import streamlit as st
from pathlib import Path

load_dotenv()

st.header("Research Tools")
# user_input = st.text_input("Enter your prompts")
model = ChatOpenAI(model="gpt-4", temperature=0.5)

paper_input = st.selectbox( "Select Research Paper Name",
                            ["Attention Is All You Need",
                             "BERT: Pre-training of Deep Bidirectional Transformers",
                             "GPT-3: Language Models are Few-Shot Learners",
                             "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style",
                            ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] )

length_input = st.selectbox( "Select Explanation Length",
                             ["Short (1-2 paragraphs)",
                              "Medium (3-5 paragraphs)",
                              "Long (detailed explanation)"] )

# template = PromptTemplate(
#     template="""
# Please summarize the research paper titled "{paper_input}" with the following specifications:
# Explanation Style: {style_input}
# Explanation Length: {length_input}
# 1. Mathematical Details:
#    - Include relevant mathematical equations if present in the paper.
#    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
# 2. Analogies:
#    - Use relatable analogies to simplify complex ideas.
# If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
# Ensure the summary is clear, accurate, and aligned with the provided style and length.
# """,
# input_variables=['paper_input', 'style_input','length_input'],
# validate_template=True
# )

script_dir = Path(__file__).parent
template_path = script_dir / "template.json"
template = load_prompt(template_path)
# template = load_prompt("C:/Users/Gunjan Kumar/CODING_LEARNING/CODING/AI_ML/LANGCHAIN_PROJECTS/LANGCHAIN_REPO/LANGCHAIN_PROMPTS/template.json")

prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input,
})

if st.button("Summarize"):
    response = model.invoke(prompt)
    st.text(response.content)
