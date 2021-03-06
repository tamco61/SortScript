from os import listdir, rename, mkdir

# this files script don't touch
exceptions = ['main.py', 'sortScript.py']


# function, that creates folder
def create_folder():
    for i in folders:
        if i not in list(listdir()):
            mkdir(i)

# formats
image_formats = ['jpg', 'png']
video_formats = ['mp4']
audio_formats = ['mp3']

# folders
folder_audio = 'audio'
folder_video = 'video'
folder_image = 'image'
folder_other = 'other'
folders = [folder_audio, folder_image, folder_video, folder_other]

# getting files in directory
lst = list(listdir())

# sorting files in directory
lst_video = list()
lst_image = list()
lst_audio = list()
lst_other = list()
files = [lst_audio, lst_image, lst_video, lst_other]

for file in lst:
    if '.' in file:
        if file.split('.')[0] == '' or file in exceptions:
            continue
        form = file.split('.')[1]
        if form in video_formats:
            lst_video.append(file)
        elif form in audio_formats:
            lst_audio.append(file)
        elif form in image_formats:
            lst_image.append(file)
        else:
            lst_other.append(file)

# creating folders
create_folder()

# move files
for i in range(len(folders)):
    folder = folders[i]
    for r in range(len(files[i])):
        file = files[i][r]
        rename(file, f'{folder}/{file}')
