class TokenData:
    user_id: int
    email: str
    is_active: bool

    def __init__(self, user_id: int, email: str, is_active: bool):
        self.user_id = user_id
        self.email = email
        self.is_active = is_active