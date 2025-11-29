RAG_PROMPT_TEMPLATE = """
You are an AI assistant tasked with answering questions based on the provided context.

Context: {context}

Question: {question}

Based on the context, provide a concise and accurate answer. If the answer is not available in the context, state that you don't have enough information.
"""

print(f"Created {project_root}/prompts/rag_prompt.py")
