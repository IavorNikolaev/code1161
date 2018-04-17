import pip

def install(package):
    pip.main(['install', package])

if __name__ == '__main__':
    install('mock')



def adder(number):

    return number + 5 

def adder2(number1, number2):

    return number1 + number2

def uppercase_(string):

    return string.upper()  

def exclaim(string):

    return string.upper() + ' !'

def upper_number(string, number):

    return string.upper() + str(number)

def oddoreven(number): 

    if number % 2 == 0:  
        return 'even'
    else:  
        return 'odd'

def fixornot(does_it_move = True, should_it = True):

    if does_it_move == True:
        if should_it == True: 
            return 'np' 
        else: 
            return 'dt'
    else:
        if should_it == True:
            return 'WD40'
        else:
            return 'np'

def lol():

    return None 

def lister():

    ls = []
    for x in range(10):
        ls.append('*')
    return ls 

def lister2(ntimes,symbol):
    ls = []
    for x in range(ntimes):
        ls.append(symbol)
    return ls 


def feild():

    rows = []
    for x in range(10):
        colums = []
        for xx in range(10):
            colums.append('*')
        rows.append(colums)
    return rows 

def lol():

    return None 

def loops_4():

    colums = []
    for x in range(10):
        count = 0
        rows = []
        for xx in range(10):
            rows.append(count)
            count = count + 1
        colums.append(rows)
    return colums 

def loops_5():

    colums = []
    for x in range(10):
        rows = []
        for xx in range(x + 1):
            rows.append(xx)
        colums.append(rows)
    return colums

def asd(high,low)
    keepasking = True
    while keepasking == True 
        imput



def lol():

    return None 



