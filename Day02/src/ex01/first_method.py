class Research:
    def file_reader():
        try:
            with open("../ex00/data.csv", 'r') as file:
                data = file.read()
                return(data)
        except Exception as e:
            return(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    print(Research.file_reader())