insert into
	genres(name)
values
	('Научная фантастика'),
	('Ужасы'),
	('Биография'),
	('Учебная литература');

insert into books(name, register_date)
values('Цветы для Элджернона', '2023-06-23');
insert into genres_for_books(genre_id, book_id)
values(1, 1);
insert into authors(full_name)
values('Дэниел Киз');
insert into authors_for_books(author_id, book_id)
values(1, 1);

insert into books(name, register_date)
values('Жук в муравейнике', '2023-06-23');
insert into genres_for_books(genre_id, book_id)
values(1, 2);
insert into authors(full_name)
values('Аркадий Стругацкий');
insert into authors(full_name)
values('Борис Стругацкий');
insert into authors_for_books(author_id, book_id)
values(2, 2);
insert into authors_for_books(author_id, book_id)
values(3, 2);

insert into books(name, register_date)
values('Понедельник начинается в субботу', '2023-06-23');
insert into genres_for_books(genre_id, book_id)
values(1, 3);
insert into authors_for_books(author_id, book_id)
values(2, 3);
insert into authors_for_books(author_id, book_id)
values(3, 3);

insert into books(name, register_date)
values('Сияние', '2023-06-23');
insert into genres_for_books(genre_id, book_id)
values(2, 4);
insert into authors(full_name)
values('Стивен Кинг');
insert into authors_for_books(author_id, book_id)
values(4, 4);

insert into books(name, register_date)
values('Оно', '2023-06-23');
insert into genres_for_books(genre_id, book_id)
values(2, 5);
insert into authors_for_books(author_id, book_id)
values(4, 5);

insert into books(name, register_date)
values('Зов Ктулху', '2023-06-23');
insert into genres_for_books(genre_id, book_id)
values(2, 6);
insert into authors(full_name)
values('Говард Лавкрафт');
insert into authors_for_books(author_id, book_id)
values(5, 6);

insert into books(name, register_date)
values('Дагон', '2023-06-23');
insert into genres_for_books(genre_id, book_id)
values(2, 7);
insert into authors_for_books(author_id, book_id)
values(5, 7);

insert into books(name, register_date)
values('Стив Джобс', '2023-06-23');
insert into genres_for_books(genre_id, book_id)
values(3, 8);
insert into authors(full_name)
values('Уолтер Айзексон');
insert into authors_for_books(author_id, book_id)
values(6, 8);

insert into books(name, register_date)
values('Как уличный кот изменил мою жизнь', '2023-06-23');
insert into genres_for_books(genre_id, book_id)
values(3, 9);
insert into authors(full_name)
values('Джеймс Боуэн');
insert into authors_for_books(author_id, book_id)
values(7, 9);

insert into books(name, register_date)
values('Чистый код: создание, анализ и рефакторинг', '2023-06-23');
insert into genres_for_books(genre_id, book_id)
values(4, 10);
insert into authors(full_name)
values('Роберт Мартин');
insert into authors_for_books(author_id, book_id)
values(8, 10);

insert into books(name, register_date)
values('Чистая архитектура. Искусство разработки программного обеспечения', '2023-06-23');
insert into genres_for_books(genre_id, book_id)
values(4, 11);
insert into authors_for_books(author_id, book_id)
values(8, 11);

insert into
	users(firstname, lastname, middlename, phone, register_date)
values
	('Пелагея', 'Третьякова', 'Антоновна', '+7 (930) 786-71-62', '2023-05-01'),
	('Конкордия', 'Сафарова', 'Федоровна', '+7 (994) 924-97-77', '2023-03-02'),
	('Никон', 'Шин', 'Макарович', '+7 (982) 239-83-34', '2023-05-02'),
	('Клара', 'Вихирева', 'Николаевна', '+7 (913) 499-23-78', '2023-05-06');

insert into
	books_for_users(user_id, book_id, take_date, expected_return_date, real_return_date)
values
	(1, 1, '2023-06-23', '2023-07-07', NULL),
	(1, 2, '2023-06-23', '2023-07-07', NULL),
	(2, 3, '2023-05-12', '2023-05-26', NULL),
	(3, 4, '2023-05-02', '2023-05-16', '2023-05-14'),
	(3, 5, '2023-05-02', '2023-05-16', '2023-05-18'),
	(4, 6, '2023-06-01', '2023-06-15', '2023-06-20');