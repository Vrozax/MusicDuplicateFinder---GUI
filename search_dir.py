from tinytag import TinyTag
import glob
import create_list
import os


class search_dir:
    def search_files(self, pathFolder):
        list_folders = list_dirs(pathFolder)

        list_files = []
        files_list = [".mp3", ".flac", ".wav"]
        for fileType in files_list:

            try:
                # "**/*"+fileType
                for file in glob.glob(pathFolder + "/*" + fileType, recursive=True):
                    list_files.append(file)
            except:
                print(f"Folder {pathFolder} not exist")

        for folder in list_folders:
            for fileType in files_list:

                try:
                    # "**/*"+fileType
                    for file in glob.glob(pathFolder +"/" +folder + "/*" + fileType, recursive=True):

                        list_files.append(file)
                except:
                    print(f"Folder {folder} not exist")

        # create data about file
        complete_data = create_list.create_list()
        result = complete_data.create_list_music(list_files)

        return result


def list_dirs(pathFolder):
    return [d for d in os.listdir(pathFolder) if os.path.isdir(os.path.join(pathFolder, d))]
