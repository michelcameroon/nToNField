from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Association table for the many-to-many relationship
tb1_tb2 = db.Table('tb1_tb2',
    db.Column('tb1_id', db.Integer, db.ForeignKey('tb1.id'), primary_key=True),
    db.Column('tb2_id', db.Integer, db.ForeignKey('tb2.id'), primary_key=True)
)

class Tb1(db.Model):
    __tablename__ = 'tb1'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tb2s = db.relationship('Tb2', secondary=tb1_tb2, backref=db.backref('tb1s', lazy='dynamic'))

    def __repr__(self):
        return f'<Tb1 {self.name}>'

    def get_field_names():
        tb1_fields = [column.key for column in Tb1.__table__.columns]
        return tb1_fields

    def get_field_names_noIds():
        tb1_fields = [column.key for column in Tb1.__table__.columns]
        #tb1_fields = get_field_names()
        tb1_fields_noIds = [] 
        for tb1_field in tb1_fields:
            if  tb1_field != 'id':
                tb1_fields_noIds.append(tb1_field)
        return tb1_fields_noIds    





class Tb2(db.Model):
    __tablename__ = 'tb2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Tb2 {self.name}>'

    def get_field_names():
        tb2_fields = [column.key for column in Tb2.__table__.columns]
        return tb2_fields

    def get_field_names_noIds():
        tb2_fields = [column.key for column in Tb2.__table__.columns]
        #tb1_fields = get_field_names()
        tb2_fields_noIds = [] 
        for tb2_field in tb2_fields:
            if  tb2_field != 'id':
                tb2_fields_noIds.append(tb2_field)
        return tb2_fields_noIds    

