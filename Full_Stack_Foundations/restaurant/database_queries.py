from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)

session = DBSession()

def getAllRestaurants():
	'''Returns a list with the name of all existing restaurants'''
	restaurants = session.query(Restaurant).all()
	return restaurants

def getHTMLContentWithRestaurantList(restaurants):
	output = ""
	for restaurant in restaurants:
		output += "<div> %s" % (restaurant.name)
		output += "</br>"
		output += "<a href=/restaurants/%s/edit>Edit</a>" % (restaurant.id)
		output += "</br>"
		output += "<a href=/restaurants/%s/delete>Delete</a>" % (restaurant.id)
		output += "</div>"
		output += "</br>"
	return output

def addRestaurant(name):
	new_restaurant = Restaurant(name=name)
	session.add(new_restaurant)
	session.commit()

def updateRestaurantName(id, new_name):
	restaurant_to_update = session.query(Restaurant).filter_by(id = id).one()
	restaurant_to_update.name = new_name;
	session.add(restaurant_to_update)
	session.commit()

def deleteRestaurant(id):
	restaurant_to_remove = session.query(Restaurant).filter_by(id = id).one()
	session.delete(restaurant_to_remove)
	session.commit()

def testQueries():
	# Shows all the Veggie Burgers
	items = session.query(MenuItem).filter_by(name = "Veggie Burger")
	itemnames = [[item.id, item.restaurant.name, item.price] for item in items]
	print 'There are {0} Menu Items with the name Veggie Burger'.format(len(itemnames))

	# Updates a unique instance of the Veggie Burger
	menuItemToUpdate = session.query(MenuItem).filter_by(id = 12).one()
	menuItemToUpdate.price = '$2.99'
	session.add(menuItemToUpdate)
	session.commit()
	print menuItemToUpdate.restaurant.name +"'s "+ menuItemToUpdate.name + "'s price has been updated"

	# Updates all the Veggie Burgers
	for item in items:
		item.price = '$2.99'
		session.add(item)
		session.commit()
	print "All Veggie Burger prices have been updated to $2.99"

	# Deletes a single item
	menuItemToDelete = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
	session.delete(menuItemToDelete)
	session.commit()