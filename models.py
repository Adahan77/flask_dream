from peewee import *


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase('book.db')

class Book(BaseModel):
    id = PrimaryKeyField(null=True)
    name = CharField(max_length=100)
    author = CharField(max_length=100)
    year = CharField(max_length=100)
    janr = CharField(max_length=100)
    description = TextField()
    photo_url = CharField()

    class Meta:
        db_table = 'book'


class BaseModel1(Model):
    class Meta:
        database = SqliteDatabase('contact.db')

class Contact(BaseModel1):
    id = PrimaryKeyField(null=True)
    name_1 = CharField(max_length=100)
    email = CharField(max_length=100)
    phone_number = CharField(max_length=50)
    passwd = CharField(max_length=100)
    passwd_1 = CharField(max_length=100)

    class Meta:
        db_table = 'contact'

if __name__ == '__main__':
    Book.create_table()
    Contact.create_table()