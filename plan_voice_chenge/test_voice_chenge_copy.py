import librosa
import soundfile as sf

def pitch_shift_librosa(input_path, output_path, semitones):
    y, sr = librosa.load(input_path, sr=None)
    y_shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=semitones)
    sf.write(output_path, y_shifted, sr)

# 使用例
pitch_shift_librosa("レコーディング.wav", "pitch_shifted_librosa.wav", semitones=4)
