from app.models.account import Account
from app.models.transaction import Transaction
from app.repositories.account_repository import AccountRepository
from app.extensions import db


class AccountService:
    @staticmethod
    def create_account(user_id: int, account_type: str = "checking"):
        account = Account(
            account_number=AccountService._generate_account_number(),
            user_id=user_id,
            account_type=account_type,
            balance=0.0,
        )
        return AccountRepository.create(account)

    @staticmethod
    def _generate_account_number() -> str:
        import random

        return str(random.randint(1000000000, 9999999999))

    @staticmethod
    def deposit(account_id: int, amount: float, user_id: int):
        account = AccountRepository.get_by_id(account_id)
        if not account or account.user_id != user_id:
            raise ValueError("Account not found")
        account.balance = float(account.balance) + amount
        transaction = Transaction(account_id=account.id, user_id=user_id, transaction_type="deposit", amount=amount, description="Deposit")
        db.session.add(transaction)
        db.session.commit()
        return account

    @staticmethod
    def withdraw(account_id: int, amount: float, user_id: int):
        account = AccountRepository.get_by_id(account_id)
        if not account or account.user_id != user_id:
            raise ValueError("Account not found")
        if float(account.balance) < amount:
            raise ValueError("Insufficient funds")
        account.balance = float(account.balance) - amount
        transaction = Transaction(account_id=account.id, user_id=user_id, transaction_type="withdraw", amount=amount, description="Withdrawal")
        db.session.add(transaction)
        db.session.commit()
        return account

    @staticmethod
    def transfer(from_account_id: int, to_account_number: str, amount: float, user_id: int):
        from_account = AccountRepository.get_by_id(from_account_id)
        if not from_account or from_account.user_id != user_id:
            raise ValueError("Source account not found")
        to_account = Account.query.filter_by(account_number=to_account_number).first()
        if not to_account:
            raise ValueError("Destination account not found")
        if float(from_account.balance) < amount:
            raise ValueError("Insufficient funds")
        from_account.balance = float(from_account.balance) - amount
        to_account.balance = float(to_account.balance) + amount
        db.session.add(Transaction(account_id=from_account.id, user_id=user_id, transaction_type="transfer", amount=amount, description="Transfer out", related_account=to_account.account_number))
        db.session.add(Transaction(account_id=to_account.id, user_id=to_account.user_id, transaction_type="transfer", amount=amount, description="Transfer in", related_account=from_account.account_number))
        db.session.commit()
        return from_account
