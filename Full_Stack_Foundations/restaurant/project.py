from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/hello')
def helloWorld():
	return "Hello World"

@app.route("/restaurants/<int:restaurant_id>/")
def restaurantMenu(restaurant_id):
	items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)

	if (items.count() == 0):
		return "Restaurant id {0} not found".format(restaurant_id)
		return

	output = ""
	for i in items:
		print "item!"
		output += ReturnItemDescription(i)
		print output
	return output

@app.route("/restaurants/<int:restaurant_id>/new/")
def newMenuItem(restaurant_id):
	return "Page to create a new menu item. Restaurant: {0}. Task 1 complete!".format(restaurant_id)

@app.route("/restaurants/<int:restaurant_id>/edit/")
def editMenuItem(restaurant_id):
	return "Page to edit a menu item. Restaurant: {0}. Task 2 complete!".format(restaurant_id)

@app.route("/restaurants/<int:restaurant_id>/<int:menu_id>/delete/")
def deleteMenuItem(restaurant_id, menu_id):
	return "Page to delete a menu item. Restaurant: {0}. Menu Item: {1}. Task 3 complete!".format(restaurant_id, menu_id)

def ReturnItemDescription(item):
	output = ''
	output += item.name
	output += "</br>"
	output += item.price
	output += "</br>"
	output += item.description
	output += "</br>"
	output += "</br>"

	return output

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)