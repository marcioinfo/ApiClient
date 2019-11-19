import related
from ..commons.paging import ResponsePage
from ..commons import fields
from ..commons.brand import Brand


@related.immutable
class Receivable:
    creditOrderNumber = related.IntegerField()
    saleSummaryNumber = related.IntegerField()
    bankCode = related.IntegerField()
    bankBranchCode = related.IntegerField()
    accountNumber = related.IntegerField()
    brandCode = related.ChildField(Brand)
    companyNumber = related.StringField()
    amount = fields.DecimalField()
    discountAmount = fields.DecimalField()
    netAmount = fields.DecimalField()


@related.immutable
class Receivables:
    receivables = related.SequenceField(Receivable)


@related.immutable
class Response(ResponsePage):
    content = related.ChildField(Receivables)