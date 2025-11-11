from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Boolean, Float, Table

# 1. KORAK - Priprema Base klase (kao u tvom app.py)
Base = declarative_base()

# 2. KORAK - Definicija Many-to-Many pomoćne tablice (zahtjev iz uputa [cite: 790])
# Ova tablica povezuje autore i izdavače
author_publisher_table = Table('author_publisher', Base.metadata,
    Column('author_id', Integer, ForeignKey('author.id'), primary_key=True),
    Column('publisher_id', Integer, ForeignKey('publisher.id'), primary_key=True)
)

# 3. KORAK - Definicija Modela (Klasa)

class Author(Base):
    __tablename__ = "author"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(length=150), nullable=False)
    last_name = Column(String(length=150), nullable=False)
    
    # Veze (Relationships)
    books = relationship("Book", back_populates="author")
    # Many-to-Many veza prema Izdavaču [cite: 790]
    publishers = relationship("Publisher", secondary=author_publisher_table, back_populates="authors")

    def __repr__(self):
        return f"ID: {self.id} | Author: {self.first_name} {self.last_name}"

class Publisher(Base):
    __tablename__ = "publisher"

    id = Column(Integer, primary_key=True, autoincrement=True)
    naziv = Column(String(length=250), nullable=False)

    # Veze (Relationships)
    books = relationship("Book", back_populates="publisher")
    # Many-to-Many veza prema Autoru [cite: 790]
    authors = relationship("Author", secondary=author_publisher_table, back_populates="publishers")

    def __repr__(self):
        return f"ID: {self.id} | Izdavač: {self.naziv}"

class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Atributi iz uputa [cite: 790]
    title = Column(String(length=250), nullable=False) # 'naziv'
    price = Column(Float, nullable=False)              # 'cijena'
    availability = Column(Boolean, default=True)       # 'raspoloživost'

    # Foreign Key (Vanjski ključevi)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)
    publisher_id = Column(Integer, ForeignKey("publisher.id"), nullable=False)
    
    # Veze (Relationships)
    author = relationship("Author", back_populates="books")
    publisher = relationship("Publisher", back_populates="books")

    def __repr__(self):
        return f"ID: {self.id} | Book: {self.title} | Cijena: {self.price}"

# 4. KORAK - Kreiranje Engine-a (kao u tvom app.py)
# Ovo će kreirati 'bookshop.db' datoteku
engine = create_engine("sqlite:///bookshop.db")

def init_database():
    """Kreira sve tablice u bazi (ako ne postoje)."""
    Base.metadata.create_all(engine)