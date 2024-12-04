from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Global DataFrame to store user input
df = pd.DataFrame(columns=["Risk Category", "Freq_lb", "Freq_ub", "Sev_lb", "Sev_ub"])

# Route for the main page with the input form
@app.route("/", methods=["GET", "POST"])
def index():
    global df
    if request.method == "POST":
        # Collect data from the form
        risk_category = request.form.get("risk_category")
        freq_lb = float(request.form.get("freq_lb"))
        freq_ub = float(request.form.get("freq_ub"))
        sev_lb = float(request.form.get("sev_lb"))
        sev_ub = float(request.form.get("sev_ub"))

        # Add the new row to the DataFrame
        df = pd.concat([
            df,
            pd.DataFrame([{
                "Risk Category": risk_category,
                "Freq_lb": freq_lb,
                "Freq_ub": freq_ub,
                "Sev_lb": sev_lb,
                "Sev_ub": sev_ub
            }])
        ], ignore_index=True)
        return redirect(url_for("index"))

    # Render the input form and pass the DataFrame directly
    return render_template("index.html", data=df)

# Route to generate and display the graph
@app.route("/generate_graph")
def generate_graph():
    global df
    if df.empty:
        return "No data available to plot!"

    # Use the provided plotting logic
    num_rows = len(df)
    colors = cm.tab10(np.linspace(0, 1, num_rows))  # Use a colormap for distinct colors

    # Set up the plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Draw the grid for risk zones
    for i in range(1, 6):
        ax.axhline(y=i, color='lightgrey', linestyle='--', linewidth=0.7)
        ax.axvline(x=i, color='lightgrey', linestyle='--', linewidth=0.7)

    # Plot each risk
    for index, row in df.iterrows():
        color = colors[index]  # Assign a unique color based on the index
        label = row["Risk Category"]
        freq_lb, freq_ub = row["Freq_lb"], row["Freq_ub"]
        sev_lb, sev_ub = row["Sev_lb"], row["Sev_ub"]

        # Plot points and lines
        ax.scatter((freq_lb + freq_ub) / 2, (sev_lb + sev_ub) / 2, color=color, label=label)
        if freq_lb != freq_ub:
            ax.plot([freq_lb, freq_ub], [(sev_lb + sev_ub) / 2] * 2, linestyle='-', color=color)
        if sev_lb != sev_ub:
            ax.plot([(freq_lb + freq_ub) / 2] * 2, [sev_lb, sev_ub], linestyle='-', color=color)

    # Customize the plot
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xticks(range(1, 6))
    ax.set_yticks(range(1, 6))
    ax.set_xlabel("Frequency Level")
    ax.set_ylabel("Severity Level")
    ax.set_title("Risk Map")
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), title="Risk Categories")

    # Save the plot
    plot_path = os.path.join("static", "plot.png")
    plt.grid(False)
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()

    return render_template("graph.html", plot_url=plot_path)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
