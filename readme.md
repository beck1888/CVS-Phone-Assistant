# CVS Phone Assistant

## About
In my comp sci class I had a text based version of this project as a quiz question. I thought it would be cool to turn it into a live demo.

## Dependencies

**THIS PROJECT IS DESIGNED FOR MACOS ONLY**

This project uses multiple non-standard Python libraries including:

1. `pyttsx3`
2. `playsound`
3. `speech_recognition`

Number 1 and 2 can be easily installed by using `pip install`.

Note about number 3: in addition to installing it via pip, you will need to install `PyAudio` with Homebrew to manage the mic.

## API Keys
The speech_recognition library uses cloud server apis from Google or Microsoft. This library has a built-in api key for Google's servers by default. I believe this allows you 50 requests per day without having to configure anything.

## License
Since this project is a personal demo, I haven't been keeping tabs on this. I know that *allow.mp3* was sourced from the Apple Shortcuts software, so it may not be free use. The other two sounds were made by me in Audacity so they should have no restrictions. Some of these libraries may not be licensed under creative commons for commercial use, so double check before you use them outside of personal use cases.

Besides that, you may use the code I have written however you want.

## To-DO
- Fix error handling to not repeat irrelevant things
- Add comments for clarity
- Add sound effects for the phone being transferred
- Find a less obnoxious voice
- Implement an infinite on-hold simulator
- Support multiple ways of saying things (i.e. 'hours, 'store hours, 'the store hours, etc...)

## Known issues
I believe that there are no use cases that could break `main.py`, but please let me know if you spot any (or open an issue).

Previously, some text was too heavily sanitized which broke it, but that should be fixed.