import os, shutil
class FileOrganizer:
    def path_getting(self):
        user_input = input('Please enter the path to the directory you want to make some manipulations  \n')
        return user_input
    def path_validation(self, path):
        try:
            isFile = os.path.isfile(path)
            return path
        except OSError as e:
            print(f'The path is invalid: {e}. Enter another path, please \n')
            return None
    def mapping(self):
        mapping = {
                    '.pdf':'PDFs',
                    '.jpg':'Images',
                    '.png':'Images',
                    '.csv':'CSVs',
                    '.txt':'TXTs',
                    '.xls':'XLS',
                    '.xlsx':'XLSX',
                    '.py':'PYs'
        }
        
        return mapping
    

    def get_files_in_directory(self, path):
        try:
            # Get the list of all files in the specified directory
            files_list = os.listdir(path)

            # Filter out only files (excluding directories)
            files_list = [file for file in files_list if os.path.isfile(os.path.join(path, file))]

            return files_list
        except OSError as e:
            print(f"Error reading the directory: {e}")
            return None
    def get_folders_in_directory(self, path):
        try:
            # Get the list of all files in the specified directory
            files_list = os.listdir(path)

            # Filter out only files (excluding directories)
            folders_list = [file for file in files_list if not os.path.isfile(os.path.join(path, file))]

            return folders_list
        except OSError as e:
            print(f"Error reading the directory: {e}")
            return None
    def ext_extract(self, file):
        ext = os.path.splitext(file)[1]
        return ext  
    def mk_path(self, path, folder_name):
        new_path = os.path.join(path, folder_name)
        return new_path 
    def folder(self, ext, path):
        mapping = self.mapping()
        folder_name = mapping[ext]
        folder_path = self.mk_path(path, folder_name)
        os.mkdir(folder_path)
        return folder_name
    def files_distrib(self, files_list, path):
        answer = input('If you want to distribute files among folders, press "y", otherwise press "Enter" \n')
        if answer == 'y':
            folders = {}
            new_path = {}
            destination_file_path = {}
            for file in files_list:
                mapping = self.mapping()
                ext = self.ext_extract(file)
                folders_list = self.get_folders_in_directory(path)
                if ext in mapping:
                    folder_name = mapping[ext]
                else:
                    folder_name = 'OTHERS'
                if ext in mapping and folder_name in folders_list:
                    print('one')
                    folders[ext] = folder_name
                    new_path[ext] = self.mk_path(path, folders[ext])
                
                elif ext in mapping and ext not in folders:               
                    folders[ext] = self.folder(ext, path)
                    new_path[ext] = self.mk_path(path, folders[ext])
                elif ext not in mapping or ext == '':
                    if 'others' not in folders and 'OTHERS' not in folders_list:
                        print(folders)
                        print('two')
                        ext = 'others'
                        folder_name = 'OTHERS'
                        folder_path = self.mk_path(path, folder_name)
                        os.mkdir(folder_path)
                        new_path[ext] = self.mk_path(path, folder_name)
                    else:
                        ext = 'others'
                        folder_name = 'OTHERS'
                        folder_path = self.mk_path(path, folder_name)
                        new_path[ext] = self.mk_path(path, folder_name)
            
                source_file_path = self.mk_path(path, file)
                destination_file_path[ext] = self.mk_path(new_path[ext], file)
                shutil.move(source_file_path, destination_file_path[ext])
            return print('All the files in the directory {path} have been processed successfully')
    def custom_name_folder(self, path):
        folders_list = self.get_folders_in_directory(path)
        print(folders_list)
        answer = input('There are folders in the directory, you asserted. Would you rename some of this folders? Press "Enter" if not and "y", if yes  ')   
        
        if answer == 'y':
            for i in folders_list:
                folder_name = input(f'Enter your option for the {i} folder name   ') 
                if folder_name:
                   
                    folder_path_old = self.mk_path(path, i)
                    folder_path_new = self.mk_path(path, folder_name)

                    os.rename(folder_path_old, folder_path_new)  
                    i = folder_name 
      
        return None
    def folder_files_exchange(self, path):
                answer = input('If you want to move files between folders, press "y", othewise press "Enter" \n')
                if answer == 'y':
                    folders_list = self.get_folders_in_directory(path)
                    folder_to_withdraw_file = input('Enter name of a folder, from which you want to withdraw a file to move  \n')
                    file_to_move = input(f'Enter a file name to move it into another folder \n')
                    folder_to_recept_file = input('Enter a name of the folder to recept the file  \n')
                    source_folder = self.mk_path(path, folder_to_withdraw_file)
                    source_file = self.mk_path(source_folder, file_to_move)
                    destination_folder = self.mk_path(path, folder_to_recept_file)
                    destination_file = self.mk_path(destination_folder, file_to_move)
                    shutil.move(source_file, destination_file)
    
    def files_copy(self, path):
                answer = input('If you want to copy file into specific folder, press "y", othewise press "Enter" \n')
                if answer == 'y':
                    folders_list = self.get_folders_in_directory(path)
                    folder_to_withdraw_file = input('Enter name of a folder, from which you want to select a file to copy  \n')
                    file_to_move = input(f'Enter a file name to move it into another folder \n')
                    folder_to_recept_file = input('Enter a name of the folder to recept the file  \n')
                    source_folder = self.mk_path(path, folder_to_withdraw_file)
                    source_file = self.mk_path(source_folder, file_to_move)
                    destination_folder = self.mk_path(path, folder_to_recept_file)
                    destination_file = self.mk_path(destination_folder, file_to_move)
                    shutil.copy2(source_file, destination_file)



    def folders_exchange_manipulations(self, path):
        custom_answer = input('If you want to make some exchange manipulations with folders, press "y", othewise press "Enter" ')
        if custom_answer == 'y':
            answer = input('To move file between the folders, press "1", to copy file from one folder to another, press "2" \n')
            if answer == '1':
                self.folder_files_exchange(path)
            if answer == '2':
                self.files_copy(path)
        return None
               


     
f = FileOrganizer()
path = f.path_getting()
files_list = f.get_files_in_directory(path) #f.path_getting()) 
f.files_distrib(files_list, path) 
f.custom_name_folder(path)  
f.folders_exchange_manipulations(path)
    

        

