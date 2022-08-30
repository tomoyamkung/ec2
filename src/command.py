from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional


class Command(Enum):
    LIST: str = "list"

    @classmethod
    def as_list(cls) -> List[Command]:
        return [cls.LIST]

    @classmethod
    def get_by(cls, name: Optional[str]) -> Optional[Command]:
        if name is None:
            return None

        for e in cls.as_list():
            if e.value == name:
                return e

        return None
