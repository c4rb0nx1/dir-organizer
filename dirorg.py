import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileCreatedHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"File added: {event.src_path}")
        print("Organizing...")
        main()

path = 'E:\My_Projects_(Niranchan)\Directory organiser'
event_handler = FileCreatedHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    
observer.join()

pdf = ['.pdf']
documents = ['.doc', '.docx', '.pdf', '.txt', '.rtf', '.tex', '.wpd', '.odt']
presentations = ['.ppt', '.pptx', '.pps', '.key']
spreadsheets = ['.xls', '.xlsx', '.ods', '.numbers']
images = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.psd', '.raw']
video = ['.avi', '.mov', '.mp4', '.mpeg','.wmv', '.flv', '.mkv', '.webm']
audio = ['.mp3', '.wav', '.wma', '.aac', '.flac', '.alac', '.aiff', '.ogg']
archieves = ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2']
executables = ['.exe', '.dmg', '.apk', '.msi']
scripts = ['.js', '.py', '.java', '.cpp', '.cs', '.rb', '.swift']
diskImages = ['.iso', '.vmdk', '.dmg']

dest_pdf = os.path.abspath('master-pdf')
dest_documents = os.path.abspath('master-documents')
dest_audio = os.path.abspath('master-audio')
dest_video = os.path.abspath('master-video')
dest_archieve = os.path.abspath('master-archieve')
dest_executable = os.path.abspath('master-executable')
dest_script = os.path.abspath('master-script')
dest_spreadsheets = os.path.abspath('master-spreadsheets')
dest_disk_images = os.path.abspath('master-disk-images')
dest_presentation = os.path.abspath('master-presentation')
dest_others = os.path.abspath('master-others')
dest_images = os.path.abspath('master-images')

master = [dest_pdf,dest_documents,dest_audio,dest_video,dest_archieve,dest_executable,dest_script,dest_spreadsheets,dest_disk_images,dest_presentation,dest_others]

file_name = 'dirorg.py'

def src(file_path):
    return os.path.abspath(file_path)

def extention(file_path):
    return '.' + list(file_path.split('.'))[-1]

def move(source,destination):
    try:
        shutil.move(source,destination)
        return "{} moved successfully!".format(source)
    except:
        return "source file already exists in destination :{}".format(destination)

def main():
    for file in os.listdir():
        if(file != file_name):
            ext = extention(file)
            source_path = src(file)
            if ext in pdf:
                dest_path = dest_pdf +'\\'+ file
                print(move(source_path,dest_path))
            
            elif ext in documents:
                dest_path = dest_documents +'\\'+ file
                print(move(source_path,dest_path))

            elif ext in audio:
                dest_path = dest_audio +'\\'+ file
                print(move(source_path,dest_path))

            elif ext in video:
                dest_path = dest_video +'\\'+ file
                print(move(source_path,dest_path))
            
            elif ext in presentations:
                dest_path = dest_presentation +'\\'+ file
                print(move(source_path,dest_path))

            elif ext in spreadsheets:
                dest_path = dest_spreadsheets +'\\'+ file
                print(move(source_path,dest_path))
            
            elif ext in archieves:
                dest_path = dest_archieve +'\\'+ file
                print(move(source_path,dest_path))
            
            elif ext in scripts:
                dest_path = dest_script +'\\'+ file
                print(move(source_path,dest_path))
            
            elif ext in diskImages:
                dest_path = dest_disk_images +'\\'+ file
                print(move(source_path,dest_path))

            elif ext in images:
                dest_path = dest_images +'\\'+ file
                print(move(source_path,dest_path))

            elif ext in executables:
                dest_path = dest_executable +'\\'+ file
                print(move(source_path,dest_path))

            else:
                dest_path = dest_others +'\\'+ file
                if 'master' not in file:
                    print(move(source_path,dest_path))
                else:
                    print("nothing to move")
             

if __name__ == '__main__':
    main()