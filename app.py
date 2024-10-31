from flask import Flask, render_template, request, redirect, url_for
from pdf2docx import Converter
import os

app = Flask(__name__)

# Folder untuk menyimpan file upload
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Ambil file dari form
        pdf_file = request.files['pdf_file']
        if pdf_file:
            # Simpan file PDF
            pdf_path = os.path.join(UPLOAD_FOLDER, pdf_file.filename)
            pdf_file.save(pdf_path)

            # Nama file output DOCX
            docx_filename = pdf_file.filename.rsplit('.', 1)[0] + '.docx'
            docx_path = os.path.join(UPLOAD_FOLDER, docx_filename)

            # Konversi PDF ke DOCX
            cv = Converter(pdf_path)
            cv.convert(docx_path, start=0, end=None)
            cv.close()

            return redirect(url_for('download_file', filename=docx_filename))

    return render_template('index.html')

@app.route('/uploads/<filename>')
def download_file(filename):
    return f'<h3>File berhasil dikonversi: <a href="{url_for("static", filename="uploads/" + filename)}">{filename}</a></h3>'

if __name__ == "__main__":
    app.run(debug=True)
