from flask import Flask,render_template,request,redirect,url_for
from data import generate_contacts
from contact import Contact
#create flask app
app = Flask(__name__)

#load dummy data
contact_book = generate_contacts()

@app.route('/contacts')
def list_contacts():
    return render_template('list-contacts.html', contacts = contact_book.get_contacts())


@app.route('/contact/add',methods = ['GET','POST'])
def add_contact():
    if request.method == 'GET':
        return render_template('add-contact.html')
    else:
        #read values from form
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        #create a new contact
        contact = Contact(first_name,last_name)
        
        #add contact to contact book
        contact_book.add_contact(contact)
        
        #redirect to contact list
        return redirect(url_for('list_contacts'))


    
@app.route('/contact/view/<int:id>')
def view_contact(id):
    print(id)
    contact = contact_book.get_contact(id)
    print (contact)
    return render_template('view-contact.html',contact= contact)
    