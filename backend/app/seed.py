from app.extensions import db
from app.models import Account, AuditLog, Beneficiary, Transaction, User
from app.services.auth_service import AuthService


def seed_database():
    user = User.query.filter_by(email="demo@banking.app").first()
    if not user:
        user = User(
            full_name="Demo Customer",
            email="demo@banking.app",
            password_hash=AuthService.hash_password("Password123!"),
            phone="555-0100",
            address="1 Market Street",
        )
        db.session.add(user)
        db.session.flush()
    else:
        user.password_hash = AuthService.hash_password("Password123!")
        user.full_name = "Demo Customer"
        user.phone = "555-0100"
        user.address = "1 Market Street"
        db.session.add(user)
        db.session.flush()

    account = Account.query.filter_by(user_id=user.id).first()
    if not account:
        account = Account(
            account_number="1000000001",
            user_id=user.id,
            account_type="checking",
            balance=1250.50,
        )
        db.session.add(account)
        db.session.flush()

    if not Transaction.query.filter_by(account_id=account.id).first():
        db.session.add(Transaction(account_id=account.id, user_id=user.id, transaction_type="deposit", amount=1250.50, description="Initial deposit"))
    if not Beneficiary.query.filter_by(user_id=user.id).first():
        db.session.add(Beneficiary(user_id=user.id, name="Jane Doe", account_number="1000000002", nickname="Jane"))
    if not AuditLog.query.filter_by(user_id=user.id).first():
        db.session.add(AuditLog(user_id=user.id, action="signup", details="Seeded demo account"))
    db.session.commit()
