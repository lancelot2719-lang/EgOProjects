import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# --- 1. ЗАГРУЗКА И ПОДГОТОВКА ДОКУМЕНТОВ ---
file_path = "my_knowledge.txt"
loader = TextLoader(file_path, encoding='utf-8')
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
chunks = text_splitter.split_documents(documents)
print(f"Документ загружен и разбит на {len(chunks)} частей.")

# --- 2. СОЗДАНИЕ ВЕКТОРНОЙ БАЗЫ ДАННЫХ ---
embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
vector_db = FAISS.from_documents(chunks, embeddings)
print("Векторная база данных создана.")

# --- 3. НАСТРОЙКА LLM (ЧЕРЕЗ LM STUDIO) ---
llm = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="not-needed",
    temperature=0.0,
    model_name="local-model"
)
print("Подключение к локальной LLM через LM Studio установлено.")

# --- 4. СОЗДАНИЕ ЦЕПОЧКИ RAG (НОВЫЙ СПОСОБ LCEL) ---

# Создаем "извлекатель" (retriever)
retriever = vector_db.as_retriever(search_kwargs={"k": 3})

# Функция для форматирования найденных документов в одну строку
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Создаем шаблон для запроса к LLM
prompt_template = """
Используй следующий контекст, чтобы ответить на вопрос в конце.
Если ты не знаешь ответа, просто скажи, что не знаешь, не пытайся придумывать ответ.
Отвечай максимально кратко и по делу.

Контекст:
{context}

Вопрос:
{question}

Полезный ответ:"""
prompt = PromptTemplate.from_template(prompt_template)

# Собираем цепочку с помощью нового синтаксиса LCEL (символ | )
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print("\n--- RAG-система готова к работе! ---")
print("Введите 'exit' для выхода.\n")

# --- 5. ЗАПУСК И ВЗАИМОДЕЙСТВИЕ ---
while True:
    query = input("Ваш вопрос: ")
    if query.lower() == 'exit':
        break
    
    # Вызываем цепочку с помощью .invoke()
    result = rag_chain.invoke(query)
    
    print(f"\nОтвет: {result}\n")