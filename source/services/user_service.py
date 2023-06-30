import datetime
from dataclasses import dataclass
from services.base_service import BaseModelService


@dataclass
class InUser:
    firstname: str
    lastname: str
    middlename: str
    phone: str


@dataclass
class OutUser(InUser):
    id: int
    register_date: datetime.date


class UserService(BaseModelService):
    TABLE_NAME = 'users'
    IN_MODEL = InUser
    OUT_MODEL = OutUser

    @staticmethod
    def get_default_fields() -> dict:
        return dict(register_date=datetime.date.today())

    @staticmethod
    def get_order_by() -> str:
        return "lastname, firstname, middlename"
