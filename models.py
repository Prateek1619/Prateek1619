from datetime import datetime
from .app import db
import re

class DEFdata(db.Model):
    __tablename__ = 'DEF'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    instance = db.Column(db.String(128),nullable=False)
    master = db.Column(db.String(64),nullable=False)
    location_x = db.Column(db.Float, nullable=False)
    location_y = db.Column(db.Float, nullable=False)
    valid = db.Column(db.Boolean)
    comment = db.Column(db.String(512))
    

    @classmethod
    def find_masters(cls):
        """ Description
        It just returns all the unique masters from DB. 
        """    
        #return cls.query.filter_by(is_valid=False).all()
        retval = []
        try: 
            masters = cls.query.with_entities(DEFdata.master).distinct()
            for master in masters:
                temp = str(master)
                print(temp)
                x = re.sub("[(),'']",'', temp)
                print(x)
                retval.append(x)
        except Exception as e:
            print(e)
        finally:
            return retval

    @classmethod
    def get_x_and_y(cls, master):
        """ Description
        It just returns all x and y co-ordinates. 
        """   
        def description(x,y):
            return { 'x': x , 'y': y} 
        #return cls.query.filter_by(is_valid=False).all()
        retval = []
        try: 
            coordinates = cls.query.with_entities(DEFdata.location_x, DEFdata.location_y).filter_by(master=master).all()
            for x, y in coordinates:
                retval.append(description(x,y))
            
        except Exception as e:
            print(e)
        finally:
            return retval

    def add(self):
        db.session.add(self)    
        db.session.commit()
        

class file_insertion(db.Model):
    __tablename__ = 'file'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(128),nullable=False)
    date = db.Column(db.Date, nullable=False)
    processes = db.Column(db.Boolean)

    def add(self):
        db.session.add(self)    
        db.session.commit()
