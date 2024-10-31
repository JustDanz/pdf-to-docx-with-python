# PDF to DOCX Converter With Python

Proyek ini adalah aplikasi web sederhana yang dibangun dengan Flask, yang memungkinkan pengguna untuk mengonversi file PDF menjadi format DOCX. Aplikasi ini menggunakan pustaka `pdf2docx` untuk melakukan konversi.

## Fitur

- Unggah file PDF untuk konversi.
- Konversi file PDF menjadi file DOCX.
- Unduh file DOCX yang telah dikonversi.

## Prerequisites

Sebelum menjalankan aplikasi ini, pastikan Anda memiliki Python 3 dan pip terinstal di sistem Anda. Anda juga perlu menginstal beberapa pustaka yang diperlukan. Anda dapat melakukan ini dengan perintah berikut:

```bash
pip install Flask pdf2docx
```

## Struktur Proyek

```
/pdf-to-docx-converter
│
├── app.py                # File utama aplikasi Flask
├── requirements.txt      # Daftar pustaka yang diperlukan
├── uploads               # Folder untuk menyimpan file yang diunggah
└── templates
    └── index.html       # Template HTML untuk tampilan pengguna
```

## Cara Menjalankan Aplikasi

1. **Clone repositori ini**:
   ```bash
   git clone https://github.com/username/pdf-to-docx-converter.git
   cd pdf-to-docx-converter
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan aplikasi**:
   ```bash
   python app.py
   ```

4. **Akses aplikasi**:
   Buka browser dan pergi ke [http://127.0.0.1:5000](http://127.0.0.1:5000) untuk menggunakan aplikasi.

## Cara Menggunakan

1. Pilih file PDF yang ingin Anda konversi.
2. Klik tombol "Upload" untuk memulai konversi.
3. Setelah konversi selesai, Anda akan mendapatkan tautan untuk mengunduh file DOCX yang telah dikonversi.

## Kontribusi
Jika ingin berkontribusi pada proyek ini, silakan fork repositori dan kirim pull request.

## English Translate 
Here’s the translated README in English:

# PDF to DOCX Converter With Python

This project is a simple web application built with Flask that allows users to convert PDF files into DOCX format. This application uses the `pdf2docx` library for the conversion process.

## Features

- Upload PDF files for conversion.
- Convert PDF files to DOCX format.
- Download the converted DOCX file.

## Prerequisites

Before running this application, make sure you have Python 3 and pip installed on your system. You will also need to install some required libraries. You can do this using the following command:

```bash
pip install Flask pdf2docx
```

## Project Structure

```
/pdf-to-docx-converter
│
├── app.py                # Main Flask application file
├── requirements.txt      # List of required libraries
├── uploads               # Folder to store uploaded files
└── templates
    └── index.html       # HTML template for user interface
```

## How to Run the Application

1. **Clone this repository**:
   ```bash
   git clone https://github.com/username/pdf-to-docx-converter.git
   cd pdf-to-docx-converter
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the application**:
   Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to use the application.

## How to Use

1. Select the PDF file you want to convert.
2. Click the "Upload" button to start the conversion.
3. Once the conversion is complete, you will receive a link to download the converted DOCX file.

## Contribution

If you would like to contribute to this project, please fork the repository and submit a pull request.
```

Feel free to customize any part of the translation to better fit your style!
