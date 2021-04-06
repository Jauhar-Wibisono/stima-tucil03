from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.abspath('../test') # directory dokumen-dokumen
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# main page
@app.route('/', methods=['GET', 'POST'])
def MainPage():
    if request.method == 'POST':
        if 'upload' in request.files: # website dapet input file
            # dapatkan dan simpan file input
            input_file = request.files['upload']
            input_filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], input_filename))
            # baca input
            # format input:
            # Baris pertama berisi bilangan bulat N yang menyatakan banyak simpul
            # N baris berikutnya berisi sebuah string dan dua bilangan bulat yang menyatakan nama dan koordinat simpul
            # N baris berikutnya berisi adjacency matrix
            # inp = open(os.path.join(app.config['UPLOAD_FOLDER'], input_filename))
            # for line in inp
            # jalankan algoritme A*
            distance = 100 # testing value
            path = [('Bucharest', 44.457, 26.093), ('Arad', 46.181, 21.312), ('Zerind', 46.624, 21.518)] # testing value
            # tampilkan hasil
            return render_template('results-page.html', distance=distance, path=path)
    return render_template('main-page.html')
