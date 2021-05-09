imie = 'Jan'
ile = 10
diagnoza = 'rak'
i = ile

while  i  >= 0:
    if i == 0:
        print("{0} nie ma już z nami".format(imie))
    else:
        print("{0} ma {1} i zostało mu {2} dni ".format(imie, diagnoza, i))
    i = i - 1

