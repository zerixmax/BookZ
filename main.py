import repository as repo
from pyfiglet import figlet_format

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
        # ANSI escape kod za zelenu boju
        GREEN = "\033[92m"
        RESET = "\033[0m"
        
        print("\n" + GREEN + figlet_format("BookZ", font="slant") + RESET)
        print(GREEN + figlet_format("PyZ3R", font="slant") + RESET)
        print()
        print("--- BOOKSHOP MENI ---")
        print("1. Prikaz svih knjiga")
        print("2. Dodaj novu knjigu")
        print("3. Ažuriraj cijenu knjige")
        print("4. Obriši knjigu")
        print("0. Izlaz")
        
        izbor = input("Odaberite opciju: ")
        
        if izbor == '1':
            # Prikaz svih knjiga [cite: 821]
            print("\n" + figlet_format("Knjige", font="small"))
            knjige = repo.dohvati_sve_knjige()
            if not knjige:
                print("Nema unesenih knjiga.")
            for knjiga in knjige:
                print(f"- ID: {knjiga.id}, Naziv: {knjiga.title}, Autor: {knjiga.author.first_name} {knjiga.author.last_name}, Izdavač: {knjiga.publisher.naziv}, Cijena: {knjiga.price} kn")
        
        elif izbor == '2':
            # Dodaj novu knjigu [cite: 820]
            print("\n" + figlet_format("Nova Knjiga", font="mini"))
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

        elif izbor == 'art' or izbor == 'ascii':
            # Skriveni izbornik za ASCII art
            print("\n" + figlet_format("ASCII Gallery", font="slant"))
            print(figlet_format("BookZ", font="banner3"))
            print(figlet_format("Python", font="digital"))
            print(figlet_format("Coding", font="bubble"))
            print(figlet_format("Fun!", font="3-d"))
            input("\nPritisnite Enter za povratak...")
        
        elif izbor == '9':
            # Skriveni izbornik - samo PyZ3R ASCII art
            print("\n" + GREEN + figlet_format("PyZ3R", font="roman") + RESET)
            input("\nPritisnite Enter za povratak...")
        
        elif izbor == '0':
            print("\n" + figlet_format("Dovidjenja!", font="mini"))
            break
        
        else:
            print("Nepoznata opcija, pokušajte ponovo.")

if __name__ == '__main__':
    main_menu()