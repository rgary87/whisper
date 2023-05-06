import stable_whisper
import datetime
import torch
import os
import glob
import sys

args = sys.argv
other_args = []
models = ['tiny', 'base', 'small', 'medium', 'large-v1', 'large-v2'],
model_str = "medium.en"
if len(args) == 1:
    mkv_files = glob.glob("X:\Community\Community.S01-S06.720p.WEB.DL.nHD.x264-NhaNc3\*.mkv")
else:
    mkv_files = [arg for arg in args[1:] if not arg.startswith('--')]
    other_args = [arg[2:] for arg in args[1:] if arg.startswith('--')]

print(f'Files are:')
for mkv in mkv_files:
    print(f'{mkv}')
for arg in other_args:
    if arg.startswith('model='):
        model_str = arg[6:] + '.en'

device = "cuda" if torch.cuda.is_available() else "cpu"
if device == "cpu":
    print('Cpu inference is too slooooow fix your cuda install!')
    exit(1)
print(f'Using {device} Device on {model_str} model')


model = stable_whisper.load_model(model_str, device=device)

for mkv in mkv_files:
    srt_path = f'{mkv[:-4]}-medium.srt'
    if os.path.exists(srt_path):
        continue
    print(f'{datetime.datetime.now()}: start transcribing {os.path.basename(mkv)}')
    result = model.transcribe(mkv,
                              language='en',
                              suppress_silence=True,
                            #   ts_num=8,
                              demucs=True,
                              )
    print(f'{datetime.datetime.now()}: End transcription')
    result.to_srt_vtt(srt_path, word_level=False)
    print(f'Subtitles are ready for {os.path.basename(mkv)}')

os.system("shutdown /s /t 0")
