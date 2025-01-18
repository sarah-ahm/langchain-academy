from langchain_ollama import ChatOllama

llm = ChatOllama(
    model = "llama3.2",
    temperature = 0.8,
    num_predict = 256,
    # other params ...
)

from langchain_core.messages import AIMessage

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
ai_msg
print(ai_msg.content)