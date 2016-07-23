ans = input().strip()
guess = input().strip()
while guess != ans:
    A = 0
    B = 0
    listAns = list(ans)
    listGuess = list(guess)
    for i in len(listGuess):
        if listGuess[i] == listAns[i]:
            ++A
        elif listGuess[i] == listAns[i+1] or listGuess[i] == listAns[i+2] or listGuess[i] == listAns[i+3]:
            ++B
    print('%dA%dB' % (A, B))
