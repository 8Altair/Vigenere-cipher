from time import time
import string as s


def korisnicki_interface():
    print("Zdravo.\n")
    print('Ako zelite sifrovati tekst, unesite "0".')
    print('Ako zelite desifrovati tekst, unesite "1".')
    korisnicki_odgovor = str(input("Vas odgovor: "))
    while korisnicki_odgovor != "0" and korisnicki_odgovor != "1":
        print("Smijete unijeti samo jednu od dvije opcije!")
        korisnicki_odgovor = str(input("Ponovo unesite odgovor: "))
    return korisnicki_odgovor


def unos_teksta():
    uneseni_tekst = ""
    ucitati = str(input("Zelite li ucitati tekst iz file-a (da/ne)? "))
    while ucitati != "da" and ucitati != "ne":
        ucitati = str(input("Odgovor nije validan!"))
    if ucitati == "da":
        file = str(input("Unesite ime file-a (txt): "))
        file += ".txt"
        with open(file, "r") as f:
            for red in f:
                uneseni_tekst += red
    else:
        print("Unesite tekst:\n")
        uneseni_tekst = str(input())

    ispravno = 1
    while not ispravno:
        for j in range(len(uneseni_tekst)):
            if uneseni_tekst[j].isdigit():
                ispravno = 0
                print("Uneseni tekst ne smije sadrzavati brojeve.")
                print("Ponovo unesite zeljeni tekst: \n")
                uneseni_tekst = str(input())
                break
    return uneseni_tekst.upper()


def unos_kljuca(duzina_teksta):
    kljuc = str(input("Unesite kljuc za sifrovanje: "))
    ispravno = -1
    while ispravno != 1:
        if len(kljuc) <= duzina_teksta:
            ispravno = 0
        else:
            print("Duzina kljuca ne smije biti veca od duzine teksta koji zelite sifrovati")
            kljuc = str(input("Ponovo unesite kljuc za sifrovanje: "))
            continue
        for j in range(len(kljuc)):
            if kljuc[j].isdigit():
                ispravno = -1
                print("Uneseni kljuc ne smije sadrzavati brojeve.")
                kljuc = str(input("Ponovo unesite kljuc za sifrovanje: "))
                break
        if ispravno == 0:
            ispravno = 1
    return kljuc.upper()


def filtriranje_teksta(tekst_za_filtriranja):
    for znak in tekst_za_filtriranja:
        if znak in s.punctuation or znak == " " or znak == "\n":
            tekst_za_filtriranja = tekst_za_filtriranja.replace(znak, "")
    return tekst_za_filtriranja


def izjednacavanje_duzine_kljuca(kljuc, duzina_teksta):
    ponavljajuci_kljuc = kljuc
    indeks_slova = 0
    while len(ponavljajuci_kljuc) < duzina_teksta:
        ponavljajuci_kljuc += kljuc[indeks_slova]
        indeks_slova += 1
        if indeks_slova == len(kljuc):
            indeks_slova = 0
    return ponavljajuci_kljuc


def najveci_zajednicki_djelilac_udaljenosti(tekst):

    lista_udaljenosti = []
    ispitane_trojke = {}
    for j in range(len(tekst) - 2):

        tri_znaka = tekst[j:j + 3]
        if tri_znaka not in ispitane_trojke:
            ispitane_trojke[tri_znaka] = 1
        for k in range(j + 3, len(tekst) - 2):
            if tekst.count(tri_znaka) < 2 or tekst.count(tri_znaka) == ispitane_trojke[tri_znaka]:
                break
            else:
                nova_tri_znaka = tekst[k:k + 3]
                if nova_tri_znaka == tri_znaka:
                    ispitane_trojke[tri_znaka] += 1
                    lista_udaljenosti.append(k - j)
                    break
    lista_nzd = []
    for j in range(len(lista_udaljenosti)):
        for k in range(1, (lista_udaljenosti[j]) + 1):
            if lista_udaljenosti[j] % k == 0:
                lista_nzd.append(k)
    if not lista_nzd:
        print("Tekst je previse mali za dekripciju.")
        izlaz = input('Pritinite "enter" za izlaz.')
        exit(1)
    lista_nzd.sort()
    frekvencije_nzd = [lista_nzd[0]]
    indeks_elementa = len(lista_udaljenosti)
    while indeks_elementa < len(lista_nzd):
        if lista_nzd.count(lista_nzd[indeks_elementa]) / len(lista_udaljenosti) >= 0.5 and \
                lista_nzd[indeks_elementa] <= min(lista_udaljenosti):
            frekvencije_nzd.append(lista_nzd[indeks_elementa])
        indeks_elementa += lista_nzd.count(lista_nzd[indeks_elementa])
    return frekvencije_nzd[-1]


def indeks_koincidencije(dio_teksta):
    frekvencije_slova = {}
    for z in dio_teksta:
        if z in frekvencije_slova:
            frekvencije_slova[z] += 1
        else:
            frekvencije_slova[z] = 1
    suma_frekvencija = 0
    n = len(dio_teksta)
    for k in range(26):
        if chr(ord("A") + k) in frekvencije_slova:
            suma_frekvencija += (frekvencije_slova[chr(ord("A") + k)] * (frekvencije_slova[chr(ord("A") + k)] - 1))
    return suma_frekvencija / (n * (n - 1))


def medjusobni_indeks_koincidencije(dio_teksta):
    # frekvencija_slova_u_promilima = {"A": 115, "B": 15, "C": 28, "D": 37, "E": 84, "F": 3, "G": 16, "H": 8, "I": 98,
    #                                  "J": 51, "K": 36, "L": 33, "M": 31, "N": 66, "O": 90, "P": 29, "Q": 0, "R": 54,
    #                                  "S": 56, "T": 48, "U": 43, "V": 35, "W": 0, "X": 0, "Y": 0, "Z": 23}
    frekvencija_slova_u_promilima = {"A": 82, "B": 15, "C": 28, "D": 43, "E": 130, "F": 22, "G": 20, "H": 61, "I": 70,
                                     "J": 1.5, "K": 7.7, "L": 40, "M": 24, "N": 67, "O": 75, "P": 19, "Q": 0.95, "R": 60,
                                     "S": 63, "T": 91, "U": 28, "V": 98, "W": 24, "X": 1.5, "Y": 20, "Z": 0.74}

    frekvencije_slova = {}
    for z in dio_teksta:
        if z in frekvencije_slova:
            frekvencije_slova[z] += 1
        else:
            frekvencije_slova[z] = 1
    lista_vrijednosti = []
    for g in range(26):
        suma = 0
        for k in range(26):
            indeks = 0
            if (k - g) < 0:
                indeks = 26 + (k - g)
            else:
                indeks = k - g
            if (chr(ord("A") + indeks)) in frekvencije_slova:
                suma += ((frekvencija_slova_u_promilima[chr(ord("A") + k)] / 1000) *
                         (frekvencije_slova[chr(ord("A") + indeks)]))
        suma /= 26
        lista_vrijednosti.append(suma)
    return lista_vrijednosti


def konverzija(broj):
    return chr(ord("A") + (broj % 26))


odgovor = korisnicki_interface()
print()
tekst = unos_teksta()
print()
tekst = filtriranje_teksta(tekst)
duzina_teksta = len(tekst)

rijecnik_alphabeta = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
                      "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22,
                      "X": 23, "Y": 24, "Z": 25}

pocetak_izvrsavanja = time()

if odgovor == "0":

    kljucna_rijec = filtriranje_teksta(unos_kljuca(duzina_teksta))
    produzena_kljucna_rijec = izjednacavanje_duzine_kljuca(kljucna_rijec, duzina_teksta)

    sifrovan_tekst = ""
    for i in range(duzina_teksta):
        sifrovan_tekst += konverzija((rijecnik_alphabeta[tekst[i]] + rijecnik_alphabeta[produzena_kljucna_rijec[i]]))
    print(sifrovan_tekst)

    upis = str(input("Zelite li upisati sifrat u file (da/ne)? "))
    while upis != "da" and upis != "ne":
        upis = str(input("Odgovor nije validan!"))
    if upis == "da":
        ime_file = str(input("Unesite ime file-a: "))
        ime_file += ".txt"
        file = open(ime_file, "a")
        pocetak_linije = 0
        for i in range(len(sifrovan_tekst)):
            if pocetak_linije + 20 < len(sifrovan_tekst):
                file.write(sifrovan_tekst[pocetak_linije:pocetak_linije + 20])
            else:
                file.write(sifrovan_tekst[pocetak_linije:])
            pocetak_linije += 20
            file.write("\n")
        file.close()

else:
    pretpostavljena_duzina_kljuca = najveci_zajednicki_djelilac_udaljenosti(tekst)
    slucajevi = []
    for i in range(pretpostavljena_duzina_kljuca):
        podnizovi_teksta = []
        for j in range(i + 1):
            podnizovi_teksta.append("")
        slucajevi.append(podnizovi_teksta)
    for i in range(len(slucajevi)):
        brojac = 0
        for slovo in tekst:
            slucajevi[i][brojac] += slovo
            brojac += 1
            if brojac == i + 1:
                brojac = 0

    indeksi_koincidencije = []
    for i in range(pretpostavljena_duzina_kljuca):
        niz = []
        for j in range(i + 1):
            niz.append(indeks_koincidencije(slucajevi[i][j]))
        indeksi_koincidencije.append(niz)
    aritmeticke_sredine_indeksa = []
    for i in range(len(indeksi_koincidencije)):
        aritmeticke_sredine_indeksa.append(sum(indeksi_koincidencije[i]) / len(indeksi_koincidencije[i]))

    jedan_ili_svi = 0
    for i in range(len(indeksi_koincidencije)):
        for j in range(i + 1):
            if 0.063 < indeksi_koincidencije[i][j] < 0.066:
                if 0.055 <= aritmeticke_sredine_indeksa[i] <= 0.75:
                    jedan_ili_svi = 1
                    break
        if jedan_ili_svi:
            break

    if jedan_ili_svi:
        tabela_vrijednosti = []
        for i in range(len(slucajevi[-1])):
            tabela_vrijednosti.append(medjusobni_indeks_koincidencije(slucajevi[-1][i]))
        pronadjeni_kljuc = ""
        for i in range(len(tabela_vrijednosti)):
            h = tabela_vrijednosti[i].index(max(tabela_vrijednosti[i]))
            kj = -h
            if kj < 0:
                kj += 26
                if kj < 0:
                    kj += 26
            pronadjeni_kljuc += konverzija(kj)

        produzena_kljucna_rijec = izjednacavanje_duzine_kljuca(pronadjeni_kljuc, duzina_teksta)

        desifrovan_tekst = ""
        for i in range(duzina_teksta):
            desifrovan_tekst += konverzija(
                (rijecnik_alphabeta[tekst[i]] - rijecnik_alphabeta[produzena_kljucna_rijec[i]]))
        print("Kljuc sifrata:", pronadjeni_kljuc)
        print(desifrovan_tekst)
        print("\nVrijeme izvrsavanja dekripcije:", (time() - pocetak_izvrsavanja), "sekundi")

        upis = str(input("Zelite li upisati originalni tekst u file (da/ne)? "))
        while upis != "da" and upis != "ne":
            upis = str(input("Odgovor nije validan!"))
        if upis == "da":
            ime_file = str(input("Unesite ime file-a: "))
            ime_file += ".txt"
            file = open(ime_file, "a")
            pocetak_linije = 0
            for i in range(len(desifrovan_tekst)):
                if pocetak_linije + 20 < len(desifrovan_tekst):
                    file.write(desifrovan_tekst[pocetak_linije:pocetak_linije + 20])
                else:
                    file.write(desifrovan_tekst[pocetak_linije:])
                pocetak_linije += 20
                file.write("\n")
            file.close()
    else:
        print("Moguci tekstovi:\n")
        file = open("Dekriptovano.txt", "a")
        file.write("Potrebno je listati dole zbog velikog broja razmaka.\n")
        file.close()
        for j in range(len(slucajevi)):

            tabela_vrijednosti = []
            for k in range(len(slucajevi[j])):
                tabela_vrijednosti.append(medjusobni_indeks_koincidencije(slucajevi[j][k]))
            pronadjeni_kljuc = ""
            for k in range(len(tabela_vrijednosti)):
                h = tabela_vrijednosti[k].index(max(tabela_vrijednosti[k]))
                kj = -h
                if kj < 0:
                    kj += 26
                    if kj < 0:
                        kj += 26
                pronadjeni_kljuc += konverzija(kj)

            produzena_kljucna_rijec = izjednacavanje_duzine_kljuca(pronadjeni_kljuc, duzina_teksta)

            desifrovan_tekst = ""
            for k in range(duzina_teksta):
                desifrovan_tekst += konverzija(
                    (rijecnik_alphabeta[tekst[k]] - rijecnik_alphabeta[produzena_kljucna_rijec[k]]))
            print("Kljuc sifrata:", pronadjeni_kljuc)
            print(desifrovan_tekst, "\n")

            file = open("Dekriptovano.txt", "a")
            pocetak_linije = 0
            for i in range(len(desifrovan_tekst)):
                if pocetak_linije + 20 < len(desifrovan_tekst):
                    file.write(desifrovan_tekst[pocetak_linije:pocetak_linije + 20])
                else:
                    file.write(desifrovan_tekst[pocetak_linije:])
                pocetak_linije += 20
                file.write("\n")
            file.close()

        print("\nVrijeme izvrsavanja dekripcije i upisa u file:", (time() - pocetak_izvrsavanja), "sekundi")

print("Zahvaljujemo se na koristenju naseg programa.")
izlaz = input('Pritinite "enter" za izlaz.')
