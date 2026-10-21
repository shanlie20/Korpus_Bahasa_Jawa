from pathlib import Path
import re
import soundfile as sf
import pandas as pd

audio_dir = Path("../audio")

gender_map = {
    "S01": "Laki-laki",
    "S02": "Perempuan",
    "S03": "Laki-laki",
    "S04": "Perempuan",
    "S05": "Laki-laki",
    "S06": "Perempuan",
    "S07": "Laki-laki",
    "S08": "Perempuan",
    "S09": "Laki-laki",
    "S10": "Perempuan",
}

pattern = re.compile(r"^(S\d{2})_(T\d{2})_(\d{3})\.wav$")
records = []

for file in sorted(audio_dir.rglob("*.wav")):
    match = pattern.fullmatch(file.name)
    info = sf.info(file)

    speaker = match.group(1) if match else file.parent.name
    topic = match.group(2) if match else "Tidak diketahui"

    records.append({
        "file": str(file.relative_to(audio_dir)),
        "penutur": speaker,
        "topik": topic,
        "gender": gender_map.get(speaker, "Tidak diketahui"),
        "durasi_detik": info.duration
    })

df = pd.DataFrame(records)

if df.empty:
    print("\nTidak ditemukan file WAV.")
else:
    total_duration = df["durasi_detik"].sum()

    print("\nSTATISTIK KORPUS:")
    print(f"Total waktu rekaman: {total_duration / 3600:.2f} jam")
    print(f"Jumlah penutur: {df['penutur'].nunique()}")
    print(f"Jumlah penutur laki-laki: {df[df['gender'] == 'Laki-laki']['penutur'].nunique()}")
    print(f"Jumlah penutur perempuan: {df[df['gender'] == 'Perempuan']['penutur'].nunique()}")
    print(f"Jumlah recording: {len(df)}")    
    
    print("\nDURASI PER PENUTUR:")
    by_speaker = df.groupby("penutur").agg(
        jumlah_recording=("file", "count"),
        total_durasi_detik=("durasi_detik", "sum")
    )
    by_speaker["total_durasi_menit"] = (
        by_speaker["total_durasi_detik"] / 60
    )
    print(by_speaker.round(2).to_string())
    by_speaker.round(2).to_csv("durasi_per_penutur.csv")

    print("\nDURASI PER TOPIK:")
    by_topic = df.groupby("topik").agg(
        jumlah_penutur=("penutur", "nunique"),  
        jumlah_recording=("file", "count"),
        total_durasi_detik=("durasi_detik", "sum")
    )
    by_topic["total_durasi_menit"] = (
        by_topic["total_durasi_detik"] / 60
    )
    print(by_topic.round(2).to_string())
    by_topic.round(2).to_csv("durasi_per_topik.csv")

    print("\nDURASI PER GENDER:")
    by_gender = df.groupby("gender").agg(
        jumlah_penutur=("penutur", "nunique"),
        jumlah_recording=("file", "count"),
        total_durasi_detik=("durasi_detik", "sum")
    )
    by_gender["total_durasi_menit"] = (
        by_gender["total_durasi_detik"] / 60
    )
    print(by_gender.round(2).to_string())
    by_gender.round(2).to_csv("durasi_per_gender.csv")

    print("\nFile CSV berhasil disimpan:")
    print("- durasi_per_penutur.csv")
    print("- durasi_per_topik.csv")
    print("- durasi_per_gender.csv")