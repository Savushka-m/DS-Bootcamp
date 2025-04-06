class Must_read:
    try:
        with open("data.csv", 'r') as file:
            data = file.read()
            print(data)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    must_read = Must_read()