
# while <condition>:
#     <statements>

peopleString = 'plkjppfpdspssdppsdkjpphakjhpgsadppsdsd'

peopleCounter = 0
indexCounter = 0

notEnoughPeople = False  # flag

while peopleCounter - 10:

    try:
        if peopleString[indexCounter] == 'p':
            peopleCounter = peopleCounter + 1
        indexCounter = indexCounter + 1
    except IndexError:  # catch exception
        notEnoughPeople = True
        break
    except OverflowError:
        break
    # else:
    # finally:

if not notEnoughPeople:
    print(f'I found {peopleCounter} people at index: {indexCounter}')
else:
    print('ooni ke poshte saresh boodi mastesho gereft raft !')













