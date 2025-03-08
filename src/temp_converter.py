""" Przyklad funkcji w Python:
def nazwaFunkcji(argument1, argument2, …)
        operacje i działania
        print(rezultaty)
"""

"""Zadania:
1. Napisać funkcje która przelicza stopnie Celsjusza na Fahrenheit
2. Napisać funkcje która przelicza stopnie Fahrenheit na Celsjusza
3. Napisać funkcje która przelicza stopnie Celsjusza na Fahrenheit lub odwrotnie w zależności od argumentu - to sie nazywa "refactoring of code". 
Czyli uproszczenie, reuzycie czesci kodu
"""

"""Zadania 2:
2. Dodac komentarze do kodu
3. Dodac do printow jednostke temperatury wynikowej i ladny tekst w stylu: "Temperatura na wejsciu: 21 [C] > Temperatura po przeliczeniu: 68.9 [F]." > https://www.w3schools.com/python/python_string_formatting.asp
"""

""" Zadanie 3:
1. Napisac nowa funkcje ktora liczy powierzchnie: trojkata, lub kwadratu, lub trapazu, lub kola - o podanych bokach, wysokosci lub promieniu.
"""


# Zamiana C na F
def convertCto(TempValue=0):
    TFahrenheit = 2 * (TempValue - 0.1 * TempValue) + 32
    print(TFahrenheit)
    return TFahrenheit


# Zamiana F na C
def convertFto(FTemp=0):
    CTemp = (FTemp - 32)/(9/5)
    print(CTemp)


# Zamiana C na F lub F na C w jednej funkcji
def twoWayConvertr(TempValue=0, TempType='C'):
    if (TempType == 'C'):
        TFahrenheit = 2 * (TempValue - 0.1 * TempValue) + 32
        print(TFahrenheit)
    else:
        CTemp = (TempValue - 32)/(9/5)
        print(CTemp)


# Zamiana C na F lub F na C w jednej funkcji - refactoring do jednego print'a
def twoWayConverteV2(TempValue=0, TempType='C'):
    if (TempType == 'C'):
        Result = 2 * (TempValue - 0.1 * TempValue) + 32
    else:
        Result = (TempValue - 32)/(9/5)
    print(Result)


# Funkcja która przelicza temperature z jednej do drugiej.

def twoWayConverterV4(TempValue=0, TempInType='K', TempOutType='C'):
    # Konwersja z Celcjusza  do Fahrenheita
    if (TempInType == 'C') & (TempOutType == 'F'):
        Result = 2 * (TempValue - 0.1 * TempValue) + 32
    # Konwersja z Fahrenheita na Celcjusza
    elif (TempInType == 'F') & (TempOutType == 'C'):   
        Result = (TempValue - 32) / (9/5)
     # Konwersja z Kelwina do Celcjusza
    elif (TempInType == 'K') & (TempOutType == 'C'):
        Result = (TempValue - 273.15)
    #Konwersja z Celcjusza do Kelvina
    elif (TempInType == 'C') & (TempOutType == 'K'):
        Result = (TempValue + 273.15)
    #Konwersja z Kelvina do Fahrenheita
    elif (TempInType == 'K') & (TempOutType == 'F'):
        Result = (1.8 * (TempValue - 273.15) + 32)
    #Konwersja z Fahrenheita do Kelvina
    elif (TempInType == 'F') & (TempOutType == 'K'):
        Result = ((TempValue - 32) / 1.8 + 273.15)
    # Jeśli inna litera wpisana niz w programie napisz, ze nie moze zkalkulowac
    else:
        return "Conversion not supported!"
    return f'Temperatura wejsciowa {TempValue} [{TempInType}] - Temperatura wyjsciowa/ rezultat {Result} [{TempOutType}].'


# Funkcja która liczy powierzchnie Square/Rectangle, Triangle, Trapezoid

def AreaMeasurer (Shape='Triangle', Length=0, Width=0, Height=0, Unit='CM2'): 
    if (Shape == 'Square/Rectangle'):
        Result = (Length * Width)
    elif (Shape == 'Triangle'):
        Result = ((Length * Width) / 2)
    elif (Shape == 'Trapezoid'):
        Result = (((Length + Width) * Height) / 2)
    else: 
        print('A mistake or you are lacking some IQ!') 
    print(f'The area of the {Shape} is {Result} [{Unit}]')    


# Wywolanie funkcji

# convprint(txt)ertCtoF(21)
# convertFtoC(69.8)
# twoWayConverter(69.8, 'F')
# twoWayConverterV2(21, 'C')
AreaMeasurer('Triangle', 8, 9,'CM')
