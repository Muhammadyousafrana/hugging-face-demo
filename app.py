from transformers import pipeline
import gradio as gr

# Load the summarization model
model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Text Summarization App")
    gr.Markdown("Enter a block of text below and click Submit to generate a summary.")
    
    with gr.Row():
        textbox = gr.Textbox(placeholder="Enter text to summarize", lines=6)
    
    submit_btn = gr.Button("Summarize")
    
    output = gr.Textbox(label="Summary", interactive=False)
    
    submit_btn.click(predict, inputs=textbox, outputs=output)

# Launch the Gradio app
demo.launch()
