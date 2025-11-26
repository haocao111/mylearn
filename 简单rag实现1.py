import os
from llama_index.core import SimpleDirectoryReader ,VectorStoreIndex,Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

配置LLM
Settings.llm = Ollama(
    model="your model",
    base_url="your model base url",
    temperature=0.7,
    request_timeout = 120
)
Settings.embed_model = OllamaEmbedding(
    model="your model",
    base_url="your model base url"
)

try:
    documents= SimpleDirectoryReader(input_files=["you filename"]).load_data()
except Exception as e:
    print(e)
    exit()

print("索引建立ing")
index = VectorStoreIndex.from_documents(documeent)
print("finish")
#构建引擎
query_engine=index.as_query_engine()
print("finish")


question ="your questing"
print("查询中")
respone = query_engine.query(question)
print("回答如下")
print(respone)
