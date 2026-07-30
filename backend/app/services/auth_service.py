import hashlib
from datetime import datetime, timedelta
from typing import Optional

import bcrypt
import jwt
from flask import current_app

from app.models.user import User
from app.repositories.user_repository import UserRepository


class AuthService:
    @staticmethod
    def hash_password(password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        try:
            return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
        except ValueError:
            return hashlib.sha256(password.encode("utf-8")).hexdigest() == hashed_password

    @staticmethod
    def create_token(user: User) -> str:
        payload = {
            "sub": str(user.id),
            "email": user.email,
            "exp": datetime.utcnow() + timedelta(hours=current_app.config["JWT_EXPIRATION_HOURS"]),
        }
        return jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm=current_app.config["JWT_ALGORITHM"])

    @staticmethod
    def decode_token(token: str):
        return jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=[current_app.config["JWT_ALGORITHM"]])

    @staticmethod
    def register(full_name: str, email: str, password: str, phone: str = None, address: str = None):
        if UserRepository.get_by_email(email):
            raise ValueError("Email already registered")
        user = User(full_name=full_name, email=email, password_hash=AuthService.hash_password(password), phone=phone, address=address)
        return UserRepository.create(user)

    @staticmethod
    def login(email: str, password: str) -> Optional[dict]:
        user = UserRepository.get_by_email(email)
        if not user or not AuthService.verify_password(password, user.password_hash):
            return None
        return {
            "access_token": AuthService.create_token(user),
            "user": user.to_dict(),
        }

    @staticmethod
    def forgot_password(email: str):
        user = UserRepository.get_by_email(email)
        if not user:
            return False
        return True
