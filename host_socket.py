import socket
import os
import assemblyai as api


def main():
    api.settings.api_key = API_KEY

    transcriber = api.Transcriber()

    host = 'localhost'
    port = 8080
    buffer_size = 1024

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        print('Live as ', (host, port))
        while True:
            s.listen()
            conn, addr = s.accept()
            with conn:
                with open('recording.wav', 'wb') as file:
                    print('Connected with', addr)
                    while True:
                        data = conn.recv(buffer_size)
                        file.write(data)
                        if not data:
                            break
                print('Recording obtained, awaiting transcription...')
                transcription = transcriber.transcribe('recording.wav')
                os.remove('recording.wav')
                print('Transcription obtained, sending transcription...')
                conn.sendall(str.encode(transcription.text))


if __name__ == '__main__':
    main()

