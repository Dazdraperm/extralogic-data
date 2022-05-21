from config import DATABASE_URI

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


class DBWorker:
    def __init__(self):
        self.__engine = create_engine(DATABASE_URI, echo=True)
        self.__declarative_base = declarative_base()

    def init_db(self) -> None:
        self.__declarative_base.metadata.create_all(bind=self.__engine)

    def get_base(self):
        return self.__declarative_base
