from PyQt5.QtWidgets import QMessageBox

from services.author_service import AuthorService, InAuthor
from services.exceptions import UniqueException


class AuthorController:
    def __init__(self, application, ui, conn):
        self.application = application
        self.ui = ui
        self.conn = conn
        self.bind_methods()

        self.author_service = AuthorService(self.conn)
        self.authors = []
        self.current_author = None
        self.is_new_author_mode = None
        self.start_new_mode()

    def start_new_mode(self):
        self.is_new_author_mode = True
        self.ui.deleteAuthorBtn.setEnabled(False)

    def start_edit_mode(self):
        self.is_new_author_mode = False
        self.ui.deleteAuthorBtn.setEnabled(True)

    def bind_methods(self):
        self.ui.clearAuthorSearchFieldBtn.clicked.connect(self.clear_search_author_fields)
        self.ui.searchAuthorBtn.clicked.connect(self.search_author)
        self.ui.editSelectedAuthorBtn.clicked.connect(self.edit_author)
        self.ui.deleteAuthorBtn.clicked.connect(self.delete_author)
        self.ui.createNewAuthorBtn.clicked.connect(self.create_new_author)
        self.ui.saveAuthorBtn.clicked.connect(self.save_author)

    def clear_search_author_fields(self):
        self.ui.searchAuthorLineEdit.setText("")

    def search_author(self):
        self.authors = self.author_service.get_list_by_search_conditions(
            full_name=self.ui.searchAuthorLineEdit.text()
        )
        self.update_author_list()

    def update_author_list(self):
        self.ui.authorList.clear()
        self.ui.authorList.addItems(
            [f"{author.full_name} ({author.id})" for author in self.authors]
        )

    def clear_author_form(self):
        self.ui.authorLineEdit.setText("")

    def create_new_author(self):
        self.start_new_mode()
        self.clear_author_form()

    def edit_author(self):
        if not self.ui.authorList.selectedItems():
            QMessageBox.critical(
                self.application, "Ошибка", "Автор не выбран", QMessageBox.Ok
            )
            return
        self.start_edit_mode()
        index = self.ui.authorList.currentRow()
        self.current_author = self.authors[index]
        self.ui.authorLineEdit.setText(self.current_author.full_name)

    def delete_author(self):
        self.author_service.delete(self.current_author.id)
        self.authors = list(filter(lambda author: author.id != self.current_author.id, self.authors))
        self.update_author_list()
        self.current_author = None
        self.clear_author_form()
        QMessageBox.information(
            self.application, "Удаление завершено", "Автор успешно удален", QMessageBox.Ok
        )

    def save_author(self):
        new_full_name = self.ui.authorLineEdit.text()
        if self.is_new_author_mode:
            author = InAuthor(
                full_name=new_full_name
            )
            try:
                self.author_service.create(author)
            except UniqueException:
                QMessageBox.critical(
                    self.application, "Ошибка", "Автор с таким именем уже существует", QMessageBox.Ok
                )
                return
            self.clear_author_form()
            QMessageBox.information(
                self.application, "Создание завершено", "Автор успешно создан", QMessageBox.Ok
            )
        else:
            self.current_author.full_name = new_full_name
            try:
                self.author_service.update(self.current_author)
            except UniqueException:
                QMessageBox.critical(
                    self.application, "Ошибка", "Автор с таким именем уже существует", QMessageBox.Ok
                )
                return
            for (index, author) in enumerate(self.authors):
                if author.id == self.current_author.id:
                    self.authors[index] = self.current_author
                    break
            self.update_author_list()

            self.clear_author_form()
            self.current_author = None
            self.start_new_mode()
            QMessageBox.information(
                self.application, "Редактирование завершено", "Данные об авторе успешно сохранены", QMessageBox.Ok
            )
