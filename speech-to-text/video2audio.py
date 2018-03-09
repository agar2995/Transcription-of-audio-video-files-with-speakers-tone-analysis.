import moviepy.editor as mp
import os

file1 = "afterhours.wav"


def videoToAudio(sample_file) :
  name = os.path.splitext(sample_file)
  if name[1]==".mp4":
    clip = mp.VideoFileClip(sample_file).subclip(0,50)
    audio_file = name[0]+".wav"
    clip.audio.write_audiofile(audio_file)
    return audio_file

  else:
    return sample_file

videoToAudio(file1)