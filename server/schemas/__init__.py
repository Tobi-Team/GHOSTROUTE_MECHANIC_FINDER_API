from fastapi import Query
from pydantic import BaseModel, Field
from typing import Any, Union, TypeVar, Generic, Optional


T = TypeVar("T")


class ServiceResultModel(Generic[T]):
    def __init__(self, data=None) -> None:
        self.data: Union[T, None] = data
        self.errors: list[str] = []
        self.has_errors: bool = False

    def add_error(self, error: str | list[str]):
        self.has_errors = True
        if (type(error) == list or type(error) == tuple) and len(error) > 0:
            for err in error:
                self.errors.append(err)
        else:
            self.errors.append(error)
        return self


class APIResponse(BaseModel, Generic[T]):
    message: Optional[str] = Field(default="Success", examples=["Success"])
    success: bool = True
    status_code: int = 200
    data: Optional[T] = None

    model_config = {"from_attributes": True}


class PagedResponse(APIResponse):
    pages: int = 1
    page_number: int = 1
    count: int = 0
    total: int = 0
    per_page: int = 0


class PagedQuery(BaseModel):
    page: int = Query(1, ge=1)
    per_page: int = Query(10, ge=1, le=100)
    # search: Optional[str] = Query(None)
