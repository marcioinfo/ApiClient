import related


@related.immutable
class Merchant:
    companyNumber = related.StringField()
    companyName = related.StringField()
    documentNumber = related.StringField()
    tradeName = related.StringField()

