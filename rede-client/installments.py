from userede import *
from datetime import date
import io
import csv
import boto3
import os

def to_csv():
    installments = SalesInstallments(user=DEFAULT_USER, environment=PRODUCTION)
    request = mappers.installments.Request(parentCompanyNumber=77879899,
                                    subsidiaries=77879899,
                                    startDate=date(2019, 10, 1), endDate=date(2019, 10, 31))

    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL)
    headers = '''companyNumber,nsu,saleDate,expirationDate,installmentQuantity,installmentNumber,saleSummaryNumber,amount,discountAmount,netAmount,mdrFee,mdrAmount,saleAmount,movementDate,tid'''
    writer.writerow(headers.split(','))

    tsc: mappers.sales.response.Transaction
    for tsc in installments.installments(request).iterable():

        writer.writerow((
            tsc.companyNumber,
            tsc.nsu,
            tsc.saleDate,
            tsc.expirationDate,
            tsc.installmentQuantity,
            tsc.installmentNumber,
            tsc.saleSummaryNumber,
            tsc.amount,
            tsc.discountAmount,
            tsc.netAmount,
            tsc.mdrFee,
            tsc.mdrAmount,
            tsc.saleAmount,
            tsc.movementDate,
            tsc.tid,
        ))

    s3 = boto3.client('s3')
    s3.put_object(Body=output.getvalue().encode('utf-8'), Bucket="concil-api-rede", Key=f"sales/details/parcelas_full_1910_test.csv")

if __name__ == '__main__':
    to_csv()