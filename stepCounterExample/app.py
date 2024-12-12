from flask import Flask, render_template, request, redirect
import csv
import matplotlib.pyplot as plt

def get_data():
    file= open("steps.csv","r")
    data = list(csv.reader(file))
    file.close()
    data.pop(0)
    #print(data)
    return data

def make_graph(steps_data):
    steps=[]
    dates=[]
    for row in steps_data:
        dates.append(row[0])
        steps.append(int(row[1]))
    #print(steps)
    #print(dates)
    plt.switch_backend("Agg")
    plt.plot(dates,steps,"o-r")
    plt.title("Graph of my steps")
    plt.xlabel("dates")
    plt.ylabel("steps")
    plt.xticks(rotation=90)
    plt.savefig("./static/mySteps.png",bbox_inches="tight")
    plt.close()


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/viewData")
def view_data():
    data=get_data()
    #creates a list of lists each list item has 2 values [[date, steps],[date,steps]] so can be accessed using data[0] or data[1]
    # to access all data points use a loop this needs to be rendered in html page viewData.html
    
    for innerList in data:
        print(innerList[0])  # Access the date
        print(innerList[1])  # Access the steps
    #or unpack directly
    for date,steps in data:
        print(date)
        print(steps)
        
    make_graph(data)
    return render_template("viewData.html",info=data)

@app.route("/addData", methods=["GET", "POST"])
def add_data():
    if request.method == "POST":
        date= request.form.get("date")
        steps= request.form.get("steps")
        file = open("steps.csv","a")
        file.write(date+","+steps+"\n")
        file.close()
        return render_template("index.html")
    else:
        return render_template("addData.html")

if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0", port=8000)
    
