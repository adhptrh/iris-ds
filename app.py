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
        colname = df.at[i,col]
        if isinstance(colname, float):
            colname = "undefined"
        for key in data:
            if key == colname:
                data[colname] += 1
                found = True
        if not found:
            data[colname] = 1
    return data

data_siswa = pandas.read_csv("DataSiswaBaru.csv")
jenis_kelamin = getData(data_siswa,"jenkel")
pekerjaan_ortu =  getData(data_siswa,"pekerjaan_ortu")
kabkota =  getData(data_siswa,"kabkota")
jenis_sekolah =  getData(data_siswa,"jenis_sekolah")

@app.route("/")
def main():
    fig, ax = plt.subplots()
    for key, val in jenis_kelamin.items():
        teks = "Laki-Laki" if key == "L" else "Perempuan" if key == "P" else key
        barz = ax.bar(teks,val,label=teks)
        ax.bar_label(barz,fmt="%d")
    ax.set_ylabel("Jumlah")
    ax.legend()
    plt.savefig("static/graph1.png")

    fig, ax = plt.subplots()
    fig.set_size_inches(15,6)
    for key, val in pekerjaan_ortu.items():
        lol = ax.barh(key,val,label=key)
        ax.bar_label(lol,fmt="%d")
    ax.set_xlabel("Jumlah")
    ax.set_ylabel("Jenis Pekerjaan Orang Tua")
    plt.savefig("static/graph2.png")

    fig, ax = plt.subplots()
    fig.set_size_inches(15,6)
    for key, val in kabkota.items():
        lol = ax.barh(key,val,label=key)
        ax.bar_label(lol,fmt="%d")
    ax.set_xlabel("Jumlah")
    ax.set_ylabel("Kabupaten/Kota")
    plt.savefig("static/graph3.png")

    fig, ax = plt.subplots()
    for key, val in jenis_sekolah.items():
        lol = ax.bar(key,val,label=key)
        ax.bar_label(lol,fmt="%d")
    ax.set_xlabel("Jumlah")
    ax.set_ylabel("Jenis Sekolah")
    plt.savefig("static/graph4.png")
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
