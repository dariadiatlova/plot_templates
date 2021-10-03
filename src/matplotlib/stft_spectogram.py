import matplotlib.pyplot as plt
from librosa.display import specshow


def plot_histogram(magnitude_spectrum, hop_length, sr: int = 16_000):
    """
    Function takes magnitude_spectrum as input of shape n_frequency_bins x n_frames
    and displays the time-frequency spectrogram across the bins.
    :param magnitude_spectrum: np.array[np.float32], to get magnitude_spectrum from digital signal – implement
    stft transform and compute the magnitude (take a power of 2 from abs of stft output).
    :param hop_length: int, the size of overlapping windows while computing stft.
    :param sr: int, sample rate – default is 16_000 for human speech processing.
    :return: None
    """
    plt.figure(25, 10)
    specshow(magnitude_spectrum, sr=sr, hop_length=hop_length, x_axis="time", y_axis="linear")
    plt.colorbar()
