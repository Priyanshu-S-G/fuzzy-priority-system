import gradio as gr
from main import run_priority_system


def calculate_priority(urgency, impact, effort, risk):
    try:
        score, label = run_priority_system(urgency, impact, effort, risk)

        # Color coding
        if label == "High":
            color = "red"
        elif label == "Medium":
            color = "orange"
        else:
            color = "green"

        # Progress bar (simple HTML)
        progress_html = f"""
        <div style="background:#444; border-radius:5px; width:100%; height:20px;">
            <div style="width:{score}%; background:{color}; height:100%; border-radius:5px;"></div>
        </div>
        """

        # Interpretation text
        interpretation = (
            f"This task is {label.lower()} priority. "
            f"Higher urgency, impact, and risk increase priority, "
            f"while effort reduces it."
        )

        # Styled label
        styled_label = f"<span style='color:{color}; font-weight:bold;'>{label}</span>"

        return round(score, 2), styled_label, progress_html, interpretation

    except ValueError as e:
        return 0.0, "Error", "", str(e)


with gr.Blocks(title="Fuzzy Priority Allocation System") as app:
    gr.Markdown("# Fuzzy Priority Allocation System")

    with gr.Row():
        with gr.Column():
            urgency = gr.Slider(0, 10, value=5, step=0.1, label="Urgency")
            impact  = gr.Slider(0, 10, value=5, step=0.1, label="Impact")
            effort  = gr.Slider(0, 10, value=5, step=0.1, label="Effort")
            risk    = gr.Slider(0, 10, value=5, step=0.1, label="Risk")
            btn     = gr.Button("Calculate Priority", variant="primary")

        with gr.Column():
            score_out = gr.Number(label="Priority Score (0–100)")
            label_out = gr.HTML(label="Priority Label")
            progress_bar = gr.HTML(label="Priority Visualization")
            interpretation_out = gr.Textbox(label="Explanation")

    btn.click(
        fn=calculate_priority,
        inputs=[urgency, impact, effort, risk],
        outputs=[score_out, label_out, progress_bar, interpretation_out],
    )

if __name__ == "__main__":
    app.launch()