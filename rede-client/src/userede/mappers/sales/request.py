import related
from userede.mappers.commons.brand import Brand
from .modality import Modality
from .status import Status
from ..commons.paging import RequestPage
from ..commons.request import BaseRequest


@related.mutable
class _Request(BaseRequest):
    brands = related.SequenceField(Brand, required=False)
    modalities = related.SequenceField(Modality, required=False)
    status = related.ChildField(Status, required=False)


@related.immutable
class Request(_Request, RequestPage):
    pass