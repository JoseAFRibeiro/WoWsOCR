import pydantic
from typing import Optional


class Match(pydantic.BaseModel):
    base_income: Optional[int]
    premium_income: Optional[int]
    is_win: Optional[bool]
