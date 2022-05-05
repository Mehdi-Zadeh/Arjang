# flow control:
# -------------

# if, for, while

age = 18
esteghlal = -35

if esteghlal:  # bool(esteghlal)
    print('inam team e akhe ?!!')


# chained conditioning
if age > 18:  # bool(age > 18)
    print('be sene ghanooni residi')
    if age > 60:  # nested if
        print('dige vaghte bazneshastegie')
elif 15 < age <= 18:
    print('ye kocholoo dige bayad sabr koni')
elif 12 < age <= 15:
    print('boro ba bozorgtaret bia')
else:  # if not
    print('ye chizi')


if age > 18:  # bool(age > 18)
    print('be sene ghanooni residi')
if 15 < age <= 18:
    print('ye kocholoo dige bayad sabr koni')
if 12 < age <= 15:
    print('boro ba bozorgtaret bia')
else:  # if not
    print('ye chizi')


print(bool(age > 18))














