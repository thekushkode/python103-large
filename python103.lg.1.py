# Python103, Large, exercise 1

#Print the first 100 triangle numbers

#defininf count var
count = 1

# interating while less than 100 and printing triangle number
while count < 100:
    print(int((count * (count + 1)) / 2))
    count += 1
