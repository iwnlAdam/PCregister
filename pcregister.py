print("Her kan du få en oversikt over hvilke pc-er som er registrert i pc pool og som er utleveringsklare.")
print("Alt du trenger å gjøre er å skrive inn SB nummeret på pc-en, og programmet vil deretter si ifra om pc-en er i pc pool eller ikke.")


def valg():
    outfile = open('pcdata.txt', 'w')
    print("Vennligst velg et av alternativene nedenfor")
    print("1 - Søk")
    print("2 - Registrer")
    print("3 - Kasser")
    choice = input("Velg et av alternativene: " )

    if choice == "1":
        valg1SB = input("Hva er SB nummeret til pc-en?: ")
        f = open('pcdata','r')
        data = f.read()
        print('data =',data)
        outfile.write(valg1SB)

    if choice == "2":
        valg2SB = input("Hva er SB nummeret til pc-en?: ")
        valg2Modell = input("Hvilken modell er det på Pc-en?: ")
        outfile.write(valg2SB + '\n')
        outfile.write(valg2Modell)

        outfile.close()
    
    if choice == "3":
        fileVariable  = open('pcdata.txt', 'r+')
        fileVariable.truncate(0)
        
        valg3SB = input("Hva er SB nummeret til pc-en?: ")
        valg3modell = input("Hvilken modell er det på Pc-en?: ")
        print("pc-en har fått status kassert")
        print("pc " + valg3SB + "  " + valg3modell +", er blitt oppdatert status til kassert")
        fileVariable.close()
        
valg()