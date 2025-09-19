import gradio as gr
from chatbot import chat

gr.ChatInterface(fn=chat, type="messages").launch()
