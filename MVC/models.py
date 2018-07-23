from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


class Usuario(BaseModel, db.Model):
    """Model for the usuario table"""
    __tablename__ = 'usuario'

    nombre = db.Column(db.String())
    direccion = db.Column(db.String())
    keyid = db.Column(db.String(), primary_key=True)

    def _to_dict(self):
        _dict = self.__dict__

        for f in ['keyid', '_sa_instance_state']:
            _dict.pop(f, None)

        # Convert datetimes for JSON
        for k in _dict.keys():
            if type(_dict[k]) == datetime.datetime:
                _dict[k] = str(_dict[k])


        return _dict