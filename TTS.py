from google.cloud import texttospeech
import os

# Spécifie le fichier d'authentification pour Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "GoogleCloudAuthKey.json"

# Instantie le client TextToSpeech
client = texttospeech.TextToSpeechClient()

# Spécifie le texte à synthétiser
synthesis_input = texttospeech.SynthesisInput(text="Ta grosse mère ?")

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

# Le contenu audio de la réponse est binaire, donc on l'écrit dans un fichier "output.wav"
with open("output.wav", "wb") as out:
    out.write(response.audio_content)
    print('Le contenu audio a été écrit dans le fichier "output.wav"')
