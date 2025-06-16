import matplotlib.pyplot as plt
import numpy as np
import torchaudio

def plot_specgram(data, sr):
  data = data.numpy()
  num_channels, num_frames = data.shape  
  fig, ax = plt.subplots(num_channels, 1)
  if num_channels == 1:
    ax = [ax]
  for c in range(num_channels):
    ax[c].specgram(data[c], Fs=sr)

  plt.show(block=False)

filepath = 'pitch_shifted_librosa.wav'
data ,sr = torchaudio.load(filepath)

plot_specgram(data, sr)
input()