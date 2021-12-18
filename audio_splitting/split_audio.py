from pydub import AudioSegment
import os


genres = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

# milliseconds in the sound track
ranges = [(0,5000),(5000,10000),(10000,15000),(15000,20000),(20000,25000), (25000, 30000)] 


for genre in genres:
    counter = 0
    input_file_path = f'.\\genres_original\\{genre}\\'
    output_file_path = f'.\\genres_split\\{genre}\\'
    os.makedirs(output_file_path)

    while counter < 100:
        if counter < 10:
            file_name = f'{genre}.0000' + str(counter) + '.wav'
        else:
            file_name = f'{genre}.000' + str(counter) + '.wav'
            
        try: # jazz00054 wav file invalid
            sound_file = AudioSegment.from_file(input_file_path + file_name, format='wav')
        except FileNotFoundError:
            pass

        for x, y in ranges:
            new_file = sound_file[x : y]
            if counter < 10:
                new_file.export(
                    output_file_path + f'{genre}.0000' + str(counter) + '.' + str(x) + "-" + str(y) +".wav", format="wav")
            else:
                new_file.export(
                    output_file_path +f'{genre}.000' + str(counter) + '.' + str(x) + "-" + str(y) +".wav", format="wav")
        
        counter +=1







