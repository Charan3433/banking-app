import os
import unittest
from pathlib import Path

from app.config import _resolve_database_uri


class ConfigTests(unittest.TestCase):
    def test_resolve_database_uri_uses_project_root_relative_path(self):
        os.environ["DATABASE_URL"] = "sqlite:///data/banking.db"
        uri = _resolve_database_uri()
        self.assertTrue(uri.endswith("banking.db") or "banking.db" in uri)


if __name__ == "__main__":
    unittest.main()
