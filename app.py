import json
import os

from flask import request
from flask import Flask
import assemblyai as api

app = Flask(__name__)

api.settings.api_key = API_KEY

transcriber = api.Transcriber()


@app.get('/')
def prompt():
    return "POST audio files here"


@app.post('/')
def transcribe():
    file = request.files['audio']
    client = str(request.remote_addr)
    print('received file from: ' + client + '; awaiting transcription')
    file.save('received.wav')
    transcription = transcriber.transcribe('received.wav')
    os.remove('received.wav')
    print('transcription complete, sending to ' + client )
    return json.dumps(transcription.text)


if __name__ == '__main__':
    app.run()

