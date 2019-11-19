from userede import *
from datetime import date
receivables = Receivables(user=DEFAULT_USER, environment=PRODUCTION)
request = mappers.receivables.Request(parentCompanyNumber=77879899,
                                      subsidiaries=77879899,
                                      startDate=date(2019, 12, 1), endDate=date(2019, 12, 31))
for tsc in receivables.receivables(request).iterable():
    print(tsc)
