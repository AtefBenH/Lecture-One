from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base ()

class Person (Base) :
    __tablename__ = "people"

    id = Column ("id", Integer, primary_key=True)
    firstname = Column ("firstname", String)
    lastname = Column ("lastname", String)
    gender = Column ("gender", CHAR)
    age = Column ("age", Integer)

    def __init__(self, id, firstname, lastname, gender, age) :
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self) :
        return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender}, {self.age})"
    
engine = create_engine('mysql+mysqlconnector://<root>:<>@<localhost>:<3306>/<datatest.db>')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

    
p1 =Person (182508, "Atef", "Ben Hasnaoui", "M", 38)
p2 =Person (257890, "Amira", "Tarhouni", "F", 37)
p3 =Person (746358, "Elon", "Musk", "M", 59)
p4 =Person (238476, "Alma", "Ben Hasnaoui", "F", 5)

session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)

session.commit()
