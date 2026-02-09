# rc = report card
def notas(*num, sit=False):
    for c in range(1, len(num)+1):
        for value in num:
            if c == 1:
                highest = value
                lowest = value
            else:
                if value > highest:
                    highest = value
                if value < lowest:
                    lowest = value
    average = sum(num)/len(num)
    rc = {'highest':highest, 'lowest':lowest, 'avarege':average}
    if sit == True:
        if average < 5:
            situation = 'BAD'
        elif average > 5 and average < 7:
            situation ='AVERAGE'
        else:
            situation = 'GOOD'
        rc['situation'] = situation
    print(rc)

notas(4, 11, 3, 1, 5, 10, 9, sit=False)