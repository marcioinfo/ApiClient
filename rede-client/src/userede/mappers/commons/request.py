import related


@related.mutable
class BaseRequest:
    parentCompanyNumber = related.IntegerField()
    subsidiaries = related.IntegerField()
    startDate = related.DateField(formatter='%Y-%m-%d')
    endDate = related.DateField(formatter='%Y-%m-%d')