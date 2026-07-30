from app.extensions import db
from app.models.account import Account
from app.models.transaction import Transaction


class AccountRepository:
    @staticmethod
    def create(account: Account):
        db.session.add(account)
        db.session.commit()
        return account

    @staticmethod
    def get_user_accounts(user_id: int):
        return Account.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_by_id(account_id: int):
        return Account.query.get(account_id)

    @staticmethod
    def add_transaction(transaction: Transaction):
        db.session.add(transaction)
        db.session.commit()
        return transaction
