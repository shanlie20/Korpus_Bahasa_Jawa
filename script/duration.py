from pathlib import Path
import soundfile as sf
import pandas as pd

audio_dir = Path("../audio")
records = []

for file in sorted(audio_dir.rglob("*.wav")):
    info = sf.info(file)
    duration = info.duration

    print(f"{file.name}: {duration:.2f} detik")

    records.append({
        "nama_file": file.name,
        "durasi_detik": round(duration, 2)
    })

df = pd.DataFrame(records)
df.to_csv("durasi_per_file.csv", index=False)

print(f"\nTotal file: {len(df)}")
print("Data berhasil disimpan ke durasi_per_file.csv")