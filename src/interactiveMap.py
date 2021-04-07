from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from Graph import *

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
    adjacencyMatrix = [[0 for i in range (N)] for j in range (N)]
    for i in range(N):
        node_name, lng, lat = inp.readline().split(',')
        nodes.append((node_name, float(lng), float(lat)))
    
    for i in range(N):
        row = inp.readline().split(' ')
        for j in range(N):
            if row[j][0] == '1':
                adjacencyMatrix[i][j] = 1
    graph = Graph(nodes, adjacencyMatrix)
    return graph

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
            graph = readInput(input_filename)
            # jalankan algoritme A*
            
            # tampilkan hasil
            return redirect(url_for('ResultsPage', filename=input_filename[:-4]))
    return render_template('main-page.html')

# results page
@app.route('/results-<filename>', methods=['GET', 'POST'])
def ResultsPage(filename):
    graph = readInput(filename+'.txt')
    if request.method == 'POST':
        if 'startnode' in request.form and 'endnode' in request.form:
            start_node = request.form['startnode']
            end_node = request.form['endnode']
            result = graph.Astar(start_node, end_node, True)
            return render_template('results-page.html', result=result, nodes=graph.nodes(), edge_list=graph.edgeList())
    return render_template('results-page.html', result={"path":[], "distance":0}, nodes=graph.nodes(), edge_list=graph.edgeList())

if __name__ == '__main__':
    app.run()