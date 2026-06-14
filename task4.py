u=input('You:')
u.lower()
print('Robot:',end='')
if u=='hello':
    print('Hi!')
elif u=='how are you':
    print('''I'm fine,thanks''')
elif u=='bye':
    print('Goodbye!')
else:
    print('Sorry,I cannot understand')
