import random
print('Welcome To Hangman')
string=''
l=[]
list=['Ending','Insert','Coding','Delete','Number']
for i in list:
    a=i.lower()
    l.append(a)
word=random.choice(l)
print('Word = ',end='')
for i in range(len(word)):
    print('_',end=' ')
attempt=6
for a in range(attempt):
    letter=input('\nEnter your guess letter:')
    attempt-=1
    if letter in word:
        string+=letter
        for i in word:
            if i in string:
                print(i,end='')
            else:
                print('_',end='')
        if all(i in string for i in word):
            print('\nYou got the word\n')
            break
    else:
        print('Try again',end='')
    if attempt==0:
        print('\nGame Over\n')
        print('The word was:',word)

