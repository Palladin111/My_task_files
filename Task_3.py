import os

folder_path = os.getcwd()

def get_data_files():

    list_files = []

    # Формируем список файлов *.txt
    for file in os.listdir(folder_path):
        if file.endswith('.txt'):
            list_files.append(file)

    list_1 = []
    dict_files = {}

    # Читаем содержимое файлов
    for name_files in list_files:
        with open(name_files, "r") as file:
            for line in file:
                list_1.append(line.strip())
            dict_files[len(list_1)] = name_files

    list_2 = sorted(dict_files)

    while True:
        file_name = input('Введите имя новвого файла, в который выводите все данные: ') + '.txt'

        # Формируем итоговый файл
        if file_name not in list_files:
            file_res = open(file_name, "w")
            for lens in list_2:
                with open(dict_files.get(lens), "r") as file:
                    f = file.read()
                    file_res.write(f'{dict_files.get(lens)}\n{lens}\n{f}\n')
            file_res.close()

            # Вывод содержимого итогового файла на экран
            with open(file_name, 'r') as file:
                data = file.read()

            return data

        else:
            print('Файл с таким именем существует.')

print(get_data_files())
