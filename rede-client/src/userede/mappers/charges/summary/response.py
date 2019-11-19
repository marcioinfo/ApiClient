import related
from ...commons.paging import ResponsePage
from ...commons import fields


@related.immutable
class Charge:
    startDate = related.DateField(formatter='%Y-%m-%d')
    endDate = related.DateField(formatter='%Y-%m-%d')
    adjustmentTypeCode = related.IntegerField()  # TODO Enum. Não tem tabela na documentação da Rede
    debitAmount = fields.DecimalField()
    debitCompensatedAmount = fields.DecimalField()


@related.immutable
class Charges:
    charges = related.SequenceField(Charge)


@related.immutable
class Response:# (ResponsePage):
    content = related.ChildField(Charges)