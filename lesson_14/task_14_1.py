from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///test1.db", echo=True)
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


Base.metadata.create_all(engine)


engine = create_engine("sqlite:///test1.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
session.add(Person('Alex', 'Sidorov'))
session.add_all([Person('Alex', 'Sidorov'), Person('Ann', 'Ivanova')])
session.commit()
person = session.query(Person).filter_by(firstname="Alex").first()
person = session.query(Person).filter(Person.firstname=="Alex").first()
#person = session.query(Person).filter(and(Person.firstname=="Alex",Person.lastname=="Sidorov",)).all()
print(person.firstname)