"""
MIT License

Copyright (c) [2023] [@m0rniac]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import uuid
import click
import asyncio
from . import Engine, Engine_dir, EngineError

# Definition of the asynchronous main function
async def runMain(voice_name, text, filename, rate, pitch, volume):
    speech = Engine()
    v = await speech.get_voices_by_substring(voice_name)  # Get voices that match the given substring
    if not v:
        raise EngineError("The voice was not found.")
    await speech.setVoice(v[0]['Name'])  # Set the voice to be used
    await speech.setRate(rate)  # Set the speech rate
    await speech.setPitch(pitch)  # Set the voice pitch
    await speech.setVolume(volume)  # Set the voice volume
    await speech.synthesize(text.strip(), filename)  # Synthesize the speech and save it to a file

# Definition of the main function
@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.argument("voice_name")  # Command-line argument for the voice name
@click.argument("text")  # Command-line argument for the text to synthesize
@click.option("--filename", default='audio_'+str(uuid.uuid4())+'.mp3', help="Audio file name.")  # Optional command-line option for the audio file name
@click.option("--rate", default=0, help="Speech rate (from 1 to 100, or 0).")  # Optional command-line option for the speech rate
@click.option("--pitch", default=0, help="Voice pitch (from 1 to 100, or 0).")  # Optional command-line option for the voice pitch
@click.option("--volume", default=1.0, help="Voice volume (from 1.0 to 10.0).")  # Optional command-line option for the voice volume
def main(voice_name, text, filename='audio_'+str(uuid.uuid4())+'.mp3', rate=0, pitch=0, volume=1.0):
    try:
        loop = asyncio.get_event_loop()  # Get the event loop
        click.echo(loop.run_until_complete(runMain(voice_name, text, filename, rate, pitch, volume)))  # Run the asynchronous main function and print the result
    except EngineError as exn:
        click.secho(str(exn), fg='red')  # Print the exception message in red
        raise SystemExit(-2)  # Exit the program with a specific error code

# Definition of the update_voices function
@click.command()
def update_voices():
    removed = False
    for f in ["voices_list.json", "voices_list_plus.json"]:
        p = os.path.join(Engine_dir, f)  # Get the file path
        if os.path.isfile(p):  # Check if the file exists
            removed = True
            click.echo(f"removing {p}")  # Print a message indicating that the file is being removed
            os.remove(p)  # Remove the file
    if not removed:
        click.echo("Files not found")  # Print a message indicating that the files were not found
    speech = Engine()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(speech.get_voices_list())  # Get the list of available voices

if __name__ == '__main__':
    import sys
    if sys.argv[-1].replace("-", "_").lower() == "update_voices":
        update_voices()  # Call the update_voices function if the last command-line argument is "update_voices"
        sys.exit(0)  # Exit the program with a success status code
    main()  # Call the main function
