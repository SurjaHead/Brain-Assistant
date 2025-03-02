# Brain Assistant

## Overview

This project uses BrainFlow to analyze brain wave data, specifically focusing on alpha and beta wave bands. It captures EEG data, processes it through various filters, and can trigger audio responses based on the measured brain wave activity.

## Features

- Real-time EEG data collection using BrainFlow
- Signal processing with bandpass and bandstop filters
- Power spectrum density analysis using Welch's method
- Alpha and beta wave band power calculation
- Audio feedback based on brain wave activity using pyttsx3

## Requirements

Python

- BrainFlow
- NumPy
- pyttsx3
- Compatible EEG device (currently configured for board_id 1)

## Installation

```
pip install brainflow numpy pyttsx3
```

## Usage

1. Connect your EEG device (configured for COM5 by default) 2. Run the script:

```
python brain_wave_analyzer.py
```

3. The program will:
   - Collect 10 seconds of EEG data
   - Process the signals with appropriate filters
   - Calculate alpha and beta band powers
   - Speak the current date if alpha power is below 10
   - Speak the current time if beta power is above 5
   - Validate the alpha/beta ratio

## How It Works

[5]The application:

1. Initializes a connection to the EEG board
2. Captures brain wave data for 10 seconds
3. Applies detrending to the EEG signal
4. Calculates power spectral density using Welch's method
5. Applies specific filters to each EEG channel:
   - Bandstop filter (58-62 Hz) to remove power line noise
   - Bandpass filter (11-31 Hz) to focus on relevant frequencies
6. Calculates power in the alpha (7-13 Hz) and beta (14-30 Hz) bands
7. Provides audio feedback based on the measured values

## Learn More

For more information about this project, check out my article: [Link to your article]

## Customization

[6]You can modify the following parameters in the code:

- Board ID and serial port
- Filtering parameters
- Alpha and beta thresholds for audio feedback
- Audio response content
