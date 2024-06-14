from src.components.predictor import predict

import gradio as gr

gr.ChatInterface(predict).launch()
