import numpy as np
from scipy.signal import resample
from pydub.utils import get_array_type
from pydub import AudioSegment

def pitch_shift(audio, semitones):
    # AudioSegmentをNumPy配列に変換
    samples = np.array(audio.get_array_of_samples())
    
    # モノラルでない場合は変換
    if audio.channels > 1:
        samples = samples.reshape((-1, audio.channels))
    
    # ピッチシフトの計算
    factor = 2 ** (semitones / 12)
    new_length = int(len(samples) / factor)
    
    # リサンプリング
    new_samples = resample(samples, new_length)
    
    # 新しいAudioSegmentの作成
    new_audio = audio._spawn(new_samples.astype(get_array_type(audio.sample_width*8)))

    return new_audio.set_frame_rate(int(audio.frame_rate * factor))

# 使用例
audio = AudioSegment.from_wav("a-2.wav")
shifted_audio = pitch_shift(audio, 4)  # 4半音上げる
shifted_audio.export("pitch_shifted.wav", format="wav")
