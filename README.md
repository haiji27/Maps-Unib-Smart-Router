
# 🗺️ UNIB Smart Route – Sistem Pencarian Rute Terpendek Universitas Bengkulu

UNIB Smart Route adalah aplikasi berbasis web yang digunakan untuk membantu pengguna menemukan rute tercepat dan terpendek di lingkungan Universitas Bengkulu. Sistem ini menerapkan konsep **teori graf** dan algoritma **Dijkstra** untuk menghitung jalur optimal berdasarkan bobot jarak antar lokasi kampus.

Aplikasi ini dilengkapi dengan peta interaktif berbasis Leaflet yang menampilkan visualisasi rute secara langsung di atas citra satelit Google Maps Hybrid.

---

# 📌 Fitur Utama

* 🗺️ Peta interaktif Universitas Bengkulu (Leaflet + Google Hybrid)
* 📍 Pemilihan titik awal dan tujuan
* ⚡ Perhitungan rute terpendek menggunakan algoritma Dijkstra
* 🛣️ Visualisasi jalur secara real-time di peta
* 📏 Perhitungan total jarak rute (meter)
* ⏱️ Estimasi waktu tempuh perjalanan
* 🚦 Simulasi kondisi kampus berdasarkan jam perjalanan
* 🧭 Navigasi antar gedung, simpang, dan titik penting kampus

---

#  Algoritma yang Digunakan

##  Dijkstra Shortest Path Algorithm

Algoritma Dijkstra digunakan untuk mencari jalur dengan bobot minimum pada graf berbobot positif.

### Implementasi dalam sistem:

* **Node (vertex)** → lokasi di Universitas Bengkulu (gedung, simpang, tikungan)
* **Edge** → jalan penghubung antar lokasi
* **Bobot (weight)** → jarak antar node dalam meter

Algoritma akan:

1. Menginisialisasi jarak semua node sebagai infinity
2. Menggunakan priority queue (heapq)
3. Memperbarui jarak terpendek setiap node
4. Melacak jalur menggunakan `previous_nodes`
5. Menghasilkan rute optimal dari start ke end

---

#  Arsitektur Sistem

##  Backend

* Python
* Flask
* Dijkstra Algorithm (heapq)

##  Frontend

* HTML5
* CSS3
* JavaScript
* Leaflet.js
* Leaflet Routing Machine

##  Peta & Data Geospasial

* Google Maps Hybrid Tiles
* Koordinat lokasi Universitas Bengkulu (lat, lng)

---

#  Struktur Proyek

```
project/
│
├── app.py              # Backend Flask (routing + API)
├── dijkstra.py         # Implementasi algoritma Dijkstra
│
├── templates/
│   └── index.html      # Tampilan utama (UI + peta)
│
├── static/
│   └── style.css       # Styling aplikasi
│
├── requirements.txt
└── README.md
```

---

#  Cara Menjalankan Program

### 1. Install dependency

```bash
pip install -r requirements.txt
```

### 2. Jalankan server Flask

```bash
python app.py
```

### 3. Buka di browser

```
http://127.0.0.1:5000
```

---

#  Alur Kerja Sistem

1. User membuka aplikasi web
2. Sistem menampilkan peta Universitas Bengkulu
3. User memilih titik awal dan tujuan
4. Frontend mengirim request ke backend Flask
5. Backend menjalankan algoritma Dijkstra
6. Sistem menghitung rute terpendek + jarak total
7. Hasil dikirim kembali ke frontend (JSON)
8. Jalur ditampilkan di peta interaktif

---

#  Kompleksitas Algoritma

Algoritma Dijkstra yang digunakan memiliki kompleksitas:

```
O((V + E) log V)
```

### Keterangan:

* **V** = jumlah node (lokasi kampus)
* **E** = jumlah edge (jalan penghubung)

Algoritma ini cukup efisien untuk sistem navigasi skala kampus karena jumlah node masih terbatas dan terstruktur.

---

#  Tujuan Pengembangan

* Membantu mahasiswa baru mengenal lingkungan kampus
* Mempermudah navigasi lokasi di Universitas Bengkulu
* Menerapkan teori graf dalam kasus nyata
* Implementasi algoritma Dijkstra dalam sistem web
* Sebagai proyek pembelajaran Kecerdasan Buatan / Struktur Data

---

#  Pengembang

Proyek ini dikembangkan sebagai tugas akademik pada Program Studi Teknik Informatika Universitas Bengkulu.

---

