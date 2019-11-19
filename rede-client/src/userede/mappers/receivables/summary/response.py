import related
from ...commons.paging import ResponsePage
from ...commons import fields


@related.immutable
class Receivables:
    amount = fields.DecimalField()
    companyNumber = related.StringField()
    companyName = related.StringField()
    date = related.DateField(formatter='%Y-%m-%d')
    type = related.StringField()


@related.immutable
class PaymentsDaily:
    receivables = related.SequenceField(Receivables)


@related.immutable
class Response(ResponsePage):
    content = related.ChildField(PaymentsDaily)