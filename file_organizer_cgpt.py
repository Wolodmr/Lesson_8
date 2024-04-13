import os
import shutil

class FileOrganizer:
    FILE_EXTENSIONS = {
        '.pdf': 'PDFs',
        '.jpg': 'Images',
        '.png': 'Images',
        '.csv': 'CSVs',
        '.txt': 'TXTs',
        '.xls': 'XLS',
        '.xlsx': 'XLSX',
        '.py': 'PYs'
    }

    def get_user_input(self, message):
        return input(message)

    def validate_path(self, path):
        try:
            if os.path.isdir(path):
                return path
            else:
                print("The provided path is not a valid directory.")
                return None
        except OSError as e:
            print(f"Error validating the path: {e}")
            return None

    def get_files_in_directory(self, path):
        try:
            files_list = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
            return files_list
        except OSError as e:
            print(f"Error reading the directory: {e}")
            return []

    def extract_extension(self, file):
        return os.path.splitext(file)[1].lower()

    def create_folder(self, path, folder_name):
        new_path = os.path.join(path, folder_name)
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        return new_path

    def organize_files(self, files_list, path):
        for file in files_list:
            ext = self.extract_extension(file)
            folder_name = self.FILE_EXTENSIONS.get(ext, 'Others')
            folder_path = self.create_folder(path, folder_name)
            source_file_path = os.path.join(path, file)
            destination_file_path = os.path.join(folder_path, file)
            shutil.move(source_file_path, destination_file_path)
        print(f"All the files in the directory {path} have been processed successfully")

    def rename_folders(self, path):
        folders_list = [folder for folder in os.listdir(path) if os.path.isdir(os.path.join(path, folder))]
        if folders_list:
            rename_option = input("Would you like to rename some folders? (y/n): ")
            if rename_option.lower() == 'y':
                for folder in folders_list:
                    new_name = input(f"Enter new name for '{folder}': ").strip()
                    if new_name:
                        old_path = os.path.join(path, folder)
                        new_path = os.path.join(path, new_name)
                        os.rename(old_path, new_path)

    def move_file_between_folders(self, path):
        move_option = input("Would you like to move files between folders? (y/n): ")
        if move_option.lower() == 'y':
            folder_from = input("Enter the name of the source folder: ").strip()
            file_name = input("Enter the name of the file to move: ").strip()
            folder_to = input("Enter the name of the destination folder: ").strip()
            source_file = os.path.join(path, folder_from, file_name)
            destination_file = os.path.join(path, folder_to, file_name)
            shutil.move(source_file, destination_file)
            print(f"File '{file_name}' moved from '{folder_from}' to '{folder_to}' successfully")

    def copy_file_to_folder(self, path):
        copy_option = input("Would you like to copy a file to a specific folder? (y/n): ")
        if copy_option.lower() == 'y':
            folder_from = input("Enter the name of the source folder: ").strip()
            file_name = input("Enter the name of the file to copy: ").strip()
            folder_to = input("Enter the name of the destination folder: ").strip()
            source_file = os.path.join(path, folder_from, file_name)
            destination_file = os.path.join(path, folder_to, file_name)
            shutil.copy2(source_file, destination_file)
            print(f"File '{file_name}' copied to '{folder_to}' successfully")

    def perform_folder_manipulations(self, path):
        self.rename_folders(path)
        self.move_file_between_folders(path)
        self.copy_file_to_folder(path)

    def organize_directory(self):
        path = self.get_user_input("Please enter the path to the directory you want to organize: ").strip()
        path = self.validate_path(path)
        if path:
            files_list = self.get_files_in_directory(path)
            if files_list:
                self.organize_files(files_list, path)
                self.perform_folder_manipulations(path)

if __name__ == "__main__":
    organizer = FileOrganizer()
    organizer.organize_directory()
    print("Program completed. Exiting...")




