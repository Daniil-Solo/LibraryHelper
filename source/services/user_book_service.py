import datetime
from dataclasses import dataclass
from services.base_middle_service import BaseMiddleModelService


@dataclass
class InUserBook:
    user_id: int
    book_id: int
    expected_return_date: datetime.date


@dataclass
class OutUserBook(InUserBook):
    id: int
    take_date: datetime.date
    real_return_date: datetime.date


class UserBookService(BaseMiddleModelService):
    TABLE_NAME = 'books_for_users'
    IN_MODEL = InUserBook
    OUT_MODEL = OutUserBook

    def get_default_fields(self) -> dict:
        return {
            "take_date": datetime.date.today(),
            "real_return_date": None
        }
