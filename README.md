# BookZ - Aplikacija za upravljanje knjižarom

## Opis projekta

BookZ je konzolna aplikacija za upravljanje knjižarom razvijena u Pythonu koristeći SQLAlchemy ORM za rad s bazom podataka.

## Značajke

- **Pregled knjiga** - Prikaz svih knjiga s detaljima (autor, izdavač, cijena)
- **Dodavanje knjiga** - Unos novih knjiga u bazu
- **Ažuriranje cijene** - Izmjena cijene postojećih knjiga
- **Brisanje knjiga** - Uklanjanje knjiga iz baze podataka
- **Upravljanje autorima i izdavačima** - Automatsko dodavanje i povezivanje autora i izdavača

## Struktura projekta

```
BookZ/
├── main.py           # Glavni program s izbornicima
├── models.py         # SQLAlchemy modeli (Author, Publisher, Book)
├── repository.py     # CRUD funkcije za rad s bazom
├── requirements.txt  # Python zavisnosti
└── README.md         # Dokumentacija
```

## Instalacija

1. Instalirajte potrebne pakete:
```bash
pip install -r requirements.txt
```

2. Pokrenite aplikaciju:
```bash
python3 main.py
```

## Korištenje

Aplikacija nudi interaktivni izbornik s opcijama:

1. **Prikaz svih knjiga** - Prikazuje sve knjige u bazi
2. **Dodaj novu knjigu** - Unos nove knjige
3. **Ažuriraj cijenu knjige** - Promjena cijene postojeće knjige
4. **Obriši knjigu** - Brisanje knjige iz baze
0. **Izlaz** - Zatvaranje aplikacije

## Baza podataka

Aplikacija koristi SQLite bazu (`bookshop.db`) koja se automatski kreira pri prvom pokretanju.

### Modeli

- **Author** - Autor (ime, prezime)
- **Publisher** - Izdavač (naziv)
- **Book** - Knjiga (naslov, cijena, raspoloživost, autor, izdavač)

PostojiMany-to-Many veza između autora i izdavača putem pomoćne tablice `author_publisher`.

## Tehnologije

- Python 3
- SQLAlchemy (ORM)
- SQLite (baza podataka)
