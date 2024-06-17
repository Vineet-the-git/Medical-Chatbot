from src.components.predictor import predict
import gradio as gr

if __name__=="__main__":
    gr.ChatInterface(predict).launch()
