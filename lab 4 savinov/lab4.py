s = input()
razdeliteli= "«_.,;:\n\t!?»"
for razdel in razdeliteli:
    s=s.replace(razdel, ' ')
words = s.split()


special = ""
for j in words:
    bukva = False
    cifra = False
    znak = False
    for i in range (len(j)):
        simvol = j[i]
        if simvol.isalpha():
            bukva = True
        elif simvol.isdigit():
            cifra = True
        else:
            znak = True
    
    if bukva == True and cifra == True and znak == True:
        special = special + j + ' '

if special == "":
    print ("Слова со знаком, буквой и цифрой в данной строке отсутствуют :(")
else:
    print("Слова со знаком, буквой и цифрой: ", special.strip())


symmetric = ""
max_kol=0
for l in words:
    if l == l[::-1]:
        kol_cifr = 0
        for n in range(len(l)):
            simvol = l[n]
            if simvol.isdigit():
                kol_cifr += 1
        if kol_cifr > max_kol:
            max_kol = kol_cifr
            symmetric = l + ' '
        elif kol_cifr == max_kol:
            symmetric += l + ' '

if symmetric == "":
    print("Симметричные слова с максимальным количеством цифр в данной строке отсутсвуют :(")
else:
    print("Симметричные слова с максимальным количеством цифр: ", symmetric.strip())
