"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
q1 = db.session.query(Brand).get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
q2 = db.session.query(Model).filter_by(name='Corvette',brand_name='Chevrolet').all()

# Get all models that are older than 1960.
q3 = db.session.query(Model).filter(Model.year >1960).all()

# Get all brands that were founded after 1920.
q4 = db.session.query(Brand).filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
q5 = db.session.query(Model).filter(Model.name.like("%Cor%")).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
q6 = db.session.query(Brand).filter(Brand.founded == 1903 , Brand.discontinued == None).all()

# Get all brands with that are either discontinued or founded before 1950.
q7 = db.session.query(Brand).filter((Brand.founded < 1950)|(Brand.discontinued.isnot(None)).all()
# **query seemed to work but when I tried to call the object, i got this error:
# **"UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 28: ordinal not in range(128)"
# i think it has to do with the citroen word in Model table....


# Get any model whose brand_name is not Chevrolet.
q8 = db.session.query(Model).filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_brand = db.session.query(Model,Brand).join(Brand).filter(Model.year == year).all()

    for model, brand in model_brand:
        print model.name + " " + model.brand + " " + brand.headquarters

get_model_info(1950)

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brand_names = db.session.query(Brand,Model).join(Model).all()

    for brand, model in brand_names:
        print brand.name + " " + model.name

get_brands_summary()

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# this returns on list of objects, objects for the records with the brand name Ford


# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# an association table is a "middle man" table that just only needs data to connect two tables together.
# ie: has a primary key and two foreign keys for other tables
