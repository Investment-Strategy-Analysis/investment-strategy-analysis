from services.user_service.common.abstract import User
from services.user_service.db.user_db_impl import save_user as __save_user
from services.user_service.db.user_db_impl import get_user_by_login as __get_user_by_login
from services.user_service.db.user_db_impl import delete_user_by_login as __delete_user_by_login


def save_user(user: User):  # if it's a new user creates it.
    return __save_user(user)


def get_user_by_login(login: str) -> User:
    return __get_user_by_login(login)


def delete_user_by_login(login: str):
    return __delete_user_by_login(login)


def __small_example():
    a = User(login='a', password='pass')
    save_user(a)
    print(get_user_by_login(a.login))
    delete_user_by_login(a.login)
    print(get_user_by_login(a.login))


if __name__ == '__main__':
    __small_example()