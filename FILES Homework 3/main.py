import os

BASE_PATH = os.getcwd()

def reader():
    files_dict = {}
    for file in os.listdir(BASE_PATH):
        if file.endswith('.txt'):
            with open(file, 'r', encoding='utf-8') as file_obj:
                files_list = file_obj.readlines()
                files_dict[file] = files_list
    final_sorted_dict = {}
    sorted_files_dict = sorted(files_dict.values(), key=len)
    print(sorted_files_dict)
    for file in sorted_files_dict:
        for key in files_dict:
            if files_dict[key] == file:
                    final_sorted_dict[key] = file
    for file, text in final_sorted_dict.items():
        with open('merge.txt', 'a', encoding='utf-8') as merge_file_obj:
            merge_file_obj.write(file + '\n')
            merge_file_obj.write(str(len(text)) + '\n')
            for line in text:
                if '\n' in line:
                    merge_file_obj.write(line)
                else:
                    merge_file_obj.write(line + '\n')

reader()
