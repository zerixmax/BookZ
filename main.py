import repository as repo

def main_menu():
    """Prikazuje glavni izbornik aplikacije."""
    
    # Inicijalizacija baze - kreira tablice ako ne postoje
    repo.init_database()
    
    # Dodajmo neke početne podatke da ne bude prazno
    # (Ovo će se izvršiti samo ako već ne postoje)
    autor1 = repo.dodaj_autora("J.R.R.", "Tolkien")
    izdavac1 = repo.dodaj_izdavaca("Algoritam")
    
    # Dodajmo i knjigu (možeš obrisati kasnije)
    # repo.dodaj_knjigu("The Hobit", 150.00, True, autor1, izdavac1)

    while True:
        print("\n--- BOOKSHOP MENI ---")
        print("1. Prikaz svih knjiga")
        print("2. Dodaj novu knjigu")
        print("3. Ažuriraj cijenu knjige")
        print("4. Obriši knjigu")
        print("0. Izlaz")
        
        izbor = input("Odaberite opciju: ")
        
        if izbor == '1':
            # Prikaz svih knjiga [cite: 821]
            knjige = repo.dohvati_sve_knjige()
            if not knjige:
                print("Nema unesenih knjiga.")
            for knjiga in knjige:
                print(f"- ID: {knjiga.id}, Naziv: {knjiga.title}, Autor: {knjiga.author.first_name} {knjiga.author.last_name}, Izdavač: {knjiga.publisher.naziv}, Cijena: {knjiga.price} kn")
        
        elif izbor == '2':
            # Dodaj novu knjigu [cite: 820]
            print("--- Dodavanje nove knjige ---")
            title = input("Naziv: ")
            price = float(input("Cijena: "))
            # Ovdje bi išla i logika za odabir postojećeg autora/izdavača ili dodavanje novog
            # Za jednostavnost, koristimo prethodno dodane
            print("Koristim zadane autore i izdavače...")
            repo.dodaj_knjigu(title, price, True, autor1, izdavac1)

        elif izbor == '3':
            # Ažuriraj cijenu [cite: 823]
            try:
                book_id = int(input("Unesi ID knjige za ažuriranje: "))
                nova_cijena = float(input("Unesi novu cijenu: "))
                repo.azuriraj_cijenu_knjige(book_id, nova_cijena)
            except ValueError:
                print("Greška: ID i cijena moraju biti brojevi.")

        elif izbor == '4':
            # Obriši knjigu
            try:
                book_id = int(input("Unesi ID knjige za brisanje: "))
                repo.obrisi_knjigu(book_id)
            except ValueError:
                print("Greška: ID mora biti broj.")

        elif izbor == '0':
            print("Izlaz iz aplikacije.")
            break
        
        else:
            print("Nepoznata opcija, pokušajte ponovo.")

if __name__ == '__main__':
    main_menu()