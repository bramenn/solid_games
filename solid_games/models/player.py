import uuid


class Player:
    id: str
    nickname: str
    points: int = 0

    is_host: bool

    def __init__(self, nickname: str, is_host: bool = False) -> None:
        self.id = uuid.uuid4()
        self.nickname = nickname
        self.is_host = is_host
