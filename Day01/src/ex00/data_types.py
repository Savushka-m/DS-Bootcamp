def data_types():
    sp = [1, "1", 1.0, True, [], {}, (), set()]
    res = []
    for i in sp:
        res.append(type(i).__name__)
    print("[" + ', '.join(res) + "]")

if __name__ == '__main__':
    data_types()