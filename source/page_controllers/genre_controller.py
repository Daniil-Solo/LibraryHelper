from PyQt5.QtWidgets import QMessageBox

from services.genre_service import GenreService, InGenre


class GenreController:
    def __init__(self, application, ui, conn):
        self.application = application
        self.ui = ui
        self.conn = conn
        self.bind_methods()

        self.genre_service = GenreService(self.conn)
        self.genres = []
        self.current_genre = None
        self.is_new_genre_mode = None
        self.start_new_mode()

    def start_new_mode(self):
        self.is_new_genre_mode = True
        self.ui.deleteGenreBtn.setEnabled(False)

    def start_edit_mode(self):
        self.is_new_genre_mode = False
        self.ui.deleteGenreBtn.setEnabled(True)

    def bind_methods(self):
        self.ui.clearGenreSearchFieldBtn.clicked.connect(self.clear_search_genre_fields)
        self.ui.searchGenreBtn.clicked.connect(self.search_genre)
        self.ui.editSelectedGenreBtn.clicked.connect(self.edit_genre)
        self.ui.deleteGenreBtn.clicked.connect(self.delete_genre)
        self.ui.createNewGenreBtn.clicked.connect(self.create_new_genre)
        self.ui.saveGenreBtn.clicked.connect(self.save_genre)

    def clear_search_genre_fields(self):
        self.ui.searchGenreLineEdit.setText("")

    def search_genre(self):
        self.genres = self.genre_service.get_list_by_search_conditions(
            name=self.ui.searchGenreLineEdit.text()
        )
        self.update_genre_list()

    def update_genre_list(self):
        self.ui.genreList.clear()
        self.ui.genreList.addItems(
            [f"{genre.name} ({genre.id})" for genre in self.genres]
        )

    def clear_genre_form(self):
        self.ui.genreLineEdit.setText("")

    def create_new_genre(self):
        self.start_new_mode()
        self.clear_genre_form()

    def edit_genre(self):
        if not self.ui.genreList.selectedItems():
            QMessageBox.critical(
                self.application, "Ошибка", "Жанр не выбран", QMessageBox.Ok
            )
            return
        self.start_edit_mode()
        index = self.ui.genreList.currentRow()
        self.current_genre = self.genres[index]
        self.ui.genreLineEdit.setText(self.current_genre.name)

    def delete_genre(self):
        self.genre_service.delete(self.current_genre.id)
        self.genres = list(filter(lambda genre: genre.id != self.current_genre.id, self.genres))
        self.update_genre_list()
        self.current_genre = None
        self.clear_genre_form()
        QMessageBox.information(
            self.application, "Удаление завершено", "Жанр успешно удален", QMessageBox.Ok
        )

    def save_genre(self):
        new_name = self.ui.genreLineEdit.text()
        if self.is_new_genre_mode:
            genre = InGenre(
                name=new_name
            )
            self.genre_service.create(genre)
            self.clear_genre_form()
            QMessageBox.information(
                self.application, "Создание завершено", "Жанр успешно создан", QMessageBox.Ok
            )
        else:
            self.current_genre.name = new_name
            self.genre_service.update(self.current_genre)

            for (index, genre) in enumerate(self.genres):
                if genre.id == self.current_genre.id:
                    self.genres[index] = self.current_genre
                    break
            self.update_genre_list()

            self.clear_genre_form()
            self.current_genre = None
            self.start_new_mode()
            QMessageBox.information(
                self.application, "Редактирование завершено", "Данные о жанре успешно сохранены", QMessageBox.Ok
            )
