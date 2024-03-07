#!/usr/bin/python3

import uuid
from datetime import datetime

"""Define a class that instanitiate a new instance"""

class BaseModel:
    """base class that defines all attributes"""
    def __init__(self):
    id = str(uuid.uuid4())
    created_at = datetime.now()

