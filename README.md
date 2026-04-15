# Voice Transformer

A Python-based project for exploring and applying voice transformation effects.

## Project Structure

This project contains two primary components for voice manipulation:

1. **`VoiceTransformer.ipynb` (Offline Processing)**
   * A comprehensive Jupyter Notebook exploring various DSP (Digital Signal Processing) techniques.
   * Includes implementations or analyses using:
     * **Granular Synthesis** (`gsplot.jpg`, `burst.wav`)
     * **Linear Predictive Coding (LPC)** (`lpc.jpg`)
     * **Pitch Shifting** (`pitchshift.jpg`)
     * General voice changing logic.
   * Processes pre-recorded offline audio files (like `ndambia.wav`, `voiced.wav`).

2. **`realtime.ipynb` (Real-Time Processing)**
   * A live, low-latency version of the voice transformer leveraging the `pyaudio` and `numpy` libraries. 
   * Captures your microphone, processes the audio chunk-by-chunk in real-time, and outputs it to your speakers.
   * Built-in effects include:
     * `robot`: Amplitude modulation for a robotic voice.
     * `pitch_shift_up`: Simple pitch shifting up.
     * `pitch_shift_down`: Simple pitch shifting down.
   
## Setup & Installation

Ensure you are running a modern version of Python (3.7+ recommended). 

To install the required dependencies, run:
```bash
pip install numpy scipy pyaudio sounddevice matplotlib
```

*(Note: Depending on your OS, `pyaudio` may require additional binaries like PyAudio wheels for Windows or PortAudio for macOS/Linux).*

## Usage

### Real-Time Voice Transformation
1. Open up `realtime.ipynb` in VS Code or Jupyter.
2. Select your desired effect by modifying the `TRANSFORM_TYPE` variable (e.g., `TRANSFORM_TYPE = 'robot'`).
3. Run the cells sequentially. Ensure your Windows Microphone Privacy Settings allow Python/VS Code to access your microphone.
4. Speak into your microphone and hear the transformed audio live!
5. To stop, interrupt the Jupyter Kernel.

### Offline Analysis
1. Open `VoiceTransformer.ipynb`.
2. Run the notebook to see the visualizations, listen to the processed wav files, and explore the advanced theories behind Granular Synthesis and LPC.

## Troubleshooting
- **No audio devices found (PyAudio/sounddevice)**: Check your OS-level microphone privacy settings to ensure the environment has permission to use the microphone. If using WSL, you may need a workaround for audio pass-through.
- **PortAudio missing errors**: Make sure `pyaudio` installed successfully. On Windows, simply running `pip install pyaudio` usually suffices as it bundles pre-built C wheels.
