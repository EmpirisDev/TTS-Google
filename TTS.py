from google.cloud import texttospeech
import os

# Spécifie le fichier d'authentification pour Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "GoogleCloudAuthKey.json"

# Spécifie le texte à synthétiser
intput = "test"

# Instantie le client TextToSpeech
client = texttospeech.TextToSpeechClient()

# Sywith open("audio/output.wav", "wb") as out:ntétise le texte
synthesis_input = texttospeech.SynthesisInput(text=intput)

# Spécifie les paramètres de la voix (ici, en français)
voice = texttospeech.VoiceSelectionParams(
    language_code="fr-FR",
    name="fr-FR-Wavenet-C",
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
)

# Spécifie le format audio de la sortie (wave ici)
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16
)

# Envoie la requête au serveur de Text-to-Speech de Google Cloud pour synthétiser la parole
response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)
filename = "output.wav"
with open(filename, "wb") as out:
    out.write(response.audio_content)