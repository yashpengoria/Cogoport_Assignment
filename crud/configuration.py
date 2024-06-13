from sqlalchemy.orm import Session
from models.configuration import Configuration
from schemas.configuration import ConfigurationCreate, ConfigurationUpdate

def create_configuration(db: Session, config: ConfigurationCreate):
    db_config = Configuration(**config.dict())
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config

def get_configuration(db: Session, country_code: str):
    return db.query(Configuration).filter(Configuration.country_code == country_code).first()

def update_configuration(db: Session, config: ConfigurationUpdate):
    db_config = db.query(Configuration).filter(Configuration.country_code == config.country_code).first()
    if db_config:
        db_config.onboarding_requirements = config.onboarding_requirements
        db.commit()
        db.refresh(db_config)
    return db_config

def delete_configuration(db: Session, country_code: str):
    db_config = db.query(Configuration).filter(Configuration.country_code == country_code).first()
    if db_config:
        db.delete(db_config)
        db.commit()
    return db_config
