import sys
import os

class CustomException(Exception):
    pass

class Research:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def file_reader(self):
        try:
            with open(self.path_to_file, 'r') as file:
                data = file.read()
            sp_data = data.split('\n')
            if len(sp_data[0].split(',')) != 2:
                raise CustomException("Неверный заголовок")
            if len(sp_data) < 2:
                raise CustomException("Слишком мало строк")
            for i in range(1, len(sp_data)):
                if sp_data[i] != "1,0" and sp_data[i] != "0,1":
                    raise CustomException("Неверная структура файла")
            return data
        except Exception as e:
            return(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        res = Research(arg).file_reader()
        if res != None:
            print(res)