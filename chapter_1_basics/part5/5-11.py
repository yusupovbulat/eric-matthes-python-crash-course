digits = []
for digit in range(1, 10):
    digits.append(digit)
for digit in digits:
    if digit == 1:
        ending = 'st'
    elif digit == 2:
        ending = 'nd'
    elif digit == 3:
        ending = 'rd'
    else:
        ending = 'th'
    print(str(digit) + ending)
