import related
from ...commons import fields, paging


@related.immutable
class Installment:
    companyNumber = related.StringField()
    nsu = related.StringField()
    saleDate = related.DateField()
    expirationDate = related.DateField()
    installmentQuantity = related.IntegerField()
    installmentNumber = related.IntegerField()
    saleSummaryNumber = related.IntegerField()
    amount = fields.Decimal()
    discountAmount = fields.DecimalField()
    netAmount = fields.DecimalField()
    mdrFee = fields.DecimalField()
    mdrAmount = fields.DecimalField()
    saleAmount = fields.DecimalField()

    movementDate = related.DateField(required=False)
    tid = related.StringField(required=False)


@related.immutable
class Installments:
    installments = related.SequenceField(Installment)


@related.immutable
class Response(paging.ResponsePage):
    content = related.ChildField(Installments)
