wartosc = float(input())
skala = input()

if skala == "K":
    c = wartosc - 273.15
    f = c * 9/5 + 32
    print(round(c, 2), round(f, 2))
elif skala == "C":
    k = wartosc + 273.15
    f = wartosc * 9/5 + 32
    print(round(k, 2), round(f, 2))
elif skala == "F":
    c = (wartosc - 32) * 5/9
    k = c + 273.15
    print(round(c, 2), round(k, 2))
