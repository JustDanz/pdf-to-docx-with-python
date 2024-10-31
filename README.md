# PDF to DOCX Converter

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
