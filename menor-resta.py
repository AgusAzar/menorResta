numbers = [0,1,2,3,4,5,6,7,8,9]

def getLowerNumber():
    lenght = len(numbers)/2
    number = 0
    for n in range(lenght):
        number += numbers[n]*pow(10,(lenght-n)-1)        
    return number

def getBiggerNumber():
    lenght = len(numbers)/2
    reversedNumeros = list(numbers)
    reversedNumeros.reverse()
    number = 0
    for n in range(lenght):
        number += reversedNumeros[n]*pow(10,(lenght-n)-1)        
    return number

def getBiggerThanMedium(mediumValue):
    lenght = len(str(mediumValue))-1
    wildcard = pow(10,lenght)-1
    for number in numbers:
        value = number*pow(10,lenght) + wildcard
        if(value > mediumValue):
            numbers.remove(number)
            biggerNumber = number*pow(10,lenght)            
            print("Calculando primer valor mayor al promedio --- ",biggerNumber)
            break
    while lenght > 0:
        lenght -= 1
        newNumber = numbers[0]*pow(10,lenght)
        biggerNumber += newNumber
        print("Calculando primer valor mayor al promedio --- ",biggerNumber)
        del numbers[0]
    return biggerNumber


def getLowerThanMedium(mediumValue):
    lenght = len(str(mediumValue))-1
    wildcard = pow(10,lenght)-1
    for number in numbers:
        value = number*pow(10,lenght) + wildcard
        if(value <= mediumValue):
            numbers.remove(number)
            lowNumber = number*pow(10,lenght)            
            print("Calculando primer valor menor al promedio --- ",lowNumber)
            break
    newNumberList = numbers
    newNumberList.reverse()
    while lenght > 0:
        lenght -= 1
        newNumber = newNumberList[0]*pow(10,lenght)
        lowNumber += newNumber
        print("Calculando primer valor menor al promedio --- ",lowNumber)
        del newNumberList[0]
    return lowNumber

lowerNumber= getLowerNumber()
print("El menor numero es:",lowerNumber)
biggerNumber= getBiggerNumber()
print("El mayor numero es:",biggerNumber)
mediumValue = (lowerNumber + biggerNumber)/2
print("El valor promedio es:",mediumValue)

firstValueBiggerThanMedium = getBiggerThanMedium(mediumValue)
firstValueLowerThanMedium  = getLowerThanMedium(mediumValue)
diferencia = firstValueBiggerThanMedium - firstValueLowerThanMedium 

print("El menor numero mayor al promedio es:",firstValueBiggerThanMedium)
print("El mayor numero menor al promedio es:",firstValueLowerThanMedium)

print("La diferencia es:",diferencia)
