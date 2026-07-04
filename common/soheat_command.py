from pydantic import BaseModel

class SO2HeatCommand(BaseModel):
    name : str
    parameters : dict

