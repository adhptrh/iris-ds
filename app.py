from flask import Flask, render_template, send_from_directory, request, redirect
import matplotlib.pyplot as plt
import numpy as np
import pandas
import csv

app = Flask(__name__)

"""
atribut yg dipakai:
 jenkel, pekerjaan_ortu, kabkota, id_jenis_sekolah
"""

def getData(df, col):
    data = {}
    for i in range(len(df.index)):
        found = False
        for key in data:
            if key == df.at[i,col]:
                data[df.at[i,col]] += 1
                found = True
        if not found:
            data[df.at[i,col]] = 1
    return data

data_siswa = pandas.read_csv("DataSiswaBaru.csv")
jenis_kelamin = getData(data_siswa,"jenkel")
pekerjaan_ortu =  getData(data_siswa,"pekerjaan_ortu")
print(jenis_kelamin)
print(pekerjaan_ortu)


@app.route("/")
def main():
    fig, ax = plt.subplots()
    
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
