import io
import requests
import sounddevice as sd
from scipy.io.wavfile import write
import argparse


def record(seconds=3, save=False):
    sr = 32000
    print('Recording...')
    recording = sd.rec(int(seconds*sr), samplerate=sr, channels=2)
    sd.wait()
    print('...Finished')
    stream = io.BytesIO()
    write(stream, sr, recording)
    if save:
        write("recording.wav", sr, recording)
    return stream


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--recordLength', type=int, default=3)
    parser.add_argument('-s', '--save', type=bool, default=False)

    options = parser.parse_args()

    record_length = options.recordLength
    save = options.save

    url = "http://127.0.0.1:5000/"
    stream = record(record_length, save)
    print('Sending audio stream to the server, awaiting response...')
    req = requests.post(url, files={'audio': stream})
    print(req.text)


if __name__ == '__main__':
    main()
