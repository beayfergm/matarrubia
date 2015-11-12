from flask import Flask, render_template, request, redirect, url_for, flash
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

@app.route("/restaurants/<int:restaurant_id>/new/", methods = ['GET', 'POST'])
def newMenuItem(restaurant_id):
	if request.method == 'POST':
		newItem = MenuItem(name = request.form['name'], restaurant_id = restaurant_id)
		session.add(newItem)
		session.commit()
		flash("New Menu Item Created")
		return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
	else:
		return render_template('newmenuitem.html', restaurant_id = restaurant_id)

@app.route("/restaurants/<int:restaurant_id>/<int:menu_id>/edit/", methods = ['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
	if request.method == 'POST':
		existingMenuItem = 	session.query(MenuItem).filter_by(id = menu_id, restaurant_id = restaurant_id).one()
		oldName = existingMenuItem.name
		existingMenuItem.name = request.form['name']
		session.add(existingMenuItem)
		session.commit()
		flashText = "Menu Item Edited. Old Item name: {0}. New Item name: {1}".format(oldName, existingMenuItem.name)
		flash(flashText)
		return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
	else:
		existingMenuItem = 	session.query(MenuItem).filter_by(id = menu_id, restaurant_id = restaurant_id).one()
		return render_template('editmenuitem.html', restaurant_id = restaurant_id, menu_id = menu_id, item = existingMenuItem)

@app.route("/restaurants/<int:restaurant_id>/<int:menu_id>/delete/", methods = ['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
	if request.method == 'POST':
		existingMenuItem = 	session.query(MenuItem).filter_by(id = menu_id, restaurant_id = restaurant_id).one()
		deletedItemName = existingMenuItem.name
		session.delete(existingMenuItem)
		session.commit()
		flashText = "Menu Item Deleted. Item name: {0}".format(deletedItemName)
		flash(flashText)
		return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
	else:
		return render_template('deletemenuitem.html', restaurant_id = restaurant_id, menu_id = menu_id)

def RenderResponse(restaurant, items):
	return render_template('menu.html', restaurant = restaurant, items = items)

if __name__ == '__main__':
	app.debug = True
	app.secret_key = "super_secret_key"
	app.run(host = '0.0.0.0', port = 5000)