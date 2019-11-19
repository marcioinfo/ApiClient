from userede import *
from datetime import date
import io
import csv
import boto3
import os

def to_csv():
    receivables = Receivables(user=DEFAULT_USER, environment=PRODUCTION)
    request = mappers.receivables.Request(parentCompanyNumber=77879899,
                                    subsidiaries=77879899,
                                    startDate=date(2019, 12, 1), endDate=date(2019, 12, 31))

    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL)
    headers = '''creditOrderNumber,saleSummaryNumber,bankCode,bankBranchCode,accountNumber,brandCode,accountNumber,companyNumber,amount,discountAmount,netAmount'''
    writer.writerow(headers.split(','))

    tsc: mappers.receivables.response.Receivable
    for tsc in receivables.receivables(request).iterable():

        writer.writerow((
            tsc.amount,
            tsc.companyNumber,
            tsc.companyName,
            tsc.bankBranchCode,
            tsc.date,
            tsc.type ,
        ))

    s3 = boto3.client('s3')
    s3.put_object(Body=output.getvalue().encode('utf-8'), Bucket="concil-api-rede", Key=f"sales/details/Receivable_full_1912.csv")

if __name__ == '__main__':
    to_csv()