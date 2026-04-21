import gradio as gr
from main import run_priority_system


def calculate_priority(urgency, impact, effort, risk):
    """Bridge Gradio UI inputs to run_priority_system()."""
    try:
        score, label = run_priority_system(urgency, impact, effort, risk)
        return round(score, 2), label
    except ValueError as e:
        return 0.0, f"Input error: {e}"


with gr.Blocks(title="Fuzzy Priority Allocation System") as app:
    gr.Markdown("# Fuzzy Priority Allocation System")
    gr.Markdown("Adjust inputs → click **Calculate Priority** → get score and label.")

    with gr.Row():
        with gr.Column():
            urgency = gr.Slider(0, 10, value=5, step=0.1, label="Urgency")
            impact  = gr.Slider(0, 10, value=5, step=0.1, label="Impact")
            effort  = gr.Slider(0, 10, value=5, step=0.1, label="Effort")
            risk    = gr.Slider(0, 10, value=5, step=0.1, label="Risk")
            btn     = gr.Button("Calculate Priority", variant="primary")

        with gr.Column():
            score_out = gr.Number(label="Priority Score (0–100)")
            label_out = gr.Textbox(label="Priority Label (Low / Medium / High)")

    btn.click(
        fn=calculate_priority,
        inputs=[urgency, impact, effort, risk],
        outputs=[score_out, label_out],
    )

if __name__ == "__main__":
    app.launch()