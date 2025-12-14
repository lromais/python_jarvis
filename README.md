

```
sudo apt install portaudio19-dev ffmpeg espeak-ng sox -y
sudo apt install python3-pyaudio
sudo apt update
sudo apt install -y wget unzip sox libstdc++6
wget https://github.com/rhasspy/piper/releases/download/2023.11.14-2/piper_linux_x86_64.tar.gz
tar -xzvf piper_linux_x86_64.tar.gz 
sudo mv piper /usr/local/bin/
mkdir -p ~/piper/voices
cd ~/piper/voices
cd ~/piper/voices
wget https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/pt_BR/faber/medium/pt_BR-faber-medium.onnx
wget https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/pt_BR/faber/medium/pt_BR-faber-medium.onnx.json
cd /usr/local/bin/
mv piper bin_piper
sudo ln -s /usr/local/bin/bin_piper/piper /usr/local/bin/piper
sudo chmod +x /usr/local/bin/piper
```# python_jarvis
# python_jarvis
# python_jarvis
# python_jarvis
# python_jarvis
# python_jarvis
