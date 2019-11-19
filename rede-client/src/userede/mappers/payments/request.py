import related
from enum import Enum, auto, unique
from userede.mappers.commons.brand import Brand
from .status import Status
from ..commons.paging import RequestPage
from ..commons.request import BaseRequest


@unique
class Type(Enum):
    CREDIT = 'CRE'
    DEBIT = 'DEB'
    ANTICIPATION = 'ANT'


@related.mutable
class _Request(BaseRequest):
    brands = related.SequenceField(Brand, required=False)
    banks = related.IntegerField(required=False)
    status = related.ChildField(Status, required=False)
    types = related.ChildField(Type, required=False)


@related.immutable
class Request(_Request, RequestPage):
    pass