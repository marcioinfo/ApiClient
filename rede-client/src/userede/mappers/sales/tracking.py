import related
from enum import Enum, unique
from ..commons import fields


@unique
class Status(Enum):
    APPROVED = 'APPROVED'
    PARTIAL_CANCELLED = 'PARTIAL_CANCELLED'
    CANCELLED = 'CANCELLED'
    CHARGEBACK_IN_DISPUTE = 'CHARGEBACK_IN_DISPUTE'
    CHARGEBACK_SOLVED_DEBIT = 'CHARGEBACK_SOLVED_DEBIT'
    CHARGEBACK_SOLVED_CREDIT = 'CHARGEBACK_SOLVED_CREDIT'
    CHARGEBACK_SOLVED_NO_IMPACT = 'CHARGEBACK_SOLVED_NO_IMPACT'


@related.immutable
class Tracking:
    amount = fields.DecimalField()
    status = related.ChildField(Status)
    date = related.DateField(formatter='%Y-%m-%d')