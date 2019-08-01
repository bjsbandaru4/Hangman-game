import random
words=['hello','how','are','you']
random.shuffle(words)
final=list(words[0])
print(final)
screen=[]
used=[]
screen.extend(final)
used.extend(screen)
print(final)
for i in range(len(screen)):
    screen[i]='_'
print(final)
print(" ".join(screen))
count=0
while count<len(final):
    guess=input('Guess a letter: ')
    guess=guess.lower()
    print(count)
    for i in range(len(final)):
        if final[i]==guess and guess in used:
            screen[i]=guess
            count +=1
            used.remove(guess)
    if guess not in screen:
        print('Wrong Guess')        
    print(''.join(screen))
print("wow, you have guessed!!")
