import logging
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_database():
    # Connect to PostgreSQL server
    conn = psycopg2.connect(
        host=settings.POSTGRES_SERVER,
        port=settings.POSTGRES_PORT,
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    
    try:
        with conn.cursor() as cursor:
            # Check if database exists
            cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (settings.POSTGRES_DB,))
            exists = cursor.fetchone()
            
            if not exists:
                logger.info(f"Creating database {settings.POSTGRES_DB}")
                cursor.execute(f"CREATE DATABASE {settings.POSTGRES_DB}")
                logger.info(f"Database {settings.POSTGRES_DB} created successfully")
            else:
                logger.info(f"Database {settings.POSTGRES_DB} already exists")
    except Exception as e:
        logger.error(f"Error creating database: {e}")
        raise
    finally:
        conn.close()

if __name__ == "__main__":
    create_database() 