from pydantic import BaseModel


class TaskBase(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int

    class Config:
        from_attributes  = True


class TaskCreate(BaseModel):
    title: str
    description: str
    owner_id: int


class TaskUpdate(BaseModel):
    id: int

    class Config:
        from_attributes  = True

class Task(TaskBase):
    id: int

    class Config:
        from_attributes  = True


