
# PSpeechPy

A Text To Speech engine with realistic voices developed entirely in Python and powered by Microsoft Azure as Python Package

### Based:

- [SNARF's Engine](https://github.com/m0rniac/snarf)


## Installation (Python 3.X+)
- Linux:
```bash
pip3 install rspeechpy
```
- Windows:
```bash
pip install rspeechpy
```
### Usage & Examples (Scripts)

- List all avaible voices:
```python
import asyncio
from rspeechpy import Engine

# Declaration
speech = Engine()

async def example():
    names = await speech.giveVoicesList()
    for name in names:
        print(name['FriendlyName'])     # Describe voice's name & language.
        print(name['ShortName'])       # Return "key" to use that voice.

# Running
app = asyncio.get_event_loop()
app.run_until_complete(example())
```

- Create a synthesize from text (Generate .mp3 audio):
```python
import asyncio
from rspeechpy import Engine

# Declaration
speech = Engine()

async def example():
    await speech.setVoice('es-ES-ElviraNeural')
    
    await speech.setRate(5)
    await speech.setPitch(5)
    await speech.setVolume(5)
    
    text = "Hola esto es una prueba de texto a voz"
    await speech.synthesize(text, 'audio.mp3')

# Running
app = asyncio.get_event_loop()
app.run_until_complete(example())
```



## API Reference

#### from Microsoft Azure:

[More documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=stt#text-to-speech)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | *Non-Required* |



## License:

[MIT License](https://choosealicense.com/licenses/mit/)


#### 🔗 Sponsoring:
[![portfolio](https://img.shields.io/badge/buy_me_a_coffee-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.paypal.com/paypalme/christcastr/)