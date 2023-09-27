from hugchat import hugchat

chatbot = hugchat.ChatBot()
question = 'Can you help me do some prompt engineering?'
answer = chatbot.chat(question)
print(f"{answer}")