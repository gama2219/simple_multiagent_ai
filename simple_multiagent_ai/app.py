from langchain_core.messages.human import HumanMessage
from langchain_core.messages.ai import AIMessage
from agents import super_visor
import gradio as gr
import uuid


config = {"configurable": {"thread_id": str(uuid.uuid4())}}

def  history_fromat(history:str)->dict:
  response ={'role':(role :='user' if isinstance(history,HumanMessage) else 'assistant' ),'content':history.content}
  return response

def respond(message, chat_history):
  bot_message = super_visor.invoke({"messages": [HumanMessage(content=message)]},config)
  final_bot_message=bot_message.get('messages')[-1]
  bot_response_formated=history_fromat(final_bot_message)
  chat_history.append({"role": "user", "content": message})
  chat_history.append(bot_response_formated)

  return "", chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])
    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
   demo.launch(debug=True, share=False)

