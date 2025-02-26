from flask import Flask, render_template, request, redirect, url_for
from models import db, Tb1, Tb2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school11.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#@app.before_first_request
@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    tb1fieldNamesNoIds = Tb1.get_field_names_noIds()
    tb2fieldNamesNoIds = Tb2.get_field_names_noIds()
    print ('tb1fieldNamesNoIds')
    print (tb1fieldNamesNoIds)

    tb1s = Tb1.query.all()
    #students = Student.query.all()
    #courses = Course.query.all()
    tb2s = Tb2.query.all()
    return render_template('index.html', tb1s=tb1s, tb2s=tb2s, tb1fieldNamesNoIds=tb1fieldNamesNoIds, tb2fieldNamesNoIds=tb2fieldNamesNoIds )

@app.route('/add_tb1', methods=['POST'])
def add_tb1():
    tb1fieldNamesNoIds = Tb1.get_field_names_noIds()
    data = {tb1fieldNamesNoId: request.form[tb1fieldNamesNoId] for tb1fieldNamesNoId in tb1fieldNamesNoIds}
    print ('data')
    print (data)
    new_tb1 = Tb1(**data)
    db.session.add(new_tb1)

    #name = request.form.get('name')
    #new_tb1 = Tb1(name=name)
    #db.session.add(new_tb1)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_tb2', methods=['POST'])
def add_tb2():
    tb2fieldNamesNoIds = Tb2.get_field_names_noIds()

    name = request.form.get('name')
    new_tb2 = Tb2(name=name)
    db.session.add(new_tb2)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/enroll_tb1', methods=['POST'])
def enroll_tb1():
    tb1fieldNamesNoIds = Tb1.get_field_names_noIds()
    tb2fieldNamesNoIds = Tb2.get_field_names_noIds()

    tb1_id = request.form.get('tb1_id')
    tb2_id = request.form.get('tb2_id')
    tb1 = Tb1.query.get(tb1_id)
    tb2 = Tb2.query.get(tb2_id)
    if tb1 and tb2:
        tb1.tb2s.append(tb2)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
