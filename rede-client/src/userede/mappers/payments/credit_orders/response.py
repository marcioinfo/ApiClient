import related
from ...commons import fields
from ...commons.brand import Brand
from ...commons.paging import ResponsePage


@related.immutable
class PaymentCreditOrder:
    paymentId = related.StringField()
    paymentDate = related.DateField(formatter='%Y-%m-%d')
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
    type = related.StringField()
    typeCode = related.StringField()
    anticipationOperationId = related.IntegerField()
    anticipationNetAmount = fields.DecimalField()


@related.immutable
class PaymentsDaily:
    paymentsCreditOrders = related.SequenceField(PaymentCreditOrder)


@related.immutable
class Response(ResponsePage):
    content = related.ChildField(PaymentsDaily)


