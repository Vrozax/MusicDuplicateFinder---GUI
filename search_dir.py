from tinytag import TinyTag
import glob
import create_list
import os


class search_dir:
    global list_folders_to_check

    def save_folders(self, list_folders_to_check, start_folder):
        list_folders = list_dirs(start_folder)

        for folder in list_folders:

            list_folders_to_check.append(str(start_folder+"/"+folder))
            self.save_folders(list_folders_to_check, start_folder+"/"+folder)

    def search_files(self, pathFolder, label_statistic_files):
        list_folders_to_check = []

        #list_folders = list_dirs(pathFolder)

        self.save_folders(list_folders_to_check, pathFolder)

        list_files = []
        files_list = [".mp3", ".flac", ".wav"]
        for fileType in files_list:

            try:
                # "**/*"+fileType
                for file in glob.glob(pathFolder + "/*" + fileType, recursive=True):
                    list_files.append(file)
            except:
                print(f"Folder {pathFolder} not exist")

        for folder in list_folders_to_check:
            for fileType in files_list:

                try:
                    # "**/*"+fileType
                    for file in glob.glob(folder + "/*" + fileType, recursive=True):

                        list_files.append(file)
                except:
                    print(f"Folder {folder} not exist")

        # create data about file
        complete_data = create_list.create_list()
        result = complete_data.create_list_music(list_files)
        label_statistic_files["text"] = "Files:" + str(len(result))
        return result


def list_dirs(pathFolder):
    return [d for d in os.listdir(pathFolder) if os.path.isdir(os.path.join(pathFolder, d))]
