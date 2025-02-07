from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

SCHEMA_VERSION = 4


class AnalysisBasis(str, Enum):
    enrollments = "enrollments"
    exposures = "exposures"


class Statistic(BaseModel):
    metric: str
    statistic: str
    branch: str
    parameter: Optional[float] = None
    comparison: Optional[str] = None
    comparison_to_branch: Optional[str] = None
    ci_width: Optional[float] = Field(default=None, ge=0.0, le=1.0)
    point: Optional[float] = None
    lower: Optional[float] = None
    upper: Optional[float] = None
    segment: str = Field(default="all")
    analysis_basis: Optional[AnalysisBasis]
    window_index: Optional[str]


class Statistics(BaseModel):
    __root__: list[Statistic]
