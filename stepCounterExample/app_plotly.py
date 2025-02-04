from flask import Flask, render_template, request, redirect, jsonify
import csv
import plotly.graph_objs as go
import plotly.utils
import json

app = Flask(__name__)

def get_data():
    with open("steps.csv", "r") as file:
        data = list(csv.reader(file))
    data.pop(0)  # Remove header
    return data

def make_graph(steps_data):
    dates = [row[0] for row in steps_data]
    steps = [int(row[1]) for row in steps_data]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates, y=steps, mode='lines+markers',
        marker=dict(color='red'),
        name="Steps Data"
    ))
    
    fig.update_layout(
        title="Interactive Graph of Steps",
        xaxis_title="Dates",
        yaxis_title="Steps",
        xaxis=dict(tickangle=45),
        template="plotly_dark"  # Optional theme
    )

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/viewData")
def view_data():
    data = get_data()
    graphJSON = make_graph(data)
    return render_template("viewData.html", info=data, graphJSON=graphJSON)

@app.route("/addData", methods=["GET", "POST"])
def add_data():
    if request.method == "POST":
        date = request.form.get("date")
        steps = request.form.get("steps")
        with open("steps.csv", "a") as file:
            file.write(date + "," + steps + "\n")
        return redirect("/")
    return render_template("addData.html")

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8000)
