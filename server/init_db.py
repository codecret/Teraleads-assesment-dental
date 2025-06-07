import logging
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.core.config import settings
from app.services.auth import get_password_hash
from app.models.user import User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db(db: Session) -> None:
    # Create admin user
    admin = db.query(User).filter(User.email == "admin@example.com").first()
    if not admin:
        admin = User(
            email="admin@example.com",
            name="Admin User",
            hashed_password=get_password_hash("admin123"),
            is_active=True
        )
        db.add(admin)
        db.commit()
        logger.info("Created admin user")
    else:
        logger.info("Admin user already exists")

def main() -> None:
    logger.info("Creating initial data")
    db = SessionLocal()
    init_db(db)
    logger.info("Initial data created")

if __name__ == "__main__":
    main() 