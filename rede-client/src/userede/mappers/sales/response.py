import related
from enum import Enum, unique
from .merchant import Merchant
from .modality import Modality
from .tracking import Tracking
from userede.mappers.commons.brand import Brand
from .status import Status
from ..commons.paging import ResponsePage
from ..commons import fields


@unique
class ChargebackStatus(Enum):
    CHARGEBACK_IN_DISPUTE = 'CHARGEBACK_IN_DISPUTE'
    CHARGEBACK_SOLVED_DEBIT = 'CHARGEBACK_SOLVED_DEBIT'
    CHARGEBACK_SOLVED_CREDIT = 'CHARGEBACK_SOLVED_CREDIT'
    CHARGEBACK_SOLVED_NO_IMPACT = 'CHARGEBACK_SOLVED_NO_IMPACT'


@related.immutable
class Transaction:
    merchant = related.ChildField(Merchant)
    brandCode = related.ChildField(Brand)
    authorizationCode = related.IntegerField()
    tokenized = related.BooleanField()
    installmentQuantity = related.IntegerField()
    nsu = related.IntegerField()
    saleSummaryNumber = related.IntegerField()
    movementDate = related.DateField(formatter='%Y-%m-%d')
    saleDate = related.DateField(formatter='%Y-%m-%d')
    saleHour = related.TimeField(formatter='%H:%M:%S')
    status = related.ChildField(Status)
    deviceType = related.StringField()
    amount = fields.DecimalField()
    mdrFee = fields.DecimalField()
    mdrAmount = fields.DecimalField()
    feeTotal = fields.DecimalField()
    discountAmount = fields.DecimalField()
    netAmount = fields.DecimalField()
    tracking = related.SequenceField(Tracking)

    tid = related.StringField(required=False)
    orderNumber = related.IntegerField(required=False)
    cardNumber = related.RegexField(r'[0-9]{6}\*{6}[0-9]{3,4}', required=False)
    tokenNumber = related.StringField(required=False)
    modality = related.ChildField(Modality, required=False)
    device = related.StringField(required=False)
    captureType = related.StringField(required=False)
    captureTypeCode = related.IntegerField(required=False)
    chargebackStatus = related.ChildField(ChargebackStatus, required=False)
    flex = related.BooleanField(required=False)
    flexFee = related.DecimalField(required=False)
    flexAmount = related.DecimalField(required=False)
    boardingFeeAmount = related.DecimalField(required=False)


@related.immutable
class Transactions:
    transactions = related.SequenceField(Transaction)

@related.immutable
class Response(ResponsePage):
    content = related.ChildField(Transactions)