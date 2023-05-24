import os
import shutil
import string
import unicodedata

# Define the allowed extensions for each file category
IMAGE_EXTENSIONS = ('JPEG', 'PNG', 'JPG', 'SVG')
VIDEO_EXTENSIONS = ('AVI', 'MP4', 'MOV', 'MKV')
DOCUMENT_EXTENSIONS = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
MUSIC_EXTENSIONS = ('MP3', 'OGG', 'WAV', 'AMR')
ARCHIVE_EXTENSIONS = ('ZIP', 'GZ', 'TAR')
PROGRAMMER_EXTENSIONS = ('PY', 'CPP', 'M')


class FileSorter:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.known_extensions = set()
        self.unknown_extensions = set()
        self.images = []
        self.videos = []
        self.documents = []
        self.programmers = []
        self.music = []
        self.archives = []

    def normalize(self, filename):
        # Transliterate Cyrillic characters to Latin and replace invalid characters with '_'
        valid_chars = f"-_.() {string.ascii_letters}{string.digits}"
        filename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode()
        return ''.join(c for c in filename if c in valid_chars)

    def sort_files(self):
        for root, dirs, files in os.walk(self.folder_path):
            # Ignore certain folders
            dirs[:] = [d for d in dirs if d not in ['images', 'video', 'audio', 'programmers', 'documents', 'archives']]

            for file in files:
                file_path = os.path.join(root, file)
                extension = file.split('.')[-1].upper()

                # Add the extension to the known_extensions list
                self.known_extensions.add(extension)

                # Determine the category of the file
                if extension in IMAGE_EXTENSIONS:
                    self.images.append(file_path)
                    dest_folder = 'images'
                elif extension in VIDEO_EXTENSIONS:
                    self.videos.append(file_path)
                    dest_folder = 'video'
                elif extension in DOCUMENT_EXTENSIONS:
                    self.documents.append(file_path)
                    dest_folder = 'documents'
                elif extension in MUSIC_EXTENSIONS:
                    self.music.append(file_path)
                    dest_folder = 'audio'
                elif extension in PROGRAMMER_EXTENSIONS:
                    self.programmers.append(file_path)
                    dest_folder = 'programmers'
                elif extension in ARCHIVE_EXTENSIONS:
                    self.archives.append(file_path)
                    dest_folder = 'archives'
                else:
                    self.unknown_extensions.add(extension)
                    continue

                # Normalize the file name and transfer it to the appropriate folder
                new_filename = self.normalize(file.split('.')[0]) + '.' + extension
                new_path = os.path.join(root, dest_folder, new_filename)
                os.makedirs(os.path.dirname(new_path), exist_ok=True)
                shutil.move(file_path, new_path)

        # Unpack and sort the files in the archives folder
        self.sort_archives()
        print("Files have been sorted.")

    def sort_archives(self):
        for archive in self.archives:
            archive_path = os.path.splitext(archive)[0]
            os.makedirs(archive_path, exist_ok=True)
            shutil.unpack_archive(archive, archive_path)

            # Recursively sort the files in the unpacked archive folder
            archive_sorter = FileSorter(archive_path)
            archive_sorter.sort_files()

            # Remove the original archive file
            os.remove(archive)


if __name__ == '__main__':
    folder_path = input("Enter the path to the folder: ")
    sorter = FileSorter(folder_path)
    print(sorter.normalize(folder_path))
    sorter.sort_files()
