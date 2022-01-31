from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []
