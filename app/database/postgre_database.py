from flask.ext.sqlalchemy import SQLAlchemy

class Db_test(db.Model):

    __tablename__ = "test"
    t_id = db.Column("id", db.Integer, primary_key=True)
    t_name = db.Column("name", db.String(50))
    t_value = db.Column("value", db.Integer)
    t_quality = db.Column("quality", db.String(15))