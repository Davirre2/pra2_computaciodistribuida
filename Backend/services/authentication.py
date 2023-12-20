from models.user import User
from exceptions.AuthException import AuthException
import hashlib
from jose import jwt
from models.tokendata import TokenData

class AuthService:
    
    def __init__(self, service_session) -> None:
        self.db = service_session

    def login(self, email: str, password: str):
        user = self.db.query(User).filter(User.email == email).first()
        if user is None:
            raise AuthException("El correu no existeix, subnormal")
        if not self.check_password(password, user.password):
            raise AuthException("Contrasenya incorrecta")
        if user.token == None:
            user.token=self.create_token(user)
            self.db.commit()
            self.db.refresh(user)
        return user.token

    def create_token(self, user: User):
        data = {'user_id' : user.id, 
                'email' : user.email, 
                'is_active' : user.is_active}
        token = jwt.encode(data, "tincmoltamoltasoninohepreselsantidepressiusencaraxd1234", "HS256")
        return token
        
        
    def check_token(self, token: str):
        data = jwt.decode(token.encode('utf-8'), "tincmoltamoltasoninohepreselsantidepressiusencaraxd1234", "HS256")
        user = self.db.query(User).filter(User.id == data['user_id']).filter(User.email == data['email']).first()
        if user is None:
            raise AuthException("Token incorrecte, bestie (aixeca cella)")
        if not data['is_active']:
            raise AuthException("L'usuari no està actiu")
        return TokenData(user_id = data['user_id'], email = data['email'], is_active = data["is_active"])

    def check_password(self, password: str, hashed_password: str):
        converted_pw = hashlib.sha256(password.encode('utf-8'))
        return converted_pw.hexdigest() == hashed_password