from glob import iglob
import os
import librosa
import numpy as np
import pickle

AUDIO_PATH = '.\\genres_split\\'
AUDIO_LENGTH = 110250
OUTPUT_DIR = '.\\output'
OUTPUT_DIR_TRAIN = os.path.join(OUTPUT_DIR, 'train')
OUTPUT_DIR_TEST = os.path.join(OUTPUT_DIR, 'test')

os.makedirs(OUTPUT_DIR_TRAIN)
os.makedirs(OUTPUT_DIR_TEST)

class_ids = {
    'blues': 0,
    'classical': 1,
    'country': 2,
    'disco': 3,
    'hiphop': 4,
    'jazz': 5,
    'metal': 6,
    'pop': 7,
    'reggae': 8,
    'rock': 9,
}

def extract_class_id(wav_file):
    if 'blues' in wav_file:
        return class_ids.get('blues')
    elif 'classical' in wav_file:
        return class_ids.get('classical')
    elif 'country' in wav_file:
        return class_ids.get('country')
    elif 'disco' in wav_file:
        return class_ids.get('disco')
    elif 'hiphop' in wav_file:
        return class_ids.get('hiphop')
    elif 'jazz' in wav_file:
        return class_ids.get('jazz')
    elif 'metal' in wav_file:
        return class_ids.get('metal')
    elif 'pop' in wav_file:
        return class_ids.get('pop')
    elif 'reggae' in wav_file:
        return class_ids.get('reggae')
    elif 'rock' in wav_file:
        return class_ids.get('rock')

def read_audio_from_wav(wav_file):
    audio, sr = librosa.load(wav_file, sr=None, mono=True)
    audio = audio.reshape(-1, 1)
    return(audio)

for i, wav_file in enumerate(iglob(os.path.join(AUDIO_PATH, '**\\**.wav'), recursive=True)):
    class_id = extract_class_id(wav_file)
    audio = read_audio_from_wav(wav_file)

    # normalization
    # audio = (audio - np.mean(audio)) / np.std(audio)

    if len(audio) < AUDIO_LENGTH:
        audio = np.concatenate((audio, np.zeros(shape=(AUDIO_LENGTH - len(audio), 1))))
    elif len(audio) > AUDIO_LENGTH:
        audio = audio[0:AUDIO_LENGTH]

    output_folder = OUTPUT_DIR_TRAIN
    if i % 5 == 0:
        output_folder = OUTPUT_DIR_TEST
    
    output_filename = os.path.join(output_folder, str(i) + '.pkl')

    

    out = {'class_id': class_id,
           'audio': audio,
    }
    
    with open(output_filename, 'wb') as w:
        pickle.dump(out, w)

