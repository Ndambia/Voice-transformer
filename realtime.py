import sounddevice as sd
import numpy as np

SAMPLE_RATE = 32000
BLOCK_SIZE = 4048
CHANNELS = 2
TRANSFORM_TYPE = 'pitch_shift_up'

def process_audio(indata, outdata, frames, time, status):
    if status:
        print(status)

    audio_chunk = indata[:, 0].astype(np.float32)
    x = np.arange(frames)

    if TRANSFORM_TYPE == 'robot':
        t = np.arange(frames) / SAMPLE_RATE
        modulator = 0.5 * (1 + np.sin(2 * np.pi * 50 * t))
        processed = audio_chunk * modulator

    elif TRANSFORM_TYPE == 'pitch_shift_down':
        factor = 0.75
        src_idx = np.arange(frames) * factor
        src_idx = np.clip(src_idx, 0, frames - 1)
        processed = np.interp(src_idx, x, audio_chunk)

    elif TRANSFORM_TYPE == 'pitch_shift_up':
        factor = 1.5
        src_idx = np.arange(frames) * factor
        src_idx = np.clip(src_idx, 0, frames - 1)
        processed = np.interp(src_idx, x, audio_chunk)

    else:
        processed = audio_chunk

    processed = np.clip(processed, -1.0, 1.0).astype(np.float32)
    outdata[:, 0] = processed

print(f"Starting real-time Voice Transformer with effect: {TRANSFORM_TYPE}")
print("Press Ctrl+C to stop.")

try:
    with sd.Stream(
        samplerate=SAMPLE_RATE,
        blocksize=BLOCK_SIZE,
        channels=CHANNELS,
        dtype='float32',
        callback=process_audio
    ):
        while True:
            sd.sleep(100)

except KeyboardInterrupt:
    print("\nStream stopped.")
except Exception as e:
    print("\nError:", e)