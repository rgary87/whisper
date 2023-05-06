# Whisper

## Requirements
- Python v3.10.6 (along with virtualenv, pip, wheel, etc..)
- CUDA toolkit 11.8
- ffmpeg ([installation guide](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/))

## Run
In powershell: 
```powershell
PS C:\Users\username> git clone https://github.com/rgary87/whisper.git rgary_whisper
PS C:\Users\username> cd rgary_whisper
PS C:\Users\username\rgary_whisper> virtualenv venv
PS C:\Users\username\rgary_whisper> .\venv\Script\activate.ps1
(venv) PS C:\Users\username\rgary_whisper> pip install soundfile
(venv) PS C:\Users\username\rgary_whisper> pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
(venv) PS C:\Users\username\rgary_whisper> pip install ffmpeg-python
(venv) PS C:\Users\username\rgary_whisper> pip install -U git+https://github.com/jianfch/stable-ts.git
(venv) PS C:\Users\username\rgary_whisper> pip install -U demucs
(venv) PS C:\Users\username\rgary_whisper> python.exe .\main.py
```
