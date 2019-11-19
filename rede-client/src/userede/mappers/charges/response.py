import related
from ..commons.paging import ResponsePage
from ..commons import fields

#  'compensateDate', 'creditExpirationDate', 'typeCode', and 'processRetentionNumber
@related.immutable
class Charge:
    adjustmentTypeCode = related.IntegerField() # TODO Enum. Não tem tabela na documentação da Rede
    adjustmentTypeDescription = related.StringField()

    creditOrderNumber = related.IntegerField()
    companyNumber = related.IntegerField()
    debitNumber = related.IntegerField()
    debitAmount = fields.DecimalField()
    debitCompensatedAmount = fields.DecimalField()

    documentNumber = related.StringField()
    companyName = related.StringField()
    tradeName = related.StringField()

    type = related.StringField()

    compensateDate = related.DateField(formatter='%Y-%m-%d', required=False) # Está como obrigatório na daocumentação
    creditExpirationDate = related.DateField(formatter='%Y-%m-%d', required=False) # Está como obrigatório na daocumentação
    typeCode = related.IntegerField(required=False)
    processRetentionNumber = related.StringField(required=False)


@related.immutable
class Charges:
    charges = related.SequenceField(Charge)


@related.immutable
class Response(ResponsePage):
    content = related.ChildField(Charges)