from pathlib import Path
import soundfile as sf
import numpy as np
import re

audio_dir = Path("../audio")
pattern = re.compile(r"^S\d{2}_T\d{2}_\d{3}\.wav$")

issues = {
    "Sample rate tidak sesuai": [],
    "Bit depth tidak sesuai": [],
    "Channel tidak sesuai": [],
    "Clipping terindikasi": [],
    "Nama file tidak sesuai konvensi": []
}

for file in sorted(audio_dir.rglob("*.wav")):
    relative_path = str(file.relative_to(audio_dir))
    info = sf.info(file)

    if info.samplerate != 16000:
        issues["Sample rate tidak sesuai"].append(
            f"{relative_path} ({info.samplerate} Hz)"
        )

    if info.subtype != "PCM_16":
        issues["Bit depth tidak sesuai"].append(
            f"{relative_path} ({info.subtype})"
        )

    if info.channels != 1:
        issues["Channel tidak sesuai"].append(
            f"{relative_path} ({info.channels} channel)"
        )

    audio, _ = sf.read(file, dtype="int16", always_2d=True)

    if np.any((audio == 32767) | (audio == -32768)):
        issues["Clipping terindikasi"].append(relative_path)

    if not pattern.fullmatch(file.name):
        issues["Nama file tidak sesuai konvensi"].append(relative_path)

for issue, files in issues.items():
    print(f"\n{issue} ({len(files)} file):")

    if files:
        for file in files:
            print(file)
    else:
        print("Tidak ada")