import os
import wave
import numpy as np

def generate_fourier_wave(num_terms, num_samples, amplitude=1.0):
    t = np.linspace(0, 1, num_samples)
    waveform = np.zeros(num_samples)
    for i in range(1, num_terms + 1):
        frequency = np.random.uniform(1, 10)
        phase = np.random.uniform(0, np.pi * 2)
        coef = np.random.uniform(0.1, 1.0)
        waveform += coef * np.sin(2 * np.pi * frequency * t + phase)
    return amplitude * waveform / np.max(np.abs(waveform))

# Create a new folder for the generated CV wave files
output_folder = 'random_cv_wave_files_fourier'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define properties
sample_rate = 96000  # 96kHz
num_channels = 1  # Mono
num_samples = 96793  # Length
scale_factor = int(5 * (2 ** 31 - 1) / 5.0)

# Generate 10 random CV wave files using Fourier series
for i in range(100):
    random_waveform = generate_fourier_wave(5, num_samples)
    random_waveform = np.int32(random_waveform * scale_factor)

    output_path = os.path.join(output_folder, f'fourier_cv_{i+1}.wav')
    with wave.open(output_path, 'wb') as wav_file:
        wav_file.setnchannels(num_channels)
        wav_file.setsampwidth(4)  # 4 bytes for int32
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(random_waveform.tobytes())
