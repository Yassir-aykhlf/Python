from typing import NewType

UserId = NewType('UserId', int)

def get_user_by_id(user_id: UserId) -> None:
    print(f"Fetching for {user_id}")

valid_user_id: UserId = UserId(42)
invalid_user_id: int = 404

get_user_by_id(valid_user_id)
get_user_by_id(invalid_user_id) # "Literal[404]" is not assignable to "UserId"