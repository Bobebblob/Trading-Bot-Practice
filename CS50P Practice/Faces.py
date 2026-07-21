def convert(a: str) -> str:
    a = a.replace(':)', '🙂')
    a = a.replace(':(', '🙁')
    return a

if __name__ == '__main__':
    b = input("Input your text: ")
    print(convert(b))