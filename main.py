from datetime import datetime
import pyttsx3

import argparse
import time
import brainflow
import numpy as np

from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes, AggOperations, WindowFunctions, DetrendOperations


def main():
    BoardShim.enable_dev_board_logger()

    # use synthetic board for demo
    BoardShim.enable_dev_board_logger()
    params = BrainFlowInputParams()
    params.board_id = 1
    board_id = 1
    params.serial_port = 'COM5'
    board = BoardShim(board_id, params)
    eeg_channels = BoardShim.get_eeg_channels(board_id)
    sampling_rate = BoardShim.get_sampling_rate(board_id)
    timestamp = BoardShim.get_timestamp_channel(board_id)
    board.prepare_session()
    board.start_stream()
    BoardShim.log_message(LogLevels.LEVEL_INFO.value, 'start sleeping in the main thread')
    time.sleep(10)
    nfft = DataFilter.get_nearest_power_of_two(sampling_rate)
    data = board.get_board_data()
    board.stop_stream()
    board.release_session()

    eeg_channels = BoardShim.get_eeg_channels(board_id)
    # second eeg channel of synthetic board is a sine wave at 10Hz, should see huge alpha
    eeg_channel = eeg_channels[1]
    # optional detrend
    DataFilter.detrend(data[eeg_channel], DetrendOperations.LINEAR.value)
    psd = DataFilter.get_psd_welch(data[eeg_channel], nfft, nfft // 2, sampling_rate,
                                   WindowFunctions.BLACKMAN_HARRIS.value)

    for count, channel in enumerate(eeg_channels):
        if count == 0:
            DataFilter.perform_bandstop(data[channel], sampling_rate, 60.0, 4.0, 4,
                                            FilterTypes.BUTTERWORTH.value, 0)  # bandstop 58 - 62
            DataFilter.perform_bandpass(data[channel], sampling_rate, 21.0, 20.0, 4,
                                            FilterTypes.BESSEL.value, 0)  # bandpass 11 - 31
        if count == 1:
            DataFilter.perform_bandstop(data[channel], sampling_rate, 60.0, 4.0, 4,
                                            FilterTypes.BUTTERWORTH.value, 0)  # bandstop 58 - 62
            DataFilter.perform_bandpass(data[channel], sampling_rate, 21.0, 20.0, 4,
                                            FilterTypes.BESSEL.value, 0)  # bandpass 11 - 31
        if count == 2:
            DataFilter.perform_bandstop(data[channel], sampling_rate, 60.0, 4.0, 4,
                                            FilterTypes.BUTTERWORTH.value, 0)  # bandstop 58 - 62
            DataFilter.perform_bandpass(data[channel], sampling_rate, 21.0, 20.0, 4,
                                            FilterTypes.BESSEL.value, 0)  # bandpass 11 - 31
        if count == 3:
            DataFilter.perform_bandstop(data[channel], sampling_rate, 60.0, 4.0, 4,
                                            FilterTypes.BUTTERWORTH.value, 0)  # bandstop 58 - 62
            DataFilter.perform_bandpass(data[channel], sampling_rate, 21.0, 20.0, 4,
                                            FilterTypes.BESSEL.value, 0)  # bandpass 11 - 31

    band_power_alpha = DataFilter.get_band_power(psd, 7.0, 13.0)
    band_power_beta = DataFilter.get_band_power(psd, 14.0, 30.0)
    print("alpha/beta:%f", band_power_alpha / band_power_beta)

    print(band_power_alpha)
    print(band_power_beta)
    now = datetime.now().date() # time object
    now1 = datetime.now().time()
    engine = pyttsx3.init()
    

    if band_power_alpha < 10:
        engine.say(now)
        engine.runAndWait()

    if band_power_beta > 5:
        engine.say(now1)
        engine.runAndWait()
    


    # fail test if ratio is not smth we expect
    if (band_power_alpha / band_power_beta < 1):
        raise ValueError('Wrong Ratio')


if __name__ == "__main__":
    main()


#now = datetime.now().date() # time object
#engine = pyttsx3.init()
#engine.say(now)
