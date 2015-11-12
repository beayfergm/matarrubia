from flask import Flask, render_template
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
	restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)

	if (items.count() == 0):
		return "Restaurant id {0} not found".format(restaurant_id)
		return

	output = RenderResponse(restaurant, items)
	return output

@app.route("/restaurants/<int:restaurant_id>/new/")
def newMenuItem(restaurant_id):
	return "Page to create a new menu item. Restaurant: {0}. Task 1 complete!".format(restaurant_id)

@app.route("/restaurants/<int:restaurant_id>/<int:menu_id>/edit/")
def editMenuItem(restaurant_id, menu_id):
	return "Page to edit a menu item. Restaurant: {0}. Menu Item: {1}. Task 2 complete!".format(restaurant_id, menu_id)

@app.route("/restaurants/<int:restaurant_id>/<int:menu_id>/delete/")
def deleteMenuItem(restaurant_id, menu_id):
	return "Page to delete a menu item. Restaurant: {0}. Menu Item: {1}. Task 3 complete!".format(restaurant_id, menu_id)

def RenderResponse(restaurant, items):
	return render_template('menu.html', restaurant = restaurant, items = items)

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)