from abc import ABC


class BaseModelService(ABC):
    TABLE_NAME = None
    IN_MODEL = None
    OUT_MODEL = None

    def __init__(self, conn):
        self.conn = conn

    @staticmethod
    def get_default_fields() -> dict:
        return {}

    def create(self, data: IN_MODEL) -> OUT_MODEL:
        """
        Создает новую запись в таблице TABLE_NAME c данными из полей data и полей по умолчанию
        """
        fields = {**data.__dict__, **self.get_default_fields()}
        field_names = fields.keys()

        query = f"insert into {self.TABLE_NAME}({','.join(field_names)})\n"
        query += f"values({','.join([f'%({field_name})s' for field_name in field_names])})\n"
        query += "returning id;"

        with self.conn.cursor() as cursor:
            cursor.execute(query, fields)
            data_id = cursor.fetchone()[0]
        out_data = self.OUT_MODEL(id=data_id, **fields)
        self.conn.commit()
        return out_data

    def delete(self, data_id: int) -> None:
        """
        Удаляет запись с id=data_id из таблицы TABLE_NAME
        """
        query = f"delete from {self.TABLE_NAME}\n"
        query += f"where id = %s;"

        with self.conn.cursor() as cursor:
            cursor.execute(query, (data_id,))
        self.conn.commit()

    def update(self, data: OUT_MODEL) -> OUT_MODEL:
        """
        Обновляет запись с id=data.id в таблице TABLE_NAME
        """
        fields = data.__dict__
        field_names = set(fields.keys())
        field_names.remove('id')

        query = f"update {self.TABLE_NAME}\n"
        query += "set\n"
        query += ',\n'.join([f'{field_name}=%({field_name})s' for field_name in field_names])
        query += "\nwhere id=%(id)s;"

        with self.conn.cursor() as cursor:
            cursor.execute(query, fields)
        self.conn.commit()
        return data
