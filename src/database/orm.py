from database_c import sync_engine, Base, Session_factory
from models import Answer
from sqlalchemy import insert


def create_table():
    # Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)


def insert_data():
    with Session_factory() as session:
        asnw = Answer(
            answer="Some Answer",
        )
        session.add(asnw)
        session.commit()



