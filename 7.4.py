import sys

nazwa_pliku = sys.argv[1]

file = open(nazwa_pliku)

try:
    text = file.read()
    lines = text.split('\n')
finally:
    file.close()

liczba_znakow = 0
licznik_slow = 0
isEmpty = True
for line in lines:
    for i in line:
        if i != " ":
            if isEmpty:
                isEmpty = False
                licznik_slow +=1
            liczba_znakow += 1
        else:
            licznik_slow += 1

srednia = float(liczba_znakow) / float(licznik_slow)
print(str(srednia))