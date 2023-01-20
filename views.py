from models import *
from flask import *


app = Flask(__name__)
app.config['SECRET KEY'] = '123740981237401732907'


@app.route('/insert-data/', methods=['POST', 'GET'])
def insert_data():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        year = request.form['year']
        janr = request.form['janr']
        description = request.form['description']
        photo_url = request.form['photo_url']

        if not Book.select().where(Book.name == name):
            Book.create(name=name, author=author,year=year,janr=janr,description=description,photo_url=photo_url)
        else:
            return flash(f'Книга {name} уже существует', 'Warning')
    return render_template('insert.html')

@app.route('/')
def show_data():
    names = Book.select()
    # for i in English.select():
    #     print(i.id, i.word, i.translate)
    return render_template('index.html', names=names)

@app.route('/update/<int:id>', methods=['POST','GET'])
def update_data(id):
    datas = Book.get_by_id(id)
    if request.method == 'POST':
        name = request.form['name']
        name_upd = request.form['name_upd']
        year_upd = request.form['year_upd']
        janr_upd = request.form['janr_upd']
        description_upd = request.form['description_upd']
        photo_url_upd = request.form['photo_url_upd']

        query = Book.update(name=name, author=name_upd, year=year_upd, janr=janr_upd,description=description_upd,photo_url=photo_url_upd).where(Book.name==name)
        query.execute()
        return redirect('/')
    return render_template('update.html', datas=datas)
@app.route('/delete/<int:id>')
def delete_data(id):
    Book.delete_by_id(id)
    return redirect('/')

@app.route('/contact-data/', methods=['POST','GET'])
def contact():
        if request.method == 'POST':
            name_1 = request.form['name_1']
            email = request.form['email']
            phone_number = request.form['phone_number']
            passwd = request.form['passwd']
            passwd_1 = request.form['passwd_1']
            if not Contact.select().where(Contact.name_1 == name_1):
                Contact.create(name_1=name_1, email=email, phone_number=phone_number,passwd=passwd,passwd_1=passwd_1)
            else:
                return flash(f'Такой {name_1} уже существует', 'Warning')
        return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
