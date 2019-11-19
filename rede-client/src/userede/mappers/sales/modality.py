import related
from enum import Enum, unique, auto


@unique
class Type(Enum):
    CREDIT = 'CREDIT'
    DEBIT = 'DEBIT'

@unique
class Code(Enum):
    CREDIT = auto()
    DEBIT = auto()

@unique
class Product(Enum):
    NO_INSTALLMENTS = auto()
    IN_INSTALLMENTS_WITH_INTEREST = auto()
    IN_INSTALLMENTS_NO_INTEREST = auto()
    CREDIT_PLAN = auto()

@related.immutable
class Modality:
    type = related.StringField()
    code = related.ChildField(Code)
    product = related.StringField()
    productCode = related.ChildField(Product)