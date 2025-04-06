import sys
import os

class CustomException(Exception):
    pass

class Research:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.calculation = self.Calculations()

    def file_reader(self, has_header = True):
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
        def counts(self, data):
            heads_tails = [0, 0]
            for i in data:
                if i[0] == 0:
                    heads_tails[1] += 1
                else:
                    heads_tails[0] += 1
            return heads_tails
        
        def fractions(self, heads_tails):
            fract = [0, 0]
            fract[0] = heads_tails[0]/(heads_tails[0] + heads_tails[1]) * 100
            fract[1] = heads_tails[1]/(heads_tails[0] + heads_tails[1]) * 100
            return fract

if __name__ == "__main__":
    if len(sys.argv) == 2:
        res = Research(sys.argv[1])
        data = res.file_reader()
        counts = res.calculation.counts(data)
        fractions = res.calculation.fractions(counts)
        print(data)
        print(counts)
        print(fractions)