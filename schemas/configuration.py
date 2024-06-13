from pydantic import BaseModel
from typing import Dict, Any

class ConfigurationBase(BaseModel):
    country_code: str
    onboarding_requirements: Dict[str, Any]

class ConfigurationCreate(ConfigurationBase):
    pass

class ConfigurationUpdate(ConfigurationBase):
    pass

class ConfigurationResponse(ConfigurationBase):
    id: int

    class Config:
        orm_mode = True
