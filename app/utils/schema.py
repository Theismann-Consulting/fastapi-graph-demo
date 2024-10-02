from typing import Optional, List
from pydantic import BaseModel, field_validator
from pydantic_core.core_schema import ValidationInfo
from datetime import datetime


# Authorization response models
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


# Node response models
class NodeBase(BaseModel):
    node_id: str
    labels: list


class Node(NodeBase):
    properties: Optional[dict] = None


class Nodes(BaseModel):
    nodes: List[Node]

# User response models
class User(BaseModel):
    username: str
    full_name: str
    joined: Optional[datetime] = None
    disabled: bool
    role: str

class UserInDB(User):
    hashed_password: str

# User request models
class UserCreate(User):
    password: str

class UserUpdate(BaseModel):
    full_name: str
    disabled: bool
    role: str

# Relationship response models
class Relationship(BaseModel):
    relationship_id: int
    relationship_type: str
    source_node: Node
    target_node: Node
    properties: Optional[dict] = None


# Query response model
class Query(BaseModel):
    response: list
