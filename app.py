from flask import Flask, jsonify, render_template, request
from dijkstra import hitung_dijkstra

app = Flask(__name__)

# =========================================================
# DATABASE KOORDINAT UNIB
# =========================================================

LOKASI_UNIB = {

    # =====================================================
    # GEDUNG UTAMA
    # =====================================================

    "Baitul_Hikmah": {
        "nama": "Masjid Baitul Hikmah UNIB",
        "lat": -3.758998904843866,
        "lng": 102.27594531784604
    },

    "Pertanian": {
        "nama": "Jurusan Pertanian",
        "lat": -3.75424,
        "lng": 102.27448
    },

    "Danau": {
        "nama": "Danau UNIB",
        "lat": -3.758340535553358,
        "lng": 102.27316635017067
    },

    "Fak_Pertanian": {
        "nama": "Dekanat Fakultas Pertanian",
        "lat": -3.7592653639836975,
        "lng": 102.26921092323761
    },

    "FISIP": {
        "nama": "Dekanat FISIP UNIB",
        "lat": -3.759057941399334,
        "lng": 102.27420377032269
    },

    "FKIP_Dekanat": {
        "nama": "Dekanat FKIP",
        "lat": -3.75752751578353,
        "lng": 102.27504437510467
    },

    "FKIP_UNIB": {
        "nama": "Gedung FKIP UNIB",
        "lat": -3.7563330297318243,
        "lng": 102.27746309824113
    },

    "FMIPA": {
        "nama": "Dekanat FMIPA",
        "lat": -3.7559251632647945,
        "lng": 102.27477918909301
    },

    "GB1": {
        "nama": "GB I",
        "lat": -3.756943977022895,
        "lng": 102.27377244448388
    },

    "GB2": {
        "nama": "GB II",
        "lat": -3.758028386241786,
        "lng": 102.27392351670319
    },

    "GB3": {
        "nama": "GB III",
        "lat": -3.7564955492161634,
        "lng": 102.27651194098199
    },

    "GB4": {
        "nama": "GB IV",
        "lat": -3.7560990016212075,
        "lng": 102.27642724889728
    },

    "GB5": {
        "nama": "GB V",
        "lat": -3.7555269326421925,
        "lng": 102.27646633755175
    },

    "Gedung_I": {
        "nama": "Gedung I Universitas Bengkulu",
        "lat": -3.75785,
        "lng": 102.27212
    },

    "Gedung_Layanan_Terpadu": {
        "nama": "Gedung Unit Layanan Terpadu",
        "lat": -3.757959261386435,
        "lng": 102.27188240336362
    },

    "GSG": {
        "nama": "Gedung Serba Guna (GSG)",
        "lat": -3.757559014553162,
        "lng": 102.27658884880597
    },

    "Hukum": {
        "nama": "Dekanat Fakultas Hukum",
        "lat": -3.760539347447866,
        "lng": 102.2684599046901
    },

    "Kedokteran": {
        "nama": "Fakultas Kedokteran",
        "lat": -3.7551498869496425,
        "lng": 102.27802336896973
    },

    "Lab_FKIP": {
        "nama": "Laboratorium Pembelajaran FKIP",
        "lat": -3.758364763506071,
        "lng": 102.27575700801209
    },

    "Lab_Terpadu_Teknik": {
        "nama": "Laboratorium Terpadu Teknik",
        "lat": -3.7585713405896026,
        "lng": 102.27737695784646
    },

    "Perpustakaan": {
        "nama": "Perpustakaan",
        "lat": -3.7567750826584216,
        "lng": 102.27483764361487
    },

    "PKM": {
        "nama": "Gedung PKM",
        "lat": -3.7564501208752543,
        "lng": 102.27582648464937
    },

    "Rektorat": {
        "nama": "Rektorat UNIB",
        "lat": -3.758940058037797,
        "lng": 102.2723616874821
    },

    "Stadion": {
        "nama": "Stadion UNIB",
        "lat": -3.757559014553162,
        "lng": 102.278133801168
    },

    "Teknik": {
        "nama": "Dekanat Fak. Teknik UNIB",
        "lat": -3.758340535553358,
        "lng": 102.27726476546437
    },

    "Teknologi_Pertanian": {
        "nama": "Jurusan Teknologi Pertanian",
        "lat": -3.75548,
        "lng": 102.27384
    },

    "UPA_TIK": {
        "nama": "UPA TIK Universitas Bengkulu",
        "lat": -3.7585400714115167,
        "lng": 102.27500668923412
    },

    # =====================================================
    # NODE SIMPANG
    # =====================================================

    "Simp_Rektorat_Utama": {
        "nama": "Simpang Depan Rektorat",
        "lat": -3.75860,
        "lng": 102.27260
    },

    "Simp_Layanan_Terpadu": {
        "nama": "Simpang Layanan Terpadu",
        "lat": -3.75790,
        "lng": 102.27220
    },

    "Simp_Pertanian_Utara": {
        "nama": "Simpang Jalur Atas Pertanian",
        "lat": -3.75680,
        "lng": 102.27320
    },

    "Simp_Perpustakaan": {
        "nama": "Simpang Bundaran Perpustakaan",
        "lat": -3.75670,
        "lng": 102.27520
    },

    "Simp_Mipa_Utara": {
        "nama": "Simpang Lingkar Luar MIPA",
        "lat": -3.75600,
        "lng": 102.27500
    },

    "Simp_GB5": {
        "nama": "Pertigaan Akses GB V",
        "lat": -3.75580,
        "lng": 102.27640
    },

    "Simp_GB_Cluster": {
        "nama": "Simpang Akses Gedung Bersama",
        "lat": -3.75620,
        "lng": 102.27650
    },

    "Simp_Fkip_Stadion": {
        "nama": "Pertigaan Akses FKIP-Stadion",
        "lat": -3.75680,
        "lng": 102.27780
    },

    "Simp_Teknik_Gsg": {
        "nama": "Simpang Akses Teknik-GSG",
        "lat": -3.75790,
        "lng": 102.27690
    },

    "Simp_Selatan_Fisip": {
        "nama": "Simpang Jalur Utama FISIP",
        "lat": -3.75850,
        "lng": 102.27490
    },

    "Simp_Gedung_I": {
        "nama": "Simpang Koridor Barat Gedung I",
        "lat": -3.75820,
        "lng": 102.27140
    },

    # =====================================================
    # NODE TIKUNGAN
    # =====================================================

    "Tikungan_GB": {
        "nama": "Tikungan GB",
        "lat": -3.75600,
        "lng": 102.27650
    },

    "Tikungan_Rektorat_Fisip_1": {
    "nama": "Tikungan Jalan Rektorat ke FISIP",
    "lat": -3.75860,  
    "lng": 102.27350  
},

    "Tikungan_FKIP": {
        "nama": "Tikungan FKIP",
        "lat": -3.75650,
        "lng": 102.27760
    },

    "Tikungan_Stadion": {
        "nama": "Tikungan Stadion",
        "lat": -3.75710,
        "lng": 102.27790
    },

    "Bundaran_1": {
        "nama": "Bundaran 1",
        "lat": -3.75680,
        "lng": 102.27530
    },

    "Bundaran_2": {
        "nama": "Bundaran 2",
        "lat": -3.75660,
        "lng": 102.27550
    }
}

# =========================================================
# GRAF DIJKSTRA
# =========================================================

GRAF_UNIB = {

    "Rektorat": {
        "Simp_Rektorat_Utama": 35,
    },

    "Danau": {
        "Simp_Perpustakaan": 150
    },

    "Simp_Rektorat_Utama": {
        "Rektorat": 35,
        "Simp_Layanan_Terpadu": 100,
        "Tikungan_Rektorat_Fisip_1": 110
    },

    "Tikungan_Rektorat_Fisip_1": {
    "Simp_Rektorat_Utama": 110,
    "Simp_Selatan_Fisip": 120          
},

    "Simp_Layanan_Terpadu": {
        "Simp_Rektorat_Utama": 100,
        "Gedung_Layanan_Terpadu": 45,
        "Simp_Pertanian_Utara": 220,
        "Simp_Gedung_I": 260
    },

    "Gedung_Layanan_Terpadu": {
        "Simp_Layanan_Terpadu": 45,
        "Teknologi_Pertanian": 90
    },

    "Teknologi_Pertanian": {
        "Gedung_Layanan_Terpadu": 90,
        "Simp_Pertanian_Utara": 100
    },

    "Simp_Pertanian_Utara": {
        "Teknologi_Pertanian": 100,
        "Simp_Layanan_Terpadu": 220,
        "Simp_Mipa_Utara": 240
    },

    "Simp_Mipa_Utara": {
        "Simp_Pertanian_Utara": 240,
        "FMIPA": 60,
        "Perpustakaan": 130,
        "Simp_GB5": 160
    },

    "FMIPA": {
        "Simp_Mipa_Utara": 60
    },

    "Simp_GB5": {
        "Simp_Mipa_Utara": 160,
        "GB5": 30,
        "Tikungan_GB": 40
    },

    "GB5": {
        "Simp_GB5": 30
    },

    "Tikungan_GB": {
        "Simp_GB5": 40,
        "GB4": 40,
        "Simp_GB_Cluster": 50
    },

    "Kedokteran": {
    "Simp_Fkip_Stadion": 60
},

    "GB4": {
        "Tikungan_GB": 40,
        "GB3": 40
    },

    "GB3": {
        "GB4": 40,
        "Simp_GB_Cluster": 25
    },

    "Simp_GB_Cluster": {
        "Tikungan_GB": 50,
        "GB3": 25,
        "GB1": 50,
        "GB2": 45,
        "PKM": 30,
        "Simp_Perpustakaan": 140
    },

    "GB1": {
        "Simp_GB_Cluster": 50
    },

    "GB2": {
        "Simp_GB_Cluster": 45
    },

    "PKM": {
        "Simp_GB_Cluster": 30
    },

    "Perpustakaan": {
        "Simp_Mipa_Utara": 130,
        "Simp_Perpustakaan": 60
    },

    "Simp_Perpustakaan": {
        "Perpustakaan": 60,
        "Danau": 150,
        "Simp_GB_Cluster": 140,
        "FKIP_Dekanat": 75,
        "Simp_Selatan_Fisip": 200
    },

    "FKIP_Dekanat": {
        "Simp_Perpustakaan": 75,
        "UPA_TIK": 70,
        "GSG": 150
    },

    "UPA_TIK": {
        "FKIP_Dekanat": 70,
        "Simp_Selatan_Fisip": 85
    },

    "FISIP": {
        "Simp_Selatan_Fisip": 50
    },

    "Simp_Selatan_Fisip": {
        "FISIP": 50,
        "Tikungan_Rektorat_Fisip_1": 120,
        "Simp_Perpustakaan": 200,
        "UPA_TIK": 85,
        "Baitul_Hikmah": 95,
        "Simp_Teknik_Gsg": 140
    },

    "Baitul_Hikmah": {
        "Simp_Selatan_Fisip": 95
    },

    "Simp_Teknik_Gsg": {
        "Simp_Selatan_Fisip": 140,
        "Teknik": 40,
        "GSG": 50,
        "Tikungan_Stadion": 90
    },

    "Lab_Terpadu_Teknik": {
    "Teknik": 30
},

    "Teknik": {
        "Simp_Teknik_Gsg": 40,
        "Lab_Terpadu_Teknik": 30
    },

    "GSG": {
        "Simp_Teknik_Gsg": 50
    },

    "Tikungan_Stadion": {
        "Simp_Teknik_Gsg": 90,
        "Tikungan_FKIP": 70,
        "Stadion": 80
    },

    "Tikungan_FKIP": {
        "Tikungan_Stadion": 70,
        "Simp_Fkip_Stadion": 40
    },

    "Simp_Fkip_Stadion": {
    "Tikungan_FKIP": 40,
    "FKIP_UNIB": 40,
    "Kedokteran": 60
},

    "FKIP_UNIB": {
        "Simp_Fkip_Stadion": 40
    },

    "Stadion": {
        "Tikungan_Stadion": 80
    },

    "Simp_Gedung_I": {
        "Simp_Layanan_Terpadu": 260,
        "Gedung_I": 70,
        "Fak_Pertanian": 140
    },

    "Gedung_I": {
        "Simp_Gedung_I": 70
    },

    "Fak_Pertanian": {
        "Simp_Gedung_I": 140,
        "Hukum": 210
    },

    "Hukum": {
        "Fak_Pertanian": 210
    }
}

# =========================================================
# HALAMAN UTAMA
# =========================================================

JAM_RAMAI = {
    "Rektorat": "08:00 - 11:00",
    "Perpustakaan": "09:00 - 14:00",
    "FMIPA": "07:30 - 12:00",
    "FKIP_UNIB": "08:00 - 13:00",
    "Teknik": "10:00 - 15:00",
    "GSG": "16:00 - 18:00"
}

@app.route('/')
def index():

    gedung_clean = {
        k: v for k, v in LOKASI_UNIB.items()
        if not (
            k.startswith("Simp_")
            or k.startswith("Tikungan")
            or k.startswith("Bundaran")
        )
    }

    return render_template(
        'index.html',
        locations=gedung_clean,
        jam_ramai=JAM_RAMAI
    )


# =========================================================
# API RUTE TERPENDEK
# =========================================================

@app.route('/api/rute-terpendek')
def api_rute_terpendek():

    dari = request.args.get('start')
    ke = request.args.get('end')

    if dari not in GRAF_UNIB or ke not in GRAF_UNIB:
        return jsonify({
            "status": "error",
            "message": "Lokasi tidak valid"
        }), 400

    jalur_titik, total_jarak = hitung_dijkstra(
        GRAF_UNIB,
        dari,
        ke
    )

    if jalur_titik is None:
        return jsonify({
            "status": "error",
            "message": "Rute tidak ditemukan"
        }), 404

    koordinat_jalur = [
        [
            LOKASI_UNIB[t]["lat"],
            LOKASI_UNIB[t]["lng"]
        ]
        for t in jalur_titik
    ]

    nama_rute_user = [
        LOKASI_UNIB[t]["nama"]
        for t in jalur_titik
        if not (
            t.startswith("Simp_")
            or t.startswith("Tikungan")
            or t.startswith("Bundaran")
        )
    ]

    return jsonify({
        "status": "success",
        "rute_nama": nama_rute_user,
        "koordinat": koordinat_jalur,
        "jarak_meter": total_jarak
    })

# =========================================================
# RUN FLASK
# =========================================================

if __name__ == '__main__':
    app.run(debug=True, port=5000)