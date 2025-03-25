from pydantic import BaseModel, Field
from typing import Optional

class DeviceSpecs(BaseModel):
    model_name: str = Field(..., title="Model Name")
    camera: Optional[str] = Field(None, title="Camera Specs")
    processor: Optional[str] = Field(None, title="Processor Details")
    battery: Optional[str] = Field(None, title="Battery Life")
    display: Optional[str] = Field(None, title="Display Size & Type")

  