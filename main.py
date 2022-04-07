from flask import Flask, render_template
import util

app = Flask(__name__)

username = 'raywu1990'
password = 'test'
host = '127.0.0.1'
port ='5432'
database='dvdrental'

@app.route("/api/update_basket_a")

def update_basket_a():
	cursor,connection = util.connect_to_db(username, password, host, port, database)
	status = util.insert_row(cursor)
	util.disconnect_from_db(connection,cursor)
	return render_template('update.html', log_html = status)

@app.route("/api/unique")

def unique():
	cursor,connection = util.connect_to_db(username, password, host, port, database)

	status, data = util.unique(cursor)
	col_names = None
	log = None
	is_error = data is None
	if data is not None:
		col_names = [desc[0] for desc in cursor.description]       
		log = data[:]
		

	util.disconnect_from_db(connection,cursor)

	return render_template('unique.html', sql_table = log, table_title = col_names, is_error = is_error)

if __name__ == '__main__':
	app.debug = True
	ip = '127.0.0.1'
	app.run(host=ip)
