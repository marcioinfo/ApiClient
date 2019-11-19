import related
from ...commons.paging import RequestPage


@related.mutable
class _Request:
    parentCompanyNumber = related.StringField()
    subsidiaries = related.StringField()
    startDate = related.DateField()
    endDate = related.DateField()


@related.immutable()
class Request(_Request, RequestPage):
    pass

