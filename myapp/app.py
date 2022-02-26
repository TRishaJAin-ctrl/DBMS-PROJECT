'''
#app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
 
app = Flask(__name__)
#app.secret_key = "cairocoders-ednalan"
 
DB_HOST = "localhost"
DB_NAME = "vehicle_renting"
DB_USER = "postgres"
DB_PASS = "postgres"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
 
@app.route('/', methods=['GET','POST'])
def Index():
	return render_template('index.html')


@app.route('/show_vehicle', methods=['GET','POST'])
def show_available():
	cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	if request.method == 'POST':
		start_date = request.form['start_date']
		end_date = request.form['end_date']
		s = "select vehicle_type, model_type, company_name, mileage, color, rental_price, seats from vehicle where ((Available_from <= (%s) and Available_till >= (%s)) or (Available_from >= (%s) and Available_till <= (%s)))"
		cur.execute(s, (start_date, end_date, start_date, end_date))
		list_user = cur.fetchall()
		cur.close()
		print(list_user[0])
	return render_template('show_vehicle.html', list_users = list_user)


if __name__ == "__main__":
    app.run(debug=True)
'''
# Store this code in 'app.py' file

from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import re
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your secret key'

DB_HOST = "localhost"
DB_NAME = "vehicle_renting"
DB_USER = "postgres"
DB_PASS = "postgres"

 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

conn_customer = psycopg2.connect(dbname=DB_NAME, user='customer', password='1000', host=DB_HOST)
conn_driver = psycopg2.connect(dbname=DB_NAME, user='driver', password='1000', host=DB_HOST)
conn_owner= psycopg2.connect(dbname=DB_NAME, user='owner', password='1000', host=DB_HOST)
conn_employee = psycopg2.connect(dbname=DB_NAME, user='employee', password='1000', host=DB_HOST)


@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		user_type = request.form['user_type']
		cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
		if user_type == "accounts_customer":
			#cursor = conn_customer.cursor(cursor_factory=psycopg2.extras.DictCursor)
			cursor.execute('SELECT * FROM accounts_customer WHERE username = %s AND password = %s', (username, password, ))
		elif user_type == "accounts_owner":
			#cursor = conn_owner(cursor_factory=psycopg2.extras.DictCursor)
			cursor.execute('SELECT * FROM accounts_owner WHERE username = %s AND password = %s', (username, password, ))
		elif user_type == "accounts_driver":
			#cursor = conn_driver(cursor_factory=psycopg2.extras.DictCursor)
			cursor.execute('SELECT * FROM accounts_driver WHERE username = %s AND password = %s', (username, password, ))
		else:
			#cursor = conn_employee(cursor_factory=psycopg2.extras.DictCursor)
			cursor.execute('SELECT * FROM accounts_employee WHERE username = %s AND password = %s', (username, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			session['id'] = account['id']
			session['username'] = account['username']
			msg = 'Logged in successfully !'
			if user_type == "accounts_customer":
				print('Inside customer if part')
				msg1 = ''
				c_fname, c_lname = session['username'].split()
				cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
				s = 'select p_id as PaymentID, advance as total_paid, balance from trip, payment, customer where trip.c_id = customer.c_id and trip.p_id = payment.payment_id and customer.c_fname = %s and customer.c_lname = %s and payment.balance > 0.00'
				cursor.execute(s, (c_fname, c_lname,))
				payment_list = cursor.fetchall()
				print('In index customer')
				return render_template('index_customer.html', msg = msg, msg1 = msg1, payment_list = payment_list)
			elif user_type == "accounts_employee":
				return render_template('index_employee.html', msg = msg)
			elif user_type == "accounts_driver":
				msg1 = ''
				d_fname, d_lname = session['username'].split()
				cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
				cursor.execute('select d_id from driver where d_fname = %s and d_lname = %s', (d_fname, d_lname))
				d_id = cursor.fetchall()
				print('Im here')
				if(len(d_id) == 0):
					msg1 = 'Please update your profile and login again!'
					print('IN if')
					info_list = []
				else:
		 			cursor.execute('select r_from, r_till, c_phno, c_fname, c_lname from trip, customer where trip.d_id = %s and trip.c_id = customer.c_id', (d_id[0]))
		 			info_list = cursor.fetchall()
		 			print('info_list')
				return render_template('index_driver.html', msg = msg, msg1 = msg1, info_list = info_list)
			else:
				return render_template('index_owner.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))
	
@app.route('/index1', methods=['GET','POST'])
def Index():
	return render_template('index1.html')
	
@app.route('/contact', methods=['GET','POST'])
def contact():
	office_list = []
	cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	if request.method == 'POST':
		office_name = request.form['office_name']
		s = 'select office.branch_id, office_name, office_addr, branch_phno from office, office_phno where office.branch_id = office_phno.branch_id and office_name = (%s)'
		cur.execute(s, (office_name,))
		office_list = cur.fetchall()	
	return render_template('contact.html', office_list = office_list)
	
@app.route('/verify/<username>', methods=['GET','POST'])
def verify(username):
	e_fname, e_lname = username.split()
	e = 'select e_id from employee where e_fname = %s and e_lname = %s'
	cur = conn_employee.cursor(cursor_factory=psycopg2.extras.DictCursor)
	cur.execute(e, (e_fname, e_lname))
	e_id = cur.fetchall()
	e_id = e_id[0][0]
	customer_list = []
	driver_list = []
	owner_list = []
	c = 'select c_id, c_fname, c_lname, c_dob, c_addr, c_emailid, c_phno, c_license from customer where e_id IS NULL'
	cur = conn_employee.cursor(cursor_factory=psycopg2.extras.DictCursor)
	cur.execute(c)
	customer_list = cur.fetchall()
	d = 'select d_id, d_fname, d_lname, d_dob, d_addr, d_phno, d_license from driver where e_id IS NULL'
	cur = conn_employee.cursor(cursor_factory=psycopg2.extras.DictCursor)
	cur.execute(d)
	driver_list = cur.fetchall()
	o = 'select o_id, o_fname, o_lname, o_dob, o_addr, o_emailid, o_phno from v_owner where e_id IS NULL'
	cur = conn_employee.cursor(cursor_factory=psycopg2.extras.DictCursor)
	cur.execute(o)
	owner_list = cur.fetchall()
	return render_template('verify.html', customer_list = customer_list, owner_list = owner_list, driver_list = driver_list, e_id = e_id)	
	
@app.route('/verified/<userid>/<eid>', methods=['GET','POST'])
def verified(userid, eid):
	user_type = userid[:2]
	print(user_type)
	print(eid)
	if user_type == 'OW':
		print('owner')
		o = 'update v_owner set e_id = %s where o_id = %s'
		cur = conn_employee.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cur.execute(o, (eid, userid))
		conn_employee.commit()	
	elif user_type == 'DR':
		print('driver')
		d = 'update driver set e_id = %s where d_id = %s'
		cur = conn_employee.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cur.execute(d, (eid, userid))
		conn_employee.commit()
	else:
		print('customer')
		c = 'update customer set e_id = %s where c_id = %s'
		cur = conn_employee.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cur.execute(c, (eid, userid))
		conn_employee.commit()
	return redirect(url_for('index_employee'))	
	
@app.route('/show_vehicle', methods=['GET','POST'])
def show_available():
	list_user = []
	msg = ''
	cur = conn_customer.cursor(cursor_factory=psycopg2.extras.DictCursor)
	if request.method == 'POST':
		start_date = request.form['start_date']
		end_date = request.form['end_date']
		if 'rental_price' in request.form and 'vehicle_type' in request.form:
			rental_price = request.form['rental_price']
			vehicle_type = request.form['vehicle_type']
			s = "select distinct v_number, vehicle_type, model_type, company_name, mileage, color, rental_price, seats from vehicle where ((Available_from <= (%s)) and (Available_till >= (%s))) and v_number not in (select distinct v_no from trip where (trip.r_from < (%s)) and (trip.r_till > (%s))) and (vehicle_type = (%s)) and (rental_price <= (%s))"
			cur.execute(s, (start_date, end_date, end_date, start_date, vehicle_type, rental_price))
			list_user = cur.fetchall()
			cur.close()
		#print(list_user[0])
		if 'v_number' in request.form and 'c_id' in request.form:
			cursor = conn_customer.cursor(cursor_factory=psycopg2.extras.DictCursor)
			v_number = request.form['v_number']
			c_id = request.form['c_id']
			if('driver' in request.form):
				driver = request.form['driver']
			else:
				driver = 0
			print(driver)
			#see if c_id exists
			#c = 'select count(*) from customer where c_id = %s'
			print(c_id)
			c_id = str(c_id)
			cursor.execute("select count(*) from Customer where Customer.c_id = %s", (c_id,))
			count = cursor.fetchall()
			#cursor.close()
			if(count[0] == 0):
				msg = 'Update Profile!'
			else:
				e = 'select e_id from customer where c_id = %s'
				cursor.execute(e, (c_id,))
				id = cursor.fetchall()
				cursor.close()
				if(len(id) == 0):
					msg = 'Please wait until you are verified!'
				else:
					#p_id
					s = 'select count(*) from Payment'
					cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
					cursor.execute(s)
					count = cursor.fetchall()
					#cursor.close()
					for row in count:
						fcount = row[0] + 1
					paymentid = 'PY'
					paymentid += str(fcount)
					payment_id = paymentid
					p = 'select rental_price from Vehicle where v_number = %s'
					cursor.execute(p, (v_number,))
					price = cursor.fetchall()
					price = price[0]
					print(price[0])
					start_day = start_date.split()[0]
					end_day = end_date.split()[0]
					start_day = start_day[:10]
					end_day = end_day[:10]
					#total_time = end_day - start_day
					#days = total_time.days
					date_format = "%Y-%m-%d"
					a = datetime.strptime(start_day, date_format)
					b = datetime.strptime(end_day, date_format)
					delta = b - a
					days = delta.days
					#print(int(end_date - start_date))
					#total_time = end_date - start_date
					balance = days * price
					advance = '0.00'
					payment_date = start_date.split()[0]
					payment_date = payment_date[:10]
					i = 'INSERT INTO Payment values(%s, NULL, %s, %s, %s)'
					cursor.execute(i, (payment_id, payment_date, advance, balance[0]))
					conn.commit()
					msg = 'Booked successfully!'
					print(driver)
					driver = int(driver)
					d = 'update driver set c_id = NULL where d_id in (select d_id from trip where r_till < CURRENT_DATE and d_id not in (select d_id from trip where r_till >= CURRENT_DATE))'
					cursor.execute(d)
					conn.commit()
					#d_id
					if (driver == 1):
						d = 'select d_id from Driver where c_id IS NULL and e_id IS NOT NULL ORDER BY random() LIMIT 1'
						cursor.execute(d)
						driverid = cursor.fetchall()
						if(len(driverid) == 0):
							print('In no did')
							msg = 'No available drivers!'
							return render_template('show_vehicle.html', list_users = list_user, msg = msg)
						else:
							d_id = driverid[0]
							u = 'UPDATE Driver SET c_id = %s WHERE d_id = %s'
							cursor.execute(u, (c_id, d_id[0]))
							conn.commit()
							i = "INSERT into Trip values(%s, %s, %s, %s, %s, %s)"
							cursor.execute(i, (start_date, end_date, c_id, v_number, payment_id, d_id[0]))
							conn.commit()
							msg = 'Booked successfully!'
					else:
						print("In else part")
						i = "INSERT into Trip(r_from, r_till, c_id, v_no, p_id) values(%s, %s, %s, %s, %s)"
						cursor.execute(i, (start_date, end_date, c_id, v_number, payment_id))
						conn.commit()
						msg = 'Booked successfully!'
					cursor.close()				
	return render_template('show_vehicle.html', list_users = list_user, msg = msg)	
	
@app.route('/index_owner')
def index_owner():
	return render_template('index_owner.html')	
	
@app.route('/index_customer')
def index_customer():
	print('Inside customer if part')
	msg1 = ''
	c_fname, c_lname = session['username'].split()
	cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	s = 'select p_id as PaymentID, advance as total_paid, balance from trip, payment, customer where trip.c_id = customer.c_id and trip.p_id = payment.payment_id and customer.c_fname = %s and customer.c_lname = %s and payment.balance > 0.00'
	cursor.execute(s, (c_fname, c_lname,))
	payment_list = cursor.fetchall()
	print('In index customer')
	return render_template('index_customer.html', msg1 = msg1, payment_list = payment_list)
	
@app.route('/index_employee')
def index_employee():
	return render_template('index_employee.html')	
'''	
@app.route('/book/<v_number>', methods = ['POST', 'GET'])
def book(v_number):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM students WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', student = data[0])	
 '''   
@app.route('/payment', methods = ['GET', 'POST'])
def payment():
	msg = ''
	print('Outside if')
	if request.method == 'POST' and 'p_id' in request.form and 'payment_method' in request.form and 'amount' in request.form and 'transaction_id' in request.form:
		print('inside if')
		if('rating' in request.form):
			rating = request.form['rating']
		p_id = request.form['p_id']
		payment_method = request.form['payment_method']
		amount = request.form['amount']
		transaction_id = request.form['transaction_id']
		if(rating != 'NA'):
			s = 'select d_id from trip where p_id  = (%s)'
			cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
			cur.execute(s, (p_id,))
			d_idlist = cur.fetchall()
			rating = str(rating)
			if(len(d_idlist)):
				d_id = d_idlist[0][0]
				d_id = str(d_id)
				d = 'update driver set rating = (rating + (%s))/2 where d_id = (%s)'
				cur.execute(d, (rating, d_id))
				conn.commit()
		msg = 'Taken Input'
		s = 'update payment set balance = balance - %s where payment_id = %s'
		cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cur.execute(s, (amount, p_id))
		conn.commit()
		msg = 'Updated balance'
		s =	'update payment set advance = advance + %s where payment_id = %s'
		cur.execute(s, (amount, p_id))
		conn.commit()
		msg = 'Updated advance'
		s =	'update payment set payment_date = CURRENT_DATE where payment_id = %s'
		cur.execute(s, (p_id,))
		conn.commit()
		msg = 'Payment Successful!'
	return render_template('payment.html', msg = msg)
	

@app.route('/index_driver', methods = ['GET', 'POST'])
def index_driver():
	print('Inside function')
	msg = ''
	driver_fullname = session['username']
	print(driver_fullname)
	d_fname, d_lname = session['username'].split()
	cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	cursor.execute('select d_id from driver where d_fname = %s and d_lname = %s', (d_fname, d_lname))
	d_id = cursor.fetchall()
	d_id = d_id[0][0]
	print('Im here')
	if(len(d_id) == 0):
		msg = 'Please update your profile!'
		print('IN if')
	else:
		 cursor.execute('select r_from, r_till, c_phno, c_fname, c_lname from trip, customer where trip.d_id = %s and trip.c_id = customer.c_id', (d_id,))
		 info_list = cursor.fetchall()
		 print('info_list')
	return render_template('index_driver.html', msg = msg, info_list = info_list)	
	
@app.route('/owner_add_vehicle', methods = ['GET', 'POST'])
def owner_add_vehicle():
	msg = ''
	if request.method == 'POST' and 'v_number' in request.form and 'vehicle_type' in request.form and 'model_type' in request.form and 'company_name' in request.form and 'seats' in request.form and 'o_id' in request.form and 'o_phno' in request.form:
		cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
		o_id = request.form['o_id']
		o_phno = request.form['o_phno']
		v_number = request.form['v_number']
		vehicle_type = request.form['vehicle_type']
		company_name = request.form['company_name']
		model_type = request.form['model_type']
		mileage = request.form['mileage']
		color = request.form['color']
		available_from = request.form['available_from']
		available_till = request.form['available_till']
		seats = request.form['seats']
		rental_price = int(seats) * 300 
		
		print(o_phno)
		
		if(len(v_number) == 0 or len(vehicle_type) == 0 or len(model_type) == 0 or len(company_name) == 0 or len(seats) == 0 or len(o_id) == 0 or len(o_phno) == 0):
			msg = 'Please update profile!'
		else:
			cursor.execute('select o_phno from v_owner where o_id = %s', (o_id,))
			phoneno = cursor.fetchall()
			for row in phoneno:
				phno = phoneno[0]
			print(phno)
			if(phno[0] == o_phno):
				cursor.execute('INSERT INTO Vehicle values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (v_number, o_id, vehicle_type, model_type, company_name, mileage, color, rental_price, available_from, available_till, seats, ))
				conn.commit()
				msg = "Vehicle added successfully!"
			else:
				msg = "Vehicle  not added!"				
	elif request.method == 'POST':
		msg = 'Please update profile!'
	return render_template('owner_add_vehicle.html', msg = msg)

	
@app.route('/profile_owner', methods = ['GET', 'POST'])
def profile_owner():
	msg = ''
	print(session)
	if request.method == 'POST' and 'o_fname' in request.form and 'o_lname' in request.form and 'o_phno' in request.form:
		o_fname = request.form['o_fname']
		o_lname = request.form['o_lname']
		o_phno = request.form['o_phno']
		o_emailid = request.form['o_emailid']
		o_addr = request.form['o_addr']
		o_dob = request.form['o_dob']
		s = 'select count(*) from V_Owner'
		cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(s)
		count = cursor.fetchall()
		for row in count:
			fcount = row[0] + 1
		ownerid = 'OW'
		ownerid += str(fcount)
		o_id = ownerid
		cursor.execute('SELECT * FROM V_Owner WHERE o_phno = %s', (o_phno,))
		account = cursor.fetchone()
		if account:
			msg = 'Profile already exists!'
		else:
			cursor.execute('INSERT INTO V_Owner(o_id, o_fname, o_lname, o_dob, o_addr, o_emailid, o_phno) values(%s, %s, %s, %s, %s, %s, %s)', (o_id, o_fname, o_lname, o_dob, o_addr, o_emailid, o_phno ))
			conn.commit()
			msg = "Profile updated successfully!"
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
		print(session)
	return render_template('profile_owner.html', msg = msg)
	
@app.route('/profile_customer', methods = ['GET', 'POST'])
def profile_customer():
	msg = ''
	if request.method == 'POST' and 'c_fname' in request.form and 'c_lname' in request.form and 'c_phno' in request.form:
		c_fname = request.form['c_fname']
		c_lname = request.form['c_lname']
		c_phno = request.form['c_phno']
		c_emailid = request.form['c_emailid']
		c_addr = request.form['c_addr']
		c_dob = request.form['c_dob']
		c_license = request.form['c_license']
		s = 'select count(*) from Customer'
		cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(s)
		count = cursor.fetchall()
		for row in count:
			fcount = row[0] + 1
		customerid = 'CU'
		customerid += str(fcount)
		c_id = customerid
		cursor.execute('SELECT * FROM Customer WHERE c_phno = %s', (c_phno,))
		account = cursor.fetchone()
		if account:
			msg = 'Profile already exists!'
		else:
			cursor.execute('INSERT INTO Customer(c_id, c_fname, c_lname, c_dob, c_addr, c_emailid, c_phno, c_license) values(%s, %s, %s, %s, %s, %s, %s, %s)', (c_id, c_fname, c_lname, c_dob, c_addr, c_emailid, c_phno, c_license ))
			conn.commit()
			msg = "Profile updated successfully!"
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
		print(session)
	return render_template('profile_customer.html', msg = msg)

@app.route('/profile_driver', methods = ['GET', 'POST'])
def profile_driver():
	msg = ''
	if request.method == 'POST' and 'd_fname' in request.form and 'd_lname' in request.form and 'd_phno' in request.form and 'd_license' in request.form:
		d_fname = request.form['d_fname']
		d_lname = request.form['d_lname']
		d_phno = request.form['d_phno']
		d_addr = request.form['d_addr']
		d_dob = request.form['d_dob']
		d_license = request.form['d_license']
		s = 'select count(*) from Driver'
		cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(s)
		count = cursor.fetchall()
		for row in count:
			fcount = row[0] + 1
		driverid = 'DR'
		driverid += str(fcount)
		d_id = driverid
		cursor.execute('INSERT INTO Driver(d_id, d_fname, d_lname, d_dob, d_addr, d_phno, d_payment, d_license) values(%s, %s, %s, %s, %s, %s, 0.00, %s)', (d_id, d_fname, d_lname, d_dob, d_addr, d_phno, d_license))
		conn.commit()
		msg = "Profile updated successfully!"
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
		print(session)
	return render_template('profile_driver.html', msg = msg)

@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		user_type = request.form['user_type']
		cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
		if user_type == "accounts_customer":
			cursor.execute('SELECT * FROM accounts_customer WHERE username = %s', (username, ))
		elif user_type == "accounts_owner":
			cursor.execute('SELECT * FROM accounts_owner WHERE username = %s', (username, ))
		elif user_type == "accounts_driver":
			cursor.execute('SELECT * FROM accounts_driver WHERE username = %s', (username, ))
		else:
			cursor.execute('SELECT * FROM accounts_employee WHERE username = %s', (username, ))
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'Username must contain only characters and numbers !'
		elif not username or not password or not email:
			msg = 'Please fill out the form !'
		else:
			if user_type == "accounts_customer":
				cursor.execute('INSERT INTO accounts_customer(username, password, email) VALUES (%s, %s, %s)', (username, password, email, ))
			elif user_type == "accounts_owner":
				cursor.execute('INSERT INTO accounts_owner(username, password, email) VALUES (%s, %s, %s)', (username, password, email, ))
			elif user_type == "accounts_driver":
				cursor.execute('INSERT INTO accounts_driver(username, password, email) VALUES (%s, %s, %s)', (username, password, email, ))
			else:
				cursor.execute('INSERT INTO accounts_employee(username, password, email) VALUES (%s, %s, %s)', (username, password, email, ))
			conn.commit()
			msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg)

if __name__ == "__main__":
    app.run(debug=True)