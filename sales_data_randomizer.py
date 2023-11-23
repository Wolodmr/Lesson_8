# Extracting a data file with a data to handle from files kept in a special directory(dir).
# Data file extension can have one of number extensions, done in a tuple ext = (scv, xls, txt) 
# Data files are to be transferred from external depository to the special directory on this 
# machine. A path to the directory is to be specified by user
# Data files can in to the dir any time but they are to be handled once a day or with another
# user-specified frequency at a user-specified time of day during a user-specified period of some 
# seconds. A data function of the program is to: 1) Shuffle rows of data in a data file and 
# 2) Back up data file before shuffle the rows
#
# Changes in a data files and back ups are logged in a log file as events

# A function to exract a data file with a data to handle from files kept in a special directory(dir).
# Parameters: 'path_in' - a path to dir; 'path_out' - a path to a working directory, 'ext' - a tuple 
# with possible extensions of data file 
# def data_function(path_in):

# Extracting a data file with a data to handle from files kept in a special directory(dir):
def getting_file(p, p_s):
    import os, logging, datetime
    from datetime import timezone
    
    # Getting list of files from the input folder 'Csv':  
    path_initial = os.getcwd()   
    os.chdir(p)
    files = os.listdir()

    logging.basicConfig(filename=p_s + '//log.log', level=logging.DEBUG, filemode = 'w', format="%(asctime)s line:%(lineno)d %(levelname)s %(message)s")

    # file timestamp creation for the files in the 'Csv' folder:
    files_dict = {}
    for file in files:
        timestamp = os.path.getctime(file)

        # convertion the created timestamp into DateTime object (datestamp):
        datestamp = datetime.datetime.fromtimestamp(timestamp)
        datestamp = datestamp.astimezone(tz=None)

        # append file to the dictionary of files in the 'Csv' folder:
        files_dict[file] = datestamp
      
        logging.debug(f'File {str(file)} created at: {str(datestamp)}')
     

    # Sorting the dictionary of files in the 'files_dict' dictionary by their creation datestamp:
    dict(sorted(files_dict.items(), key=lambda item: item[1]), reverse=True)
    os.chdir(path_initial)
 
    return files_dict


def backup(p, p_o, p_s, ext, func):
    import logging
    number = str(1)
    import csv, random, os, datetime, shutil, logging

    # Getting list of files in the target folder 'Csv' from the 'files_dict.py' dictionary,
    # which was created in the 'getting_file.py' file:
    files = list(func.items())
    
    # Checking extensions of the files in the 'files_dict.py' dictionary by comparing them to
    # the extensions of the files in the 'ext' list 'extensions' in the 'Initial data' block (below):
    i = len(files)-1
    while i >= 0:
                    
        file_name = files[i][0]
        if str(file_name)[-4] == '.':
            extension = str(file_name)[-3:]
        elif str(file_name)[-5] == '.':
            extension = str(file_name)[-4:]
        elif str(file_name)[-3] == '.':
            extension = str(file_name)[-2:]   
        else:
            pass

        i -= 1
        if extension in str(ext):               
            print() 
            break
        else:           
            print('exception')
            logging.basicConfig(filename=p_s + '//log.log', level=logging.DEBUG, filemode = 'w', format="%(asctime)s line:%(lineno)d %(levelname)s %(message)s")
            logging.warning(f'File *.{extension} is not regular for the input folder "Csv"!')    
             
    
    # Creating a name of the backup file - 'file_backup':
    file_backup = str(file_name)[:(-len(extension)-1)] + number +'.'+ extension
    
    # Back up data file before shuffle the rows:
    source = p+'\\'+str(file_name)
    destination = p_o+'\\' + file_backup
    shutil.copyfile(source, destination)
    logging.basicConfig(filename=p_s+'\\'+'log.log', level=logging.DEBUG, filemode = 'w', format="%(asctime)s line:%(lineno)d %(levelname)s %(message)s")
    logging.debug(f'File {str(file_name)} is backed up to: {str(destination)}')

    # Name of the data file to be shuffled:
    return file_name
   
def sales_data_randomization(p, p_s, func):
    
    import csv, random, os, shutil, logging

    # Opening the data file to be shuffled:
    path_initial = os.getcwd() 
    os.chdir(p)
    file_name = p+ '\\' + func
    file = open(file_name, 'r')
    csvreader = list(csv.reader(file))
    logging.info(f'Handling the data file: {str(file_name)}')

    # Getting the header of the data file as a string:
    print()
    header = csvreader[0]
    print(" ".join(map(str,header))) 
    file.close()

    # Shuffling the rows of the data file and casting rows as lists to a string type:
    rows = csvreader[1:]
    random.shuffle(rows)
    for row in rows:
        print(",".join(map(str,row)))

    # Writing the shuffled rows of the data file back to the file:
    file_shuffled = p_s+ '\\' + 's_'+ func   
    data = open(file_shuffled, 'w') 
    data.write( " ".join(map(str,header))+ '\n')
    for row in rows:
        data.write(",".join(map(str,row)) + '\n')
    data.close()

    # Returning to the initial working directory:
    os.chdir(path_initial)
    return file_name
            
def main(t, ext, p, p_s, p_o, func): 

    #Executing the functions:
    #sales_data_randomization(path, path_shuffled, backup(path, path_out, path_shuffled, extensions, getting_file(path, path_shuffled)))
    func
    # Logging to the file 'py_log.log':
    import logging
    logging.basicConfig(filename=path_shuffled+'\\log.log', level=logging.DEBUG, filemode = 'w', format="%(asctime)s line:%(lineno)d %(levelname)s %(message)s")
    logging.info("Shuffle rows of the sales data. Backup source file.")
    

# Initial data:
time_handle = '12:03:00'
extensions = ['.csv', '.xls', '.xlsx']
path = 'C:\VS_Code\Camp_programs\Lessons\Csv'
path_shuffled = 'C:\VS_Code\Camp_programs\Lessons\Csv_shuffled'
path_out = 'C:\VS_Code\Camp_programs\Lessons\Sales_backup'

import time
from datetime import datetime
t = datetime.now()
t = t.strftime('%H:%M:%S')

while t < time_handle:
    time.sleep(5)
    t = datetime.now()
    t = t.strftime('%H:%M:%S')

    #Executing the functions:
main(time_handle, extensions, path, path_shuffled, path_out, sales_data_randomization(path, path_shuffled, backup(path, path_out, path_shuffled, extensions, getting_file(path, path_shuffled))))
