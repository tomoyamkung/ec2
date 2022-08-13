from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional


class Environment(Enum):
    PRODUCTION: str = "prod"
    STAGING: str = "stg"
    DEVELOPMENT: str = "dev"

    @classmethod
    def as_list(cls) -> List[Environment]:
        return [cls.PRODUCTION, cls.STAGING, cls.DEVELOPMENT]

    @classmethod
    def get_by(cls, name: Optional[str]) -> Optional[Environment]:
        if name is None:
            return None

        for e in cls.as_list():
            if e.value == name:
                return e

        return None

    @property
    def to_filter(self) -> Dict[str, Any]:
        return {"Name": "tag:Category1", "Values": [self.value]}
