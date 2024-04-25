#!/usr/bin/python3
"""Defines the DBStorage engine."""
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session, sessionmaker
import sqlalchemy

class DBStorage:
    """
    database storage engine representation.

    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes new DBStorage instance.

        """
        username = getenv ("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")
        
        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(username, password, host, db_name) 

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the curret database session (self.__session)

        """
        list_obj = []
        
        if cls:
            if isinstance(cls, str):
                try:
                    cls = globals()(cls)
                except KeyError:
                    pass
            if issubclass(cls, Base):
                list_obj = self.__session.query(cls).all()
        else:
            for subclass in Base.__subclasses__():
                list_obj.extend(self.__session.query(subclass).all())

        obj_dict = {}
        
        for obj in list_obj:
            key = "{}.{}".format(obj.__class.__name__, obj.id)
            obj_dict[key] = obj
            try:
                if obj.__class__.__name__ == 'State':
                    del obj._sa_instance_state
                    obj_dict[key] = obj
                else:
                    obj_dict[key] = obj
            except Exception:
                pass
        return obj_dict

    
    def new(self, obj):
        """
        Add object to the current database session.

        """
        self.__session.add(obj)

    
    def save(self):
        """
        Commit all changes to the current database session.

        """
        self.__session.commit()

    
    def delete(self, obj=None):
        """
        Delete object from the current database session.

        """
        self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database
        initializes a new session.

        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
    
    #def close(self):
     #   """Close the working SQLAlchemy session."""
     #   self.__session.close()
