import os
import assemblyai as aai

from backend.utils import save_text_to_file


def transcribe(audio_data, question):
    aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
    transcriber = aai.Transcriber()
    config = aai.TranscriptionConfig(speaker_labels=True)

    transcript = transcriber.transcribe(audio_data, config)

    save_text_to_file("Answers_part01.txt", transcript.text, question)
