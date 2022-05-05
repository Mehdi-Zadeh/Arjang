
alphabetString = 'ABCDEFGHIJKLMNOP'

# char: iterator,   alphabetString: iterable object
for char in alphabetString:
    if char in 'CFIM':
        continue
    elif char in 'hMbc':
        break
    else:
        print(char)
else:
    print('age halghe shekaste nashe man chap misham !')


# TIME_FIN

print("=" * 40)
for ind, char in enumerate(alphabetString, 6):
    print(f'index {ind}: {char}')


for ch1, ch2 in zip(alphabetString[::2], alphabetString[1::2]):
    print(ch1, ch2)
































