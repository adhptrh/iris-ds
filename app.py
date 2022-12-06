from flask import Flask, render_template, send_from_directory, request, redirect
import matplotlib.pyplot as plt
import numpy as np
import pandas
import csv

app = Flask(__name__)



@app.route("/")
def main():
    
    iris_df = pandas.read_csv("IRIS.csv")
    fig, ax = plt.subplots()
    sepal_width_iris_setosa = []
    sepal_length_iris_setosa = []
    sepal_width_versicolor = []
    sepal_length_versicolor = []
    sepal_width_virginica = []
    sepal_length_virginica = []
    for i in range(len(iris_df.index)):
        if (iris_df.at[i, "species"] == "Iris-setosa"):
            sepal_width_iris_setosa.append(iris_df.at[i, "sepal_width"])
            sepal_length_iris_setosa.append(iris_df.at[i, "sepal_length"])
        elif (iris_df.at[i, "species"] == "Iris-versicolor"):
            sepal_width_versicolor.append(iris_df.at[i, "sepal_width"])
            sepal_length_versicolor.append(iris_df.at[i, "sepal_length"])
        elif (iris_df.at[i, "species"] == "Iris-virginica"):
            sepal_width_virginica.append(iris_df.at[i, "sepal_width"])
            sepal_length_virginica.append(iris_df.at[i, "sepal_length"])
    ax.scatter(
        sepal_width_iris_setosa,
        sepal_length_iris_setosa,
        200,
        c="green",
        alpha=0.5,
        marker=(4, 0),
        label="Iris Setosa"
    )
    ax.scatter(
        sepal_width_versicolor,
        sepal_length_versicolor,
        200,
        c="red",
        alpha=0.5,
        marker=(3, 0),
        label="Iris Versicolor"
    )
    ax.scatter(
        sepal_width_virginica,
        sepal_length_virginica,
        200,
        c="blue",
        alpha=0.5,
        marker=(5, 0),
        label="Iris Virginicia"
        )
    ax.set_xlabel("Sepal Width")
    ax.set_ylabel("Sepal Length")
    ax.legend()
    plt.savefig("static/graph1.png")

    fig, ax = plt.subplots()
    petal_width_iris_setosa = []
    petal_length_iris_setosa = []
    petal_width_versicolor = []
    petal_length_versicolor = []
    petal_width_virginica = []
    petal_length_virginica = []
    for i in range(len(iris_df.index)):
        if (iris_df.at[i, "species"] == "Iris-setosa"):
            petal_width_iris_setosa.append(iris_df.at[i, "petal_width"])
            petal_length_iris_setosa.append(iris_df.at[i, "petal_length"])
        elif (iris_df.at[i, "species"] == "Iris-versicolor"):
            petal_width_versicolor.append(iris_df.at[i, "petal_width"])
            petal_length_versicolor.append(iris_df.at[i, "petal_length"])
        elif (iris_df.at[i, "species"] == "Iris-virginica"):
            petal_width_virginica.append(iris_df.at[i, "petal_width"])
            petal_length_virginica.append(iris_df.at[i, "petal_length"])
    ax.scatter(
        petal_width_iris_setosa,
        petal_length_iris_setosa,
        200, c="green", alpha=0.5,
        marker=(4, 0),
        label="Iris Setosa"
    )
    ax.scatter(
        petal_width_versicolor,
        petal_length_versicolor,
        200,
        c="red",
        alpha=0.5,
        marker=(3, 0),
        label="Iris Versicolor"
    )
    ax.scatter(
        petal_width_virginica,
        petal_length_virginica,
        200,
        c="blue",
        alpha=0.5,
        marker=(5, 0),
        label="Iris Virginicia"
    )
    ax.set_xlabel("Petal Width")
    ax.set_ylabel("Petal Length")
    ax.legend()
    plt.savefig("static/graph2.png")
    return render_template("index.html")



@app.route("/upload", methods=["GET","POST"])
def upload():
    if request.method == "GET":
        return render_template("uploadcsv.html")
    elif request.method == "POST":
        file = request.files['file']
        file.save("./IRIS.csv")
        return redirect("/")

@app.route("/assets/<path:filename>")
def assets(filename):
    return send_from_directory(app.root_path+"/static/assets", filename)
