def playback(a):
    a = a.split(' ')
    final = ''
    for word in a:
        if word == a[-1]:
            final += word
        else:
            final += word + '...'
    return final

if __name__ == '__main__':
    b = input()
    print(playback(b))