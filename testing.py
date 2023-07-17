import asyncio
from rspeechpy import Engine

# Declaration
speech = Engine()

async def example():
    """ Look all avaible voices """
    #names = await speech.giveVoicesList()
    #for name in names:
    #    print(name['FriendlyName'])     # Describe voice's name & language.
    #    print(name['ShortName'])       # Return "key" to use that voice.
    
    """ Settings to build a synth of realist voice """
    await speech.setVoice('es-ES-ElviraNeural')
    
    await speech.setRate(5)
    await speech.setPitch(5)
    await speech.setVolume(5)
    
    text = "Hola esto es una prueba de texto a voz"
    await speech.synthesize(text, 'audio.mp3')

# Running
app = asyncio.get_event_loop()
app.run_until_complete(example())