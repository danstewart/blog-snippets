import re
from db import db
from sqlalchemy.orm import declared_attr, relationship
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey


def snake_caser(text):
    """
    Converts camelCase/PascalCase to snake_case
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()


# Base Models
class CustomBase(db.Base):
    """
    This is our customised base table
    It includes a table name generator that converts the ClassName to class_name
    an ID primary key column and a basic repr() method

    Any models that inherit from this will automatically get these things
    """
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return snake_caser(cls.__name__)

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.id}>'


class UserBase(CustomBase):
    __abstract__ = True

    label = ''

    # Columns
    name = Column(String(40))
    email = Column(String(120))

    # Relationship
    @declared_attr
    def posts(cls):
        return relationship(f'Post{cls.label}', backref=cls.__tablename__, lazy=True)


class PostBase(CustomBase):
    __abstract__ = True

    label = ''

    # Columns
    body = Column(Text(240))
    private = Column(Boolean)

    @declared_attr
    def user_id(cls):
        return Column(Integer, ForeignKey(f'user_{snake_caser(cls.label)}.id'))


# ProductA Models
class UserProductA(UserBase):
    """
    This extends the UserBase model so is a copy of that but with the table name user_product_a

    We can overwrite or extend however we want but the only the we NEED is to define the label
    The label should be cased the same as the class name
    """
    label = 'ProductA'


class PostProductA(PostBase):
    label = 'ProductA'
