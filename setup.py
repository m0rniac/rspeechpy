from setuptools import setup, find_packages

readme = open('./README.md', 'r')

setup(
    name='rspeechpy',
    packages=find_packages(),
    version='0.1',
    description="Realist Text To Speech Python Package",
    long_description=readme.read(),
    author="m0rniac",
    author_email="christ.castr@proton.me",
    url='https://github.com/m0rniac/rspeechpy',
    download_url='https://github.com/m0rniac/rspeechpy/tarball/0.1',
    keywords=["tts", "text to speech", "python tts", "realist tts", "realistic python tts", 'azure tts', 'azure'],
    data_files=[('rspeechpy', ['rspeechpy/voices_list.json', 'rspeechpy/voices_list_plus.json'])],
    install_requires=[
        'aiofiles',
        'aiohttp',
        'click'
    ],
)

