from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.abspath('../test') # directory dokumen-dokumen
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def readInput(filename):
    # format input:
    # Baris pertama berisi bilangan bulat N yang menyatakan banyak simpul
    # N baris berikutnya berisi sebuah string dan dua bilangan bulat yang menyatakan nama dan koordinat simpul
    # N baris berikutnya berisi adjacency matrix (sementara boolean)
    inp = open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    N = int(inp.readline())
    nodes = []
    edge_list = []
    for i in range(N):
        node_name, lng, lat = inp.readline().split(',')
        nodes.append((node_name, float(lng), float(lat)))
    for i in range(N):
        row = inp.readline().split(' ')
        for j in range(i):
            if row[j] == '1':
                edge_list.append((nodes[i][1], nodes[i][2], nodes[j][1], nodes[j][2]))
    return (N, nodes, edge_list)

# main page
@app.route('/', methods=['GET', 'POST'])
def MainPage():
    if request.method == 'POST':
        if 'upload' in request.files: # website dapet input file
            # dapatkan dan simpan file input
            input_file = request.files['upload']
            input_filename = secure_filename(input_file.filename)
            input_file.save(os.path.join(app.config['UPLOAD_FOLDER'], input_filename))
            # baca input
            N, nodes, edge_list = readInput(input_filename)
            # jalankan algoritme A*
            distance = 100 # testing value
            path = [(44.457, 26.093, 46.181, 21.31), (46.181, 21.312, 46.624, 21.518)] # testing value
            # tampilkan hasil
            return render_template('results-page.html', distance=distance, path=path, nodes=nodes, edge_list=edge_list)
    return render_template('main-page.html')
