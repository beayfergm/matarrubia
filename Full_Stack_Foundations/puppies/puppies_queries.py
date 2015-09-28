from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppies import Base, Shelter, Puppy
import datetime

engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)

session = DBSession()

def allPuppiesAlphabetically():
	"""
	1. Query all of the puppies and return the results in ascending alphabetical order
	"""
	puppies = session.query(Puppy).order_by(Puppy.name).all()
	result = [puppy.name for puppy in puppies]
	# print result


def allPuppiesLessThanNMonths(months=1):
	"""
	2. Query all of the puppies that are less than 6 months old organized by the youngest first
	"""
	# We assume that a month is approx 4 weeks
	six_months_ago = datetime.datetime.utcnow() - datetime.timedelta(weeks=months*4)
	puppies = session.query(Puppy).filter(Puppy.dateOfBirth > six_months_ago).order_by(Puppy.dateOfBirth.desc())
	result = [[puppy.name, puppy.dateOfBirth] for puppy in puppies]
	# print result


def allPuppiesByAscendingWeight():
	"""
	3. Query all puppies by ascending weight
	"""
	puppies = session.query(Puppy).order_by(Puppy.weight).all()
	result = [[puppy.name, int(puppy.weight)] for puppy in puppies]
	# print result


def allPuppiesGroupByShelter():
	"""
	4. Query all puppies grouped by the shelter in which they are staying
	"""
	puppies = session.query(Puppy).group_by(Puppy.shelter_id).all()
	result = [[puppy.name, puppy.shelter.name] for puppy in puppies]
	print result


def occupancyForShelterId(shelter_id):
	"""
	5. Output the current occupancy for the given shelter
	"""
	puppies_with_shelter = session.query(Puppy).filter(Puppy.shelter_id == shelter_id).all()
	result = [[puppy.name, puppy.shelter.name] for puppy in puppies_with_shelter]
	result = len(puppies_with_shelter);
	return result


if __name__ == '__main__':
	allPuppiesAlphabetically()
	allPuppiesLessThanNMonths(6)
	allPuppiesByAscendingWeight()
	allPuppiesGroupByShelter()
	occupancyForShelterId(1)



