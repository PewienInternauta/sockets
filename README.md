# Computer-Networks

### Dependancies:
 - *Assembly AI* - SDK used for speech recognition (pip install assemblyai)
 - *sounddevice* - module used for audio recording (pip install sounddevice)
 - *scipy* - library used for writing .wav files (pip install scipy)
 - **only for flask-version** - *flask* - web framework (pip install flask)
 - **only for flask-version** - *requests* - library used to send POST requests (pip install requests)

### How to run it:

First of all, the Assembly AI API requires the use of a key to access its services. Luckily the process of creating one is free. To do so one must navigate to their website found here: https://www.assemblyai.com/ \
Then create an account, by clicking "Get Started" and filling your credentials. Afterward, the API key can be found in the account tab below your e-mail. When you have the key, you have to paste it in the app.py file as the value for "api.settings.api_key". Then it's just the case of running both files starting from the app.py.

### Optional arguments:
To run the script with custom settings, one must run it from the terminal with the command "python client_socket.py" and supplying argument values after given flags:
- '-l' - length of the recording in seconds if none given deafults to 3
- '-s' - save flag if set to true will create "recording.wav", defaults to false

## How it works:
Client using sounddevice module records microphone input to a NumPy array, and using the scipy.io.wavfile.write() function writes to a bytes stream. The stream is send to the server using an HTTP POST.
There it gets saved to a file (it is needed because the API only accepts a path to the audio recording, and the file gets deleted shortly after the request). After the transcription is finished, the server serving as a middle-man, puts the transcription as the payload of the response to the client. There it is displayed to the user.
