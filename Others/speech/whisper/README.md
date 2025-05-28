
https://github.com/openai/whisper



whisper audio.flac audio.mp3 audio.wav --model turbo

conda create -n py39_whisper python=3.9
conda activate py39_whisper
pip install -U openai-whisper
whisper --language en --model medium.en --task translate TheHistoryOfTheMobilePhone.mp3


