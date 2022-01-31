import typing
from pydantic import BaseModel, Field, error_wrappers
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

def test_reserved_names():
    class MyModel(BaseModel):
        metadata: typing.Dict[str, str] = Field(alias='metadata_')

        class Config:
            orm_mode = True

    BaseModel2 = declarative_base()

    class SQLModel(BaseModel2):
        __tablename__ = 'my_table'
        id = sa.Column('id', sa.Integer, primary_key=True)
        # 'metadata' is reserved by SQLAlchemy, hence the '_'
        metadata_ = sa.Column('metadata', sa.JSON)


    sql_model = SQLModel(metadata_={'key': 'val'}, id=1)

    pydantic_model = MyModel.from_orm(sql_model)

    assert pydantic_model.metadata['key'] == 'val'

    #> {'metadata': {'key': 'val'}}
    #print(pydantic_model.dict(by_alias=True))
    #> {'metadata_': {'key': 'val'}}