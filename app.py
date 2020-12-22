from flask import Flask,render_template,request,redirect,url_for
from data import generate_contacts
from contact import Contact
from contact_book import ContactBook

#create flask app
app = Flask(__name__)

#load dummy data
contact_book = generate_contacts()

@app.route('/')
def users ():
    return render_template()

@app.route('/contacts')
def list_contacts():
    return render_template('list-contacts.html', contacts = contact_book.get_contacts(),url=url_for('add_contact'))


@app.route('/contact/add',methods = ['GET','POST'])
def add_contact():
    if request.method == 'GET':
        return render_template('add-contact.html')
    else:
        #read values from form
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        nick_name = request.form['nick_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        # favorite = request.form['value']
        # family = request.form['value']
        # friend = request.form['value']
        # work = request.form['value']
        #create a new contact
        contact = Contact(first_name.title(),last_name.title())
        contact.nickname = nick_name
        contact.phone_number = phone_number
        contact.email = email
        # contact.favorite = favorite
        # contact.family = family
        # contact.freind = friend
        # contact.work = work

        #add contact to contact book
        contact_book.add_contact(contact)
        
        #redirect to contact list
        return redirect(url_for('list_contacts'))



    
@app.route('/contact/view/<int:id>')
def view_contact(id):
    contact = contact_book.get_contact(id)
    return render_template('view-contact.html',contact= contact)
    

    
@app.route('/contactbook')
def view_contact_book():
    contacts=contact_book.get_contacts()
    return render_template('view-contact-book.html', contacts = contacts.values())
    
@app.route('/about')
def about():
    return render_template('about.html')

    
# @app.route('/remove/contact')
# def remove_contact():
#     contact = contact_book.get_contact(id)
#     contact_book.remove_contact(contact)
#     return redirect(url_for('list_contacts'))
