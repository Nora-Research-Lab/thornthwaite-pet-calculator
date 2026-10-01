import gradio as gr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from thornthwaite_pet_calculator import monthly_pet

def compute_pet(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, lat_abs, hemisphere):
    temps = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12]
    lat_signed = lat_abs if hemisphere == "Northern" else -lat_abs
    month_labels = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    pets, annual = monthly_pet(temps, lat_signed)
    rows = [(month_labels[i], temps[i], round(pets[i],2)) for i in range(12)]
    df = gr.Dataframe(value=rows, headers=["Month","Temperature (°C)","PET (mm/month)"], label="Monthly PET")
    fig, ax = plt.subplots(figsize=(8,4))
    ax.bar(month_labels, pets, color="steelblue")
    ax.set_ylabel("PET (mm/month)")
    ax.set_title("Monthly Potential Evapotranspiration (Thornthwaite)")
    plt.tight_layout()
    return df, fig, round(annual, 1)

with gr.Blocks(title="Thornthwaite PET Calculator") as demo:
    gr.Markdown("# Thornthwaite PET Calculator")
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Input Data")
            temp_inputs = [gr.Number(label=f"Month {i+1} (Jan–Dec) °C", step=0.1, minimum=0, maximum=50, value=0.0) for i in range(12)]
            lat_abs = gr.Slider(minimum=0, maximum=90, step=0.5, label="Absolute Latitude (°)", value=0.0)
            hemisphere = gr.Radio(choices=["Northern", "Southern"], value="Northern", label="Hemisphere")
            compute_btn = gr.Button("Calculate")
        with gr.Column():
            gr.Markdown("### Results")
            output_table = gr.Dataframe(label="Monthly PET Table")
            output_plot = gr.Plot(label="Monthly PET Bar Chart")
            output_annual = gr.Number(label="Annual PET (mm)", precision=1)
    compute_btn.click(
        fn=compute_pet,
        inputs=temp_inputs + [lat_abs, hemisphere],
        outputs=[output_table, output_plot, output_annual]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
