import datetime
from dataclasses import dataclass

from services.base_service import BaseModelService


@dataclass
class InBook:
    name: str


@dataclass
class OutBook(InBook):
    id: int
    register_date: datetime.date


class BookService(BaseModelService):
    TABLE_NAME = 'books'
    IN_MODEL = InBook
    OUT_MODEL = OutBook

    def get_default_fields(self) -> dict:
        return dict(register_date=datetime.date.today())
