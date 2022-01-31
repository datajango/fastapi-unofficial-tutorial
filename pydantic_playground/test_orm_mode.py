from typing import List
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, constr

def test_orm_mode():
    Base = declarative_base()

    class CompanyOrm(Base):
        __tablename__ = 'companies'
        id = Column(Integer, primary_key=True, nullable=False)
        public_key = Column(String(20), index=True, nullable=False, unique=True)
        name = Column(String(63), unique=True)
        domains = Column(ARRAY(String(255)))


    class CompanyModel(BaseModel):
        id: int
        public_key: constr(max_length=20)
        name: constr(max_length=63)
        domains: List[constr(max_length=255)]

        class Config:
            orm_mode = True


    co_orm = CompanyOrm(
        id=123,
        public_key='foobar',
        name='Testing',
        domains=['example.com', 'foobar.com'],
    )

    co_model = CompanyModel.from_orm(co_orm)

    assert co_model.id == 123
    assert co_model.name == 'Testing'
    assert co_model.public_key == 'foobar'
    assert co_model.domains == ['example.com', 'foobar.com']
