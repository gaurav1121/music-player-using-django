import eyed3

audio_file = eyed3.load(r"C:\Users\gaura\Desktop\database songs\03 Oonchi Hai Building 2.0 - Judwaa 2 - 320Kbps.mp3")
print(audio_file.tag.album)