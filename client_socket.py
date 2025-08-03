import socket
import io
import argparse
import sounddevice as sd
from scipy.io.wavfile import write


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

    host = 'localhost'
    port = 8080
    buffer_size = 1024

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        stream = record(record_length, save)
        s.sendfile(stream)
        s.shutdown(socket.SHUT_WR)
        data = s.recv(buffer_size)

    print('Transcript: ', data.decode())


if __name__ == '__main__':
    main()
