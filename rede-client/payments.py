from userede import *
from datetime import date
import io
import csv
import boto3
import os

def to_csv():
    payments = Payments(user=DEFAULT_USER, environment=PRODUCTION)
    request = mappers.payments.Request(parentCompanyNumber=77879899,
                                    subsidiaries=77879899,
                                    startDate=date(2019, 10, 1), endDate=date(2019, 10, 31))

    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL)
    headers = '''date,count,netAmount,paid.count,paid.netAmount,pending.count,pending.netAmount,rejected.count,rejected.netAmount'''
    writer.writerow(headers.split(','))

    tsc: mappers.payments.response.Payment
    for tsc in payments.paymentsDaily(request).iterable():

        writer.writerow((
            tsc.date,
            tsc.count,
            tsc.netAmount,
            tsc.paid.count,
            tsc.paid.netAmount,
            tsc.pending.count ,
            tsc.pending.netAmount,
            tsc.rejected.count,
            tsc.rejected.netAmount,
        ))

    s3 = boto3.client('s3')
    s3.put_object(Body=output.getvalue().encode('utf-8'), Bucket="concil-api-rede", Key=f"sales/details/PaymentDaily_full_1910.csv")

if __name__ == '__main__':
    to_csv()