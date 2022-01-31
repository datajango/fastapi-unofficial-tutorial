# Basic model usage
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
import json

class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

def main():
    try:

        external_data = {
            'id': '123',
            'signup_ts': '2019-06-01 12:22',
            'friends': [1, 2, '3'],
        }
        user = User(**external_data)

        print(f"User object created successfully:", user.dict())

    except Exception as e:
        print('Exception:', e)



if __name__ == '__main__':
    main()