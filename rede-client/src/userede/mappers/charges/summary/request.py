import related
from ...commons.paging import RequestPage
from ...commons.request import BaseRequest


@related.mutable
class _Request(BaseRequest):
    types = related.StringField(required=False)


@related.immutable
class Request(_Request, RequestPage):
    pass
