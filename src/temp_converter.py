# def nazwaFunkcji(argument1, argument2, …)
# operacje i działania
# operacje i działania
# print(rezultaty)

# Zadania:
# Napisać funkcje która przelicza stopnie Celsjusza na farenheit
# Napisać funkcje która przelicza stopnie farenheit na Celsjusza
# Napisać funkcje która przelicza stopnie Celsjusza na farenheit lub odwrotnie w zależności od argumentu


# Zamiana C na F
def convertCtoF(TempValue=0):
    TFahrenheit = 2 * (TempValue - 0.1 * TempValue) + 32
    print(TFahrenheit)
    return TFahrenheit


# Zamiana F na C
def convertFtoC(FTemp=0):
    CTemp = (FTemp - 32)/(9/5)
    print(CTemp)


# Zamiana C na F lub F na C w jednej funkcji
def twoWayConverter(TempValue=0, TempType='C'):
    if (TempType == 'C'):
        TFahrenheit = 2 * (TempValue - 0.1 * TempValue) + 32
        print(TFahrenheit)
    else:
        CTemp = (TempValue - 32)/(9/5)
        print(CTemp)


# Zamiana C na F lub F na C w jednej funkcji - refactoring do jednego print'a
def twoWayConverterV2(TempValue=0, TempType='C'):
    if (TempType == 'C'):
        Result = 2 * (TempValue - 0.1 * TempValue) + 32
    else:
        Result = (TempValue - 32)/(9/5)
    print(Result)


def twoWayConverterV3(TempValue=0, TempType='KtoC'):
    # Konwersja z C do F
    if (TempType == 'CtoF'):
        Result = 2 * (TempValue - 0.1 * TempValue) + 32
    elif (TempType == 'FtoC'):
        Result = (TempValue - 32) / (9/5)
    elif (TempType == 'KtoC'):
        Result = (TempValue - 273.15)
    elif (TempType == 'CtoK'):
        Result = (TempValue + 273.15)
    elif (TempType == 'KtoF'):
        Result = (1.8 * (TempValue - 273.15) + 32)
    elif (TempType == 'FtoK'):
        Result = ((TempValue - 32) / 1.8 + 273.15)
    else:
        print("Conversion not supported!")
    print(Result)
