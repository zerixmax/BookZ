from sqlalchemy.orm import Session
from models import engine, Author, Book, Publisher, init_database  # Uvozimo iz models.py

# --- CRUD Funkcije za Autore ---

def dodaj_autora(first_name, last_name):
    """Dodaje novog autora u bazu."""
    with Session(engine) as session:
        # Provjera da li autor već postoji (kao u tvom app.py)
        author_from_db = session.query(Author).filter(
            (Author.first_name == first_name) & (Author.last_name == last_name)
        ).first()
        
        if author_from_db is None:
            novi_autor = Author(first_name=first_name, last_name=last_name)
            session.add(novi_autor)
            session.commit()
            print(f"Dodan autor: {novi_autor.first_name} {novi_autor.last_name}")
            return novi_autor
        else:
            print(f"Autor {first_name} {last_name} već postoji.")
            return author_from_db

# --- CRUD Funkcije za Izdavače ---

def dodaj_izdavaca(naziv):
    """Dodaje novog izdavača u bazu."""
    with Session(engine) as session:
        publisher_from_db = session.query(Publisher).filter(Publisher.naziv == naziv).first()
        
        if publisher_from_db is None:
            novi_izdavac = Publisher(naziv=naziv)
            session.add(novi_izdavac)
            session.commit()
            print(f"Dodan izdavač: {novi_izdavac.naziv}")
            return novi_izdavac
        else:
            print(f"Izdavač {naziv} već postoji.")
            return publisher_from_db

# --- CRUD Funkcije za Knjige (po uputama [cite: 810, 811, 813, 814]) ---

def dodaj_knjigu(title, price, availability, author, publisher):
    """Dodaje novu knjigu."""
    with Session(engine) as session:
        # Moramo dohvatiti 'pune' objekte autora i izdavača koje prati session
        author_db = session.get(Author, author.id)
        publisher_db = session.get(Publisher, publisher.id)

        if not author_db or not publisher_db:
            print("Greška: Autor ili Izdavač nisu pronađeni u bazi.")
            return

        nova_knjiga = Book(title=title, price=price, availability=availability, 
                          author=author_db, publisher=publisher_db)
        session.add(nova_knjiga)
        session.commit()
        print(f"Dodana knjiga: {nova_knjiga.title}")

def dohvati_sve_knjige():
    """Dohvaća sve knjige s autorima i izdavačima."""
    with Session(engine) as session:
        # Koristimo logiku JOIN-a (implicitni) iz tvog app.py
        books = session.query(Book).all()
        return books

def azuriraj_cijenu_knjige(book_id, nova_cijena):
    """Ažurira cijenu knjige na temelju ID-a."""
    with Session(engine) as session:
        # Koristimo UPDATE logiku iz tvog app.py
        book_from_db = session.query(Book).filter_by(id=book_id).first()
        if book_from_db:
            book_from_db.price = nova_cijena
            session.commit()
            print(f"Cijena za '{book_from_db.title}' ažurirana na {nova_cijena}.")
        else:
            print(f"Knjiga s ID-om {book_id} nije pronađena.")

def obrisi_knjigu(book_id):
    """Briše knjigu na temelju ID-a."""
    with Session(engine) as session:
        # Koristimo DELETE logiku iz tvog app.py
        book_from_db = session.query(Book).filter_by(id=book_id).first()
        if book_from_db:
            session.delete(book_from_db)
            session.commit()
            print(f"Knjiga '{book_from_db.title}' obrisana.")
        else:
            print(f"Knjiga s ID-om {book_id} nije pronađena.")