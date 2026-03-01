from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str

    def __post_init__(self) -> None:
        if '@' not in self.email:
            raise ValueError("Invalid email")

bad_user = User("Bob", "bob_at_example.com")
