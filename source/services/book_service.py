import datetime
from dataclasses import dataclass

from services.base_service import BaseModelService
from services.book_genre_service import BookGenreService, InBookGenre, OutBookGenre
from services.genre_service import GenreService, OutGenre
from services.author_service import AuthorService, OutAuthor
from services.book_author_service import BookAuthorService, InBookAuthor, OutBookAuthor


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

    @staticmethod
    def get_default_fields() -> dict:
        return dict(register_date=datetime.date.today())

    @staticmethod
    def get_order_by() -> str:
        return "name"

    def get_genres(self, book_id: int) -> list[OutGenre]:
        bgs = BookGenreService(self.conn)
        return bgs.join(GenreService, 'genre_id', book_id=book_id)

    def add_genre(self, book_id: int, genre_id: int) -> OutBookGenre:
        bgs = BookGenreService(self.conn)
        book_genre = bgs.create(InBookGenre(book_id=book_id, genre_id=genre_id))
        return book_genre

    def remove_genre(self, book_id: int, genre_id: int) -> None:
        bgs = BookGenreService(self.conn)
        bgs.delete(book_id=book_id, genre_id=genre_id)

    def get_authors(self, book_id: int) -> list[OutAuthor]:
        bas = BookAuthorService(self.conn)
        return bas.join(AuthorService, 'author_id', book_id=book_id)

    def add_author(self, book_id: int, author_id: int) -> OutBookAuthor:
        bas = BookAuthorService(self.conn)
        book_author = bas.create(InBookAuthor(book_id=book_id, author_id=author_id))
        return book_author

    def remove_author(self, book_id: int, author_id: int) -> None:
        bas = BookAuthorService(self.conn)
        bas.delete(book_id=book_id, author_id=author_id)
