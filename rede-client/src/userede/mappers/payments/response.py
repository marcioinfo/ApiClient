import related
from ..commons.paging import ResponsePage
from ..commons import fields


@related.immutable
class Paid:
    count = related.IntegerField()
    netAmount = fields.DecimalField()

@related.immutable
class Pending:
    count = related.IntegerField()
    netAmount = fields.DecimalField()


@related.immutable
class Rejected:
    count = related.IntegerField()
    netAmount = fields.DecimalField()

@related.immutable
class Payment:
    paymentId = related.StringField()
    paymentDate = related.DateField(formatter='%Y-%m-%d')
    bankCode = related.IntegerField()
    bankbranchCode = related.IntegerField()
    accountNumber = related.IntegerField()
    brandCode = related.IntegerField()
    companyNumber = related.StringField()
    documentNumber = related.StringField()
    companyName = related.StringField()
    tradeName = related.StringField()
    netAmount = related.IntegerField()
    status = related.StringField()
    statusCode = related.IntegerField()
    type = related.StringField()
    typeCode = related.StringField()


@related.immutable
class PaymentDaily:
    date = related.DateField(formatter='%Y-%m-%d')
    count = related.IntegerField()
    netAmount = fields.DecimalField()

    paid = related.ChildField(Paid, required=False)
    pending = related.ChildField(Pending, required=False)
    rejected = related.ChildField(Rejected, required=False)
    payments = related.SequenceField(Payment, required=False)


@related.immutable
class PaymentsDaily:
    paymentsDaily = related.SequenceField(PaymentDaily)


@related.immutable
class Response(ResponsePage):
    content = related.ChildField(PaymentsDaily)