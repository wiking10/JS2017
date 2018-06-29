import sys

nazwa_pliku = sys.argv[1]
file = open(nazwa_pliku)

try:
    text = file.read()
    lines = text.split('\n')
    lines.pop()
finally:
    file.close()

for i in range(0, len(lines)):
    lines[i] = str(i+1) + " " + lines[i] + "\n"

newFile = open('nowy_plik.txt', 'w')
newFile.writelines(lines)
newFile.close()