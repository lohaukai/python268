ans = input().strip()
guess = input().strip()

while guess != ans:
    A = 0
    B = 0
    listAns = list(ans)
    listGuess = list(guess)
    for i in range(len(listGuess)):
        for j in range(len(listAns)):
            if listGuess[i] == listAns[j]:
                if i == j:
                    A += 1
                else:
                    B += 1
    print('%dA%dB' % (A, B))
    guess = input().strip()
else:
    print('4A0B')
    print('You Win!')

# a better way from pyt270141
# answer=list(input())
# answerSet=set(answer)
# while True:
#     a=0
#     b=0
#     s=""
#     guess=list(input())
#     guessSet=set(guess)
#     for i in range(4):
#         if(guess[i]==answer[i]):
#             a+=1
#     c=len(guessSet.intersection(answerSet))
#     b=c-a
#
#     s='%dA%dB'%(a,b)
#     print(s)
#     if s=='4A0B':
#         print("You Win!")
#         break