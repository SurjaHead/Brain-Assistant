<div align="center">
<h1 align="center">Brain Assistant</h1>

  <p align="center">
    Analyzes EEG data to trigger audio responses based on brain wave activity.
  </p>
</div>

## Table of Contents

  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#key-features">Key Features</a></li>
      </ul>
    </li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>

## About The Project

This project uses BrainFlow to capture and analyze EEG data, focusing on alpha and beta wave bands. It processes the data with filters and triggers audio feedback based on the measured brain wave activity.  The application initializes a connection to an EEG board, captures brain wave data for 10 seconds, applies detrending, calculates power spectral density using Welch's method, applies bandstop and bandpass filters, calculates power in the alpha and beta bands, and provides audio feedback based on the measured values.

### Key Features

- **Real-time EEG data collection:** Uses BrainFlow to capture EEG data from a connected device.
- **Signal Processing:** Applies bandpass and bandstop filters to clean and isolate relevant frequency bands.
- **Power Spectrum Density Analysis:** Calculates power spectrum density using Welch's method.
- **Alpha and Beta Wave Analysis:** Calculates power in the alpha (7-13 Hz) and beta (14-30 Hz) bands.
- **Audio Feedback:** Provides audio feedback using pyttsx3 based on alpha and beta power levels.

## Built With

- Python
- BrainFlow
- NumPy
- pyttsx3

## Getting Started

To get started with this project, you need to install the required libraries and connect a compatible EEG device.

### Prerequisites

- Python
- BrainFlow:
  ```sh
  pip install brainflow
  ```
- NumPy:
  ```sh
  pip install numpy
  ```
- pyttsx3:
  ```sh
  pip install pyttsx3
  ```

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/surjahead/brain-assistant.git
   ```
2. Navigate to the project directory:
   ```sh
   cd brain-assistant
   ```
3. Connect your EEG device (configured for COM5 by default, can be changed in `main.py`).
4. Run the script:
   ```sh
   python main.py
   ```

## Acknowledgments

- This project was created using the OpenBCI Ganglion Board and the BrainFlow documentation.
