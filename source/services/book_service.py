import datetime
from dataclasses import dataclass

from services.base_service import BaseModelService
from services.book_genre_service import BookGenreService, InBookGenre, OutBookGenre
from services.genre_service import GenreService, OutGenre


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

    def get_genres(self, book_id: int) -> list[OutGenre]:
        bgs = BookGenreService(self.conn)
        return bgs.join(GenreService, 'genre_id', book_id=book_id)

    def add_genre(self, book_id: int, genre_id: int) -> OutBookGenre:
        bgs = BookGenreService(self.conn)
        book_genre = bgs.create(InBookGenre(book_id=book_id, genre_id=genre_id))
        return book_genre

    def remove_genre(self, book_genre_id: int) -> None:
        bgs = BookGenreService(self.conn)
        bgs.delete(book_genre_id)
