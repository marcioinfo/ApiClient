from enum import Enum, unique


@unique
class Status(Enum):
    APPROVED = 'APPROVED'
    CANCELLED = 'CANCELLED'