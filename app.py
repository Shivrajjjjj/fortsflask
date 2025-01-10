''''
from flask import Flask, render_template, request, redirect, url_for, session

app =Flask(__name__)

@app.route('/')
def welcome():
    return render_template("aboutus.html")

if __name__ == "__main__":
    app.run()

@app.route('/aboutus',methods=['GET','POST'])
def aboutus():
    return render_template("aboutus.html")

@app.route('/place',methods=['GET','POST'])
def place():
    return render_template("place.html")

@app.route('/contact',methods=['GET','POST'])
def contact():
    return render_template("contact.html")
'''



    

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
  
  
app = Flask(__name__)
  
  
app.secret_key = 'xyzsdfg'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'shivraj'
app.config['MYSQL_DB'] = 'dbforts'
  
mysql = MySQL(app)
@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/aboutus', methods =['GET','POST'])
def aboutus():
    return render_template('aboutus.html')

@app.route('/place', methods=['GET','POST'])
def place():
    return render_template('place.html')


@app.route('/hotels',methods=['GET','POST'])
def hotels():
    return render_template('hotels.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'lname' in request.form and 'addr' in request.form and 'cont' in request.form and 'email' in request.form and 'message' in request.form:
        name = request.form['name']
        lname = request.form['lname']
        addr=request.form['addr']
        cont=request.form['cont']
        email = request.form['email']
        message=request.form['message']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM contact WHERE name = % s And lname = % s And addr = % s And cont = % s And email = % s And message = % s', (name,lname,addr,cont,email,message, ))
        if contact:
                 
                 cursor.execute('INSERT INTO contact VALUES (NULL, % s, % s, % s,% s, % s, % s)', (name,lname, email, addr,cont,message ))
                 mysql.connection.commit()
                 mesage = 'Your respond successfully submitted !'
        else :
                mesage = 'Please fill out the form !'

    return render_template('contact.html')

@app.route('/raigad' ,methods=['GET','POST'])
def raigad():
    return render_template('raigad.html')

@app.route('/shivneri',methods=['GET','POST'])
def shivneri():
    return render_template('shivneri.html')

@app.route('/purandar',methods=['GET','POST'])
def purandar():
    return render_template('purandar.html')

@app.route('/rajgad',methods=['GET','POST'])
def rajgad():
    return render_template('rajgad.html')

@app.route('/Sinhgad',methods=['GET','POST'])
def Sinhgad():
    return render_template('Sinhgad.html')

@app.route('/rajmachi',methods=['GET','POST'])
def rajmachi():
    return render_template('rajmachi.html')

@app.route('/vishalgad',methods=['GET','POST'])
def vishalgad():
    return render_template('vishalgad.html')

@app.route('/torna',methods=['GET','POST'])
def torna():
    return render_template('torna.html')

@app.route('/panhala',methods=['GET','POST'])
def panhala():
    return render_template('panhala.html')

@app.route('/lohgad',methods=['GET','POST'])
def lohgad():
    return render_template('lohgad.html')

@app.route('/sindhudurg',methods=['GET','POST'])
def sindhudurg():
    return render_template('sindhudurg.html')

@app.route('/harishchandrgad',methods=['GET','POST'])
def harishchandrgad():
    return render_template('harishchandrgad.html')



@app.route('/login',methods=['GET','POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['lname']=user['lname']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('index.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route('/register',methods=['GET','POST'])
def register():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not userName or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO user VALUES (NULL, % s, % s, % s)', (userName, email, password, ))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('register.html', mesage = mesage)


@app.route('/heritagehotel',methods=['GET','POST'])
def heritagehotel():
    return render_template('heritagehotel.html')

@app.route('/heritageimage',methods=['GET','POST'])
def heritageimage():
    return render_template('heritageimage.html')

@app.route('/booking',methods=['GET','POST'])
def booking():
    if request.method == 'POST' and 'phone' in request.form and 'txtfname' in request.form and 'txtlname' in request.form and 'txtphone' in request.form and 'txtaddress' in request.form and 'txtmail' in request.form and 'txthotel' in request.form and 'txtadult' in request.form and 'txtchild' in request.form and 'txtroom' in request.form and 'room' in request.form and 'txtdate' in request.form and 'txtdte' in request.form:
        phone=request.form['phone']
        fname=request.form['txtfname']
        lname=request.form['txtlname']
        phone=request.form['txtphone']
        address=request.form['txtaddress']
        email=request.form['txtemail']
        hotel=request.form['txthotel']
        adult=request.form['txtadult']
        child=request.form['txtchild']
        room=request.form['txtroom']
        roomtype=request.form['room']
        txtdate=request.form['date']
        txtdte=request.form['dte']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM booking WHERE phone = % s', (phone, ))
        result = cursor.fetchone()
        if result:
            msg = 'Phone number already exist !'
        else:
            cursor.executed('INSERT INTO booking values ( NULL , % s, % s, % s , % s, % s, % s , % s, % s, % s, % s, % s, % s )',
                        (fname,lname,phone,address,email,hotel,adult,child,room,roomtype,txtdate,txtdte))
            mysql.connection.commit()
            msg='Booking Sucessfully !'
    else:
        msg = 'please fill out the form !'
    return render_template('booking.html',msg= msg)

@app.route('/receipt',methods=['GET','POST'])
def receipt():
     mesage = ''
     if request.method == 'POST' and 'phone' in request.form and 'fname' in request.form and 'lname' in request.form and 'addrs' in request.form and 'email' in request.form and 'hotel' in request.form and 'adult' in request.form and 'childrn' in request.form and 'room' in request.form and 'roomtype' in request.form and 'checkin' in request.form and 'checkout' in request.form:
        phone= request.form['phone']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM booking WHERE phone = % s', (phone, ))
        result = cursor.fetchone()
        if result:
            session['loggedin']= True
            session['fname']= result['fname']
            session['lname']= result['lname']
            session['phone']= result['phone']
            session['addrs']= result['addrs']
            session['email']= result['email']
            session['hotel']= result['hotel']
            session['adult']= result['adult']
            session['childrn']= result['childrn']
            session['room']= result['room']
            session['roomtype']= result['roomtype']
            session['checkin']= result['checkin']
            session['checkout']= result['checkout']

            message ='passed !'
            return render_template('bill.html',mesage=mesage)
        else:
            message = 'please enter correct number !'
        return render_template('receipt.html',message=message) 
        

@app.route('/bill',methods=['GET','POST'])
def bill():
    return render_template('bill.html')

@app.route('/cancel',methods=['GET','POST'])
def cancel():
    session.pop('loggedin', None)
    session.pop('fname', None)
    session.pop('lname', None)
    session.pop('mobno', None)
    session.pop('hotel', None)
    session.pop('adult', None)
    session.pop('children', None)
    session.pop('room', None)
    session.pop('roomtype', None)
    session.pop('cindate', None)
    session.pop('coutdate', None)
    session.pop('noofdays', None)
    session.pop('totalbill', None)
    return redirect(url_for('booking'))

@app.route('/billing',methods=['GET','POST'])
def billing():
    if request.method == 'POST' and 'phone' in request.form:
        phone=request.form['phone']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM checkoutbill WHERE phone = % s', (phone, ))

        result = cursor.fetchone()

        if result:
             session['loggedin'] = True
             session['fname']=result['fname']
             session['lname']=result['lname']
             session['mobno']=result['mobno']
             session['hotel']=result['hotel']
             session['adult']=result['adult']
             session['children']=result['children']
             session['room']=result['room']
             session['roomtype']=result['roomtype']
             session['cindate']=result['cindate']
             session['coutdate']=result['coutdate']
             session['noofdays']=result['noofdays']
             session['totalbill']=result['totalbill']

             message= 'passed !'
             return render_template('billingpdf.html',message= message)
        else:
            message='please enter correct phone number !'
    return render_template('billing.html')

@app.route('/billingpdf',methods=['GET','POST'])
def billingpdf():
    return render_template('billingpdf.html')    
@app.route('/raigadpics',methods=['GET','POST'])
def raigadpics():
    return render_template('raigadpics.html')
@app.route('/rajgadpics',methods=['GET','POST'])
def rajgadpics():
    return render_template('rajgadpics.html')
@app.route('/rajmachipics',methods=['GET','POST'])
def rajmachipics():
    return render_template('rajmachipics.html')


@app.route('/shivneripics',methods=['GET','POST'])
def shivneripics():
    return render_template('shivneripics.html')

@app.route('/sinhgadpics',methods=['GET','POST'])
def sinhgadpics():
    return render_template('sinhgadpics.html')
@app.route('/vishalgadpics',methods=['GET','POST'])
def vishalgadpics():
    return render_template('vishalgadpics.html')

@app.route('/tornapics',methods=['GET','POST'])
def tornapics():
    return render_template('tornapics.html')

@app.route('/panhalapics',methods=['GET','POST'])
def panhalapics():
    return render_template('panhalapics.html')

@app.route('/lohgadpics',methods=['GET','POST'])
def lohgadpics():
    return render_template('lohgadpics.html')

@app.route('/sindhudurgpics',methods=['GET','POST'])
def sindhudurgpics():
    return render_template('sindhudurgpics.html')

@app.route('/harishchandrgadpics',methods=['GET','POST'])
def harishchandrgadpics():
    return render_template('harishchandrgadpics.html')

@app.route('/Sinhgadpics',methods=['GET','POST'])
def Sinhgadpics():
    return render_template('Sinhgadpics.html')

@app.route('/purandarpics',methods=['GET','POST'])
def purandarpics():
    return render_template('purandarpics.html')

@app.route('/ritzhotelimage',methods=['GET','POST'])
def ritzhotelimage():
    return render_template('ritzhotelimage.html')

@app.route('/ritzhotel',methods=['GET','POST'])
def ritzhotel():
    return render_template('ritzhotel.html')

@app.route('/Cozyhotel',methods=['GET','POST'])
def Cozyhotel():
    return render_template('Cozyhotel.html')
@app.route('/Cozyhotelimage',methods=['GET','POST'])
def Cozyhotelimage():
    return render_template('Cozyhotelimage.html')
@app.route('/woodhotelimage',methods=['GET','POST'])
def woodhotelimage():
    return render_template('woodhotelimage.html')
@app.route('/woodhotel',methods=['GET','POST'])
def woodhotel():
    return render_template('Woodshotel.html')

@app.route('/nearpune',methods=['GET','POST'])
def nearpune():
    return render_template('nearpune.html')

@app.route('/nearpuneimage',methods=['GET','POST'])
def nearpuneimage():
    return render_template('nearpuneimage.html')

@app.route('/whiteimage',methods=['GET','POST'])
def whiteimage():
    return render_template('whiteimage.html')

@app.route('/whitehotel',methods=['GET','POST'])
def whitehotel():
    return render_template('whitehotel.html')


@app.route('/Blissshotel',methods=['GET','POST'])
def Blissshotel():
    return render_template('Blissshotel.html')

@app.route('/Blisssimage',methods=['GET','POST'])
def Blisssimage():
    return render_template('Blisssimage.html')

@app.route('/Acreshotel',methods=['GET','POST'])
def Acreshotel():
    return render_template('Acreshotel.html')

@app.route('/Acresimage',methods=['GET','POST'])
def Acresimage():
    return render_template('Acresimage.html')
@app.route('/payment',methods=['GET','POST'])
def payment():
    return render_template('payment.html')
@app.route('/paymentbill',methods=['GET','POST'])
def paymentbill():
    return render_template('payment.html')
@app.route('/paymentreceipt',methods=['GET','POST'])
def paymentreceipt():
    return render_template('paymentreceipt.html')

@app.route('/portal',methods=['GET','POST'])
def portal():
    return render_template('portal.html')

@app.route('/portalbooking',methods=['GET','POST'])
def portalbooking():
    return render_template('portalbooking.html')

@app.route('/portalcancel',methods=['GET','POST'])
def portalcancel():
    return render_template('portalcancel.html')

@app.route('/portalbill',methods=['GET','POST'])
def portalbill():
    return render_template('portalbill.html')

@app.route('/portalpayments',methods=['GET','POST'])
def portalpayments():
    return render_template('portalpayments.html')

@app.route('/portalmodify',methods=['GET','POST'])
def portalmodify():
    return render_template('portalmodify.html')

@app.route('/portalcheckout',methods=['GET','POST'])
def portalcheckout():
    return render_template('portalcheckout.html')
@app.route('/portalsignout',methods=['GET','POST'])
def portalsignout():
    return render_template('portalsignout.html')

@app.route('/portalsignin',methods=['GET','POST'])
def portalsignin():
    return render_template('portalsignin.html')


if __name__ == "__main__":
    app.run()
