import unittest

from app import create_app


class BankingApiTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app("development")
        self.client = self.app.test_client()

    def test_health_endpoint(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)

    def test_deposit_persists_balance(self):
        login_resp = self.client.post(
            "/api/auth/login",
            json={"email": "demo@banking.app", "password": "Password123!"},
        )
        token = login_resp.get_json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        response = self.client.post(
            "/api/transactions/deposit",
            json={"account_id": 1, "amount": 50},
            headers=headers,
        )

        self.assertEqual(response.status_code, 200)
        accounts_resp = self.client.get("/api/accounts", headers=headers)
        accounts = accounts_resp.get_json()["accounts"]
        self.assertGreaterEqual(accounts[0]["balance"], 1300)


if __name__ == "__main__":
    unittest.main()
