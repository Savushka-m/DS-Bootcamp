import sys
import logging
from random import randint

class CustomException(Exception):
    pass

class Research:
    def __init__(self, path_to_file):
        self.logger = logging.getLogger('my_logger')
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('analytics.log')
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s,%(msecs)03d %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.path_to_file = path_to_file
        self.data = self.file_reader()
        self.calculation = self.Analytics(self.data)

    def file_reader(self, has_header = True):
        self.logger.debug("Считывание файла")
        try:
            with open(self.path_to_file, 'r') as file:
                data = file.read()
            sp_data = data.split('\n')
            if (len(sp_data[0].split(',')) != 2) and (has_header == 1):
                raise CustomException("Неверный заголовок")
            if len(sp_data) < 2:
                raise CustomException("Слишком мало строк")
            for i in range(has_header, len(sp_data)):
                if sp_data[i] != "1,0" and sp_data[i] != "0,1":
                    raise CustomException("Неверная структура файла")
            return [[int(i) for i in sp_data[j].split(',')] for j in range(has_header, len(sp_data))]
        except Exception as e:
            return(f"Произошла ошибка: {e}")
    
    class Calculations():
        def __init__(self, data):
            self.logger = logging.getLogger('my_logger')
            self.logger.setLevel(logging.DEBUG)
            file_handler = logging.FileHandler('analytics.log')
            file_handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s,%(msecs)03d %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
            self.data = data
        
        def counts(self):
            self.logger.debug("Подсчет количества орлов и решек")
            heads_tails = [0, 0]
            for i in self.data:
                if i[0] == 0:
                    heads_tails[1] += 1
                else:
                    heads_tails[0] += 1
            return heads_tails
        
        def fractions(self, heads_tails):
            self.logger.debug("Подсчет вероятностей орлов и решек")
            fract = [0, 0]
            fract[0] = heads_tails[0]/(heads_tails[0] + heads_tails[1]) * 100
            fract[1] = heads_tails[1]/(heads_tails[0] + heads_tails[1]) * 100
            return fract

    class Analytics(Calculations):
        def predict_random(self, num_forecast):
            self.logger.debug("Предсказание вероятности")
            predictions = []
            for i in range(num_forecast):
                t = randint(0,1)
                if t == 0:
                    predictions.append([0,1])
                else:
                    predictions.append([1,0])
            return predictions

        def predict_last(self):
            self.logger.debug("Последнее предсказание")
            return self.data[-1]

        def save_file(self, data, filename, ext = 'txt'):
            self.logger.debug("Сохранение репорта в файл")
            with open(f"{filename}.{ext}", "w") as file:
                file.write(data)