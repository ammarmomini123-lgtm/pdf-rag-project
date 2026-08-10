from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT_TEMPLATE = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an AI assistant for document question-answering. "
        "Answer the user question strictly using the provided context. "
        "If the answer is not present in the context, state that the information is unavailable in the document.\n\n"
        "Context:\n{context}"
    ),
    ("human", "{question}")
])