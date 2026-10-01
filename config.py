"""
Axion Ingestion Service - Configuration
Loads database connection string from environment variable.
"""

import os
from dataclasses import dataclass


@dataclass
class Settings:
    # PostgreSQL connection string
    # Format: postgresql://<user>:<password>@<host>:<port>/<database>
    # Example: postgresql://postgres:postgres@localhost:5432/axiondb
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://databaseadmin:Azure%40123456@postgre-axion-server.postgres.database.azure.com:5432/axion_db",
    )

settings = Settings()
