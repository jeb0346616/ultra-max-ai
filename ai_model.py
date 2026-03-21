def predict(data):
    data = data.upper()
    b = data.count('B')
    s = data.count('S')

    if b > s:
        return 'BIG'
    elif s > b:
        return 'SMALL'
    else:
        return 'UNCERTAIN'