import related
from ...commons.request import BaseRequest


@related.immutable
class Request(BaseRequest):
    paymentId = related.StringField(required=False)
