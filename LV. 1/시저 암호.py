def solution(s, n):
    res = ''
    print(ord('a'), ord('A'))
    for e in s:
        if (e == ' '):
            res += ' '
            continue
        if (e.isupper()):
            res += chr(65 + (ord(e) - 65 + n) % 26)
        else:
            res += chr(97 + (ord(e) - 97 + n) % 26)
    return res