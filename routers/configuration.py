from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import get_db
from schemas.configuration import ConfigurationCreate, ConfigurationUpdate, ConfigurationResponse
from crud.configuration import create_configuration, get_configuration, update_configuration, delete_configuration

router = APIRouter()

@router.post("/create_configuration", response_model=ConfigurationResponse)
def create_config(config: ConfigurationCreate, db: Session = Depends(get_db)):
    db_config = get_configuration(db, config.country_code)
    if db_config:
        raise HTTPException(status_code=400, detail="Configuration already exists")
    return create_configuration(db, config)

@router.get("/get_configuration/{country_code}", response_model=ConfigurationResponse)
def read_config(country_code: str, db: Session = Depends(get_db)):
    db_config = get_configuration(db, country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config

@router.post("/update_configuration", response_model=ConfigurationResponse)
def update_config(config: ConfigurationUpdate, db: Session = Depends(get_db)):
    db_config = update_configuration(db, config)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config

@router.delete("/delete_configuration/{country_code}")
def delete_config(country_code: str, db: Session = Depends(get_db)):
    db_config = delete_configuration(db, country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return {"detail": "Configuration deleted"}
