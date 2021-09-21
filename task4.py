'''The make_zip function creates the zip files using for loops. The batch_rename
function changes the character case. The createFolderTree function
checks if a path exists, and creates sub folders, directories and files using
the os.path.exists, os.mkdir, os.path.join'''

import random
import zipfile
import os
import shutil

def make_zip(dir_path, zipf):
    for root, dirList, files in os.walk(dir_path):
        for file in files:
            zipf.write(os.path.relpath(os.path.join(root, file)))
    zipf.close()

def batch_rename(file_paths):
    for file in file_paths:
        if os.path.isfile(file):
            basename = os.path.basename(file)
            file_name, extension = os.path.splitext(basename)
            dirname = os.path.dirname(file)
            resultant_filename = file_name.lower() + extension.upper()
            os.rename(file, os.path.join(dirname, resultant_filename))


def create_FolderTree(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name, ignore_errors=True)
    os.mkdir(folder_name)
    root_folder_path = os.path.realpath(folder_name)

    backup_folder_path = os.path.join(root_folder_path, 'backup')
    working_folder_path = os.path.join(root_folder_path, 'working')
    os.mkdir(working_folder_path)
    os.mkdir(backup_folder_path)

    sub_working_folders = ['pics', 'docs', 'movie']
    
    for sub_folder in sub_working_folders:
        temp_folder_path = os.path.join(working_folder_path, sub_folder)
        os.mkdir(temp_folder_path)

    doc_folder_path = os.path.join(working_folder_path, 'docs')
    doc_files = ['CORONAVIRUS.txt', 'DANGEROUS.txt', 'KEEPSAFE.txt', 'STAYHOME.txt', 'HYGIENE.txt']
    for file in doc_files:
        file_path = os.path.join(doc_folder_path, file)
        with open(file_path, 'w') as dummy_file:
            pass
    doc_subfolders = ['school', 'party']
    for folder in doc_subfolders:
        os.mkdir(os.path.join(doc_folder_path, folder))
    
    batch_rename([os.path.join(doc_folder_path, file) for file in doc_files])
    archives = []
    for i in range(1, 6):
        zipfilename = os.path.join(backup_folder_path, f"{i}.zip")
        archives.append(zipfilename)
        zip_file = zipfile.ZipFile(zipfilename, 'w')
        make_zip(doc_folder_path, zip_file)
        zip_file.close()
    
    print("backup folder contents:")
    for file in os.listdir(backup_folder_path):
        print(f"\t{file}")
    
    disp_zip_file = random.choice(archives)
    print(f"\nContents in {os.path.relpath(disp_zip_file)}:")
    with zipfile.ZipFile(disp_zip_file, 'r') as display_contents:
        display_contents.printdir()


def accept_folder():
    folder_name = input("Enter a folder name>> ")
    return folder_name

def main():
    folderName = accept_folder()
    create_FolderTree(folderName)


main()