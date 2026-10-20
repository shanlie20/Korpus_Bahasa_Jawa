# Tugas Besar Fase 1 IF4071 Pemrosesan Ucapan
## Pengumpulan Korpus Suara Bahasa Daerah Indonesia (Bahasa Jawa)

Kelompok 7
| Nama | NIM |
|------|-----|
| Muhammad Alfansya | 13523005 |
| Shannon Aurellius Anastasya Lie | 13523019 |
| Dzaky Aurelia Fawwaz | 13523065 |
| Ferdin Arsenarendra Purtadi | 13523117 |
| Naomi Risaka Sitorus | 13523122 |

## Deskripsi
Korpus *spontaneous speech* bahasa Jawa dari 10 penutur, dikumpulkan untuk Tugas Besar Fase 1 Pemrosesan Ucapan 2206. Korpus ini disiapkan sebagai data untuk pengembangan *Automatic Speech Recognition* (ASR) bahasa Jawa pada fase berikutnya.

## Struktur Folder
```
Korpus_Bahasa_Jawa/
├── audio/
│   ├── S01/ ... S10/          # rekaman WAV per penutur
├── metadata/
│   └── metadata.csv
├── annotation/
│   └── annotation.csv
├── consent/
│   └── consent_form/          # template
└── documentation/
   └── README.md
```

## Penamaan File
 
Format: `S{ID penutur}_T{ID topik}_{nomor urut}.wav`
 
Contoh: `S03_T02_001.wav` berarti penutur S03, topik T02, rekaman ke-1.
 
## Daftar Topik
 
| Kode | Topik |
|---|---|
| T01 | Aktivitas Sehari-hari |
| T02 | Hobi dan Waktu Luang |
| T03 | Makanan |
| T04 | Perjalanan |
| T05 | Permainan Masa Kecil |
| T06 | Pendidikan/Pekerjaan dan Rencana ke Depan |
| T07 | Cuaca dan Musim |
 
Setiap topik punya 5 pertanyaan pemicu dalam bahasa Jawa. Penutur menjawab dengan bahasanya sendiri tanpa naskah.
 
## Metadata
 
`metadata/metadata.csv` berisi satu baris per file rekaman.
 
| Kolom | Isi |
|---|---|
| File | Nama file WAV |
| Speaker | Speaker ID (S01–S10) |
| Gender | M / F |
| Language/Dialect | Dialek penutur (Surakarta-Yogyakarta, Ngapak, Jawa Timur, atau tidak yakin) |
| Topic | Kode topik (T01–T07) |
| Duration | Durasi file dalam detik |
| Environment | Indoor |
| Quality | Good / Acceptable / Reject |
 
Kelompok juga mencatat umur, frekuensi pemakaian bahasa Jawa, dan tingkat kelancaran tiap penutur dari formulir penutur. Formulir tidak menanyakan daerah asal, untuk mengurangi risiko orang mengenali penutur.
 
## Anotasi
 
`annotation/annotation.csv` berisi satu baris per segmen ujaran.
 
| Kolom | Isi |
|---|---|
| File, Seg | Nama file dan nomor segmen urut |
| Start, End | Batas segmen dalam detik |
| Transcript | Transkripsi apa adanya, huruf kecil, tanda baca minimal |
| Speaker | Speaker ID penjawab |
| Language/Dialect | Jawa-Ngoko, Jawa-Krama, Jawa-Campur, Jawa-Indonesia |
| Topic | Kode topik |
| Event | none, noise, overlap, laughter, breath, other |
| Catatan, Status | Catatan anotator dan status (Draft, Review, Final) |
 
Aturan segmentasi:
- Satu segmen berisi satu ujaran (utterance) yang utuh.
- Satu ujaran berdurasi 3–15 detik.
- Anotator memotong segmen saat penutur berhenti atau mengambil napas untuk melanjutkan bicara, yaitu saat waveform menunjukkan jeda yang jelas.
- Diam lebih dari 1 detik. Bagian diam yang lebih dari 1 detik dibuang dan tidak masuk segmen mana pun. Aturan ini berlaku untuk diam di tengah rekaman, di awal, dan di akhir.
- Diam kurang dari 1 detik. Bagian diam yang kurang dari 1 detik dibagi dua: separuh masuk ke segmen sebelumnya dan separuh masuk ke segmen sesudahnya.
- Segmen tidak harus bersambung. Tidak semua bagian rekaman menjadi segmen. End suatu segmen tidak harus sama dengan Start segmen berikutnya (misalnya Seg 1 berakhir di 0,57 detik dan Seg 2 mulai di 0,57 detik tidak diwajibkan).
 
## Proses Pengumpulan
 
1. **Persiapan.** Penutur mengisi formulir dan menandatangani informed consent. Operator menyiapkan perangkat, memeriksa level, dan melakukan test recording.
2. **Rekaman.** Operator menyalakan rekaman lebih dulu, penutur mulai bicara sekitar detik ketiga, dan operator menghentikan rekaman sekitar 3 detik setelah penutur selesai.
3. **Konversi dan QC.** Rekaman dikonversi ke 16 kHz mono 16-bit bila perlu. Anggota memeriksa kejelasan suara, clipping, noise, suara lain, dan keutuhan rekaman, lalu memberi label Good, Acceptable, atau Reject. File Reject direkam ulang bila memungkinkan.
4. **Anotasi dan review.** Anotator mentranskripsi dan memberi label, lalu anggota lain meninjau dan memperbaiki sebelum versi final.

## Etika dan Privasi
 
- Semua penutur berusia 18 tahun ke atas dan menandatangani informed consent sebelum rekaman.
- Penutur dicatat dengan Speaker ID. Nama asli dan data identitas lain disimpan di luar repositori.
- Folder `consent/` hanya memuat template kosong.
- Topik tidak menyasar data sensitif seperti kesehatan, agama, politik, dan identitas pribadi. Topik Perkenalan sengaja tidak dipakai.
- Penutur diminta tidak menyebut nama asli orang lain di dalam rekaman
.
## Keterbatasan
- Penutur sebagian besar mahasiswa dengan rentang usia 19–22, sehingga variasi usia dan latar belakang terbatas.
- Dialek dilabeli dari pilihan penutur dan diperiksa lewat pendengaran saat QC.
- Formulir tidak menanyakan bahasa ibu. Status penutur asli dinilai dari frekuensi pemakaian dan tingkat kelancaran.
- Korpus berukuran kecil (10 penutur) dan cocok untuk eksplorasi, bukan untuk melatih model skala besar.

## Pembagian Kerja
 
| NIM | Peran | Tugas utama |
|---|---|---|
| 13523019 | Koordinator | Timeline, repositori, dokumen desain, README, laporan akhir |
| 13523005 | Recording | SOP rekaman, test recording, koordinasi file audio WAV |
| 13523065 | Recording | Daftar topik dan pertanyaan pemicu, jadwal dan data penutur |
| 13523122 | Metadata dan teknis | `metadata.csv`, formulir penutur, consent, skrip pengecekan format, QC teknis |
| 13523117 | QC dan anotasi | Pedoman anotasi, checklist QC, review akhir transkrip, `annotation.csv` final |
 
13523122 bukan penutur bahasa Jawa, sehingga tidak ikut mentranskripsi penutur narasumbernya dan fokus pada metadata dan pengecekan teknis.
 
## Penggunaan
Korpus ini dibuat untuk keperluan tugas kuliah dan penelitian ASR. Mohon tidak menyebarkan ulang atau mencoba mengidentifikasi penutur tanpa izin.
