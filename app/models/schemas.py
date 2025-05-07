
from pydantic import BaseModel
from typing import Optional

class AppBuildRequest(BaseModel):
    name: str
    template_id: str
    description: Optional[str] = None
