from typing import TypedDict

class UserType(TypedDict):
    name: str
    email: str
    age: int


def send_user(user: UserType) -> None:
    print(f"sending to {user['name']} at {user['email']}")


valid_user: UserType = {'name': 'yassir', 'email': 'example@mail.com', 'age': 22}
send_user(valid_user)