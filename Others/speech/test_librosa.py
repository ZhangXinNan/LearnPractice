
import numpy as np
import librosa


file_wav = 'en.wav'

data, fs = librosa.load(file_wav, sr=None)
print(type(data), data.dtype, data.shape)
print(type(fs), fs)


