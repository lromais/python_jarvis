import speech_recognition as sr
import requests
import pyttsx3
import json
import subprocess
import tempfile
import os
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"  # ou mistral, phi, etc.

# Inicializa o TTS
engine = pyttsx3.init()
engine.setProperty("rate", 180)
PIPER_MODEL = "/home/linkoln/piper/voices/pt_BR-faber-medium.onnx"

def falar(texto):
    print("🗣 Resposta:", texto)

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav_path = f.name

    comando = [
        "piper",
        "--model", PIPER_MODEL,
        "--output_file", wav_path
    ]

    try:
        proc = subprocess.Popen(comando, stdin=subprocess.PIPE)
        proc.stdin.write(texto.encode("utf-8"))
        proc.stdin.close()
        proc.wait()

        subprocess.run(["aplay", wav_path], check=True)

    except Exception as e:
        print("❌ Erro ao falar com Piper:", e)

    finally:
        if os.path.exists(wav_path):
            os.remove(wav_path)


def ouvir():
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.dynamic_energy_threshold = True

    # USA O PULSE (índice 13) — microfone certo
    with sr.Microphone(device_index=13) as source:
        print("🎤 Fale agora...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=10, phrase_time_limit=15)

    try:
        texto = r.recognize_google(audio, language="pt-BR")
        print("🧑 Você disse:", texto)
        return texto
    except sr.UnknownValueError:
        print("❌ Não entendi o áudio.")
        return None
    except sr.RequestError as e:
        print("❌ Erro no reconhecimento:", e)
        return None


def perguntar_ollama(pergunta):
    payload = {
        "model": MODEL,
        "prompt": pergunta,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "Erro ao se comunicar com o Ollama."

def main():
    falar("Assistente iniciado. Pode falar comigo.")

    while True:
        texto = ouvir()

        if texto is None:
            falar("Não entendi. Repita por favor.")
            continue

        if "sair" in texto.lower() or "encerrar" in texto.lower():
            falar("Encerrando o assistente. Até mais!")
            break

        resposta = perguntar_ollama(texto)
        falar(resposta)

if __name__ == "__main__":
    main()

