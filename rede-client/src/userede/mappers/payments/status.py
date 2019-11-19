import related
from enum import Enum, unique, auto


@unique
class Status(Enum):
    PENDING = auto()
    PAID = auto()
    REJECTED = auto()