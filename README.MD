# 📝 Notion-Lite: Task & Progress Tracker

Notion-Lite adalah aplikasi pelacak tugas sederhana berbasis Python + Flask + Tailwind CSS yang memungkinkan pengawas atau kepala proyek memantau progres pekerjaan para anggota/karyawan tanpa login atau registrasi.

## 🚀 Fitur Utama
- Tambah tugas dan milestone via **terminal (CLI)**
- Tampilkan progres di web (Flask) dengan UI modern (Tailwind CSS)
- Input:
  - Nama user/karyawan
  - Aktivitas (mau ngapain?)
  - Status: `Belum`, `Sedang`, `Selesai`
  - Deadline tugas
- **Progress bar** otomatis dari status tugas
- **Riwayat aktivitas** ditampilkan di halaman web
- **Animasi UI ringan** (transisi, efek hover)

## 📦 Teknologi
- Python 3.12.6
- Flask 3.1.1
- Tailwind CSS (via CDN)
- HTML + Jinja2 (template rendering)

## 💡 Contoh Penggunaan
Misalnya, kamu seorang kepala tim dan ingin memberikan tugas ke anggota tanpa ribet login. Kamu cukup:
1. Jalankan server Flask
2. Input data dari terminal
3. Buka browser untuk melihat progress seluruh tim

## 📂 Struktur Project
NotionCopy/
├── app.py # Flask backend
├── templates/
│ └── index.html # Frontend HTML + Tailwind
├── static/
│ └── style.css # (Opsional) custom style
├── requirements.txt
└── README.md
