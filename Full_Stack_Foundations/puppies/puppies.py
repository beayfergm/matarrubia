from sqlalchemy import Table, Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
	__tablename__ = 'shelter'
	id = Column (Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	address = Column(String(250))
	city = Column(String(80))
	state = Column(String(20))
	zipCode = Column(String(10))
	website = Column(String)
	maximum_capacity = Column(Integer)


class Puppy(Base):
	__tablename__ = 'puppy'
	id = Column (Integer, primary_key = True)
	name = Column (String(80), nullable = False)
	gender = Column(String(6), nullable = False)
	dateOfBirth = Column (Date)
	picture = Column(String)
	breed = Column (String(30))
	weight = Column(Numeric(10))
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	shelter = relationship(Shelter)


class PuppyProfile(Base):
	__tablename__ = 'puppy_profile'
	id = Column (Integer, primary_key = True)
	picture = Column(String)
	description = Column(String(250))
	special_needs = Column(String(250))
	puppy_id = Column(Integer, ForeignKey('puppy.id'))
	puppy = relationship(Puppy)


puppy_adopters = Table('puppy_adopters', Base.metadata,
    Column('puppy_id', Integer, ForeignKey('puppy.id')),
    Column('adopter_id', Integer, ForeignKey('adopter.id'))
)


class Adopter(Base):
	__tablename__ = 'adopter'
	id = Column (Integer, primary_key = True)
	description = Column(String(250))
	puppies = relationship(Puppy,
		                    secondary=puppy_adopters,
		                    backref="adopters")


engine = create_engine('sqlite:///puppyshelter.db')


Base.metadata.create_all(engine)



