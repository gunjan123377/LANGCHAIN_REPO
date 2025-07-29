from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
# import os
# os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
#
# import torch
# torch.cuda.empty_cache()
#
# print(torch.cuda.memory_summary())

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("Write me a short poem about Nalanda.")
print(result.content)
