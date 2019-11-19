from userede import *
from datetime import date
import io
import csv
import boto3
import os

def to_csv():
    paymentCreditOrder = PaymentsCreditOrders(user=DEFAULT_USER, environment=PRODUCTION)
    request = mappers.credit_orders.Request(parentCompanyNumber=77879899,
                                    subsidiaries=77879899,
                                    startDate=date(2019, 10, 1), endDate=date(2019, 10, 31))

    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL)
    headers = '''paymentId,paymentDate,creditOrderNumber,saleSummaryNumber,bankCode,bankBranchCode,accountNumber,brandCode,companyNumber,amount,discountAmount,netAmount,type,typeCode,anticipationOperationId,anticipationNetAmount'''
    writer.writerow(headers.split(','))

    tsc: mappers.credit_orders.response.PaymentCreditOrder
    for tsc in paymentCreditOrder.paymentsCreditOrders(request).iterable():

        writer.writerow((
            tsc.paymentId,
            tsc.paymentDate,
            tsc.creditOrderNumber,
            tsc.saleSummaryNumber,
            tsc.bankCode,
            tsc.bankBranchCode ,
            tsc.accountNumber,
            tsc.brandCode,
            tsc.companyNumber,
            tsc.amount,
            tsc.discountAmount,
            tsc.netAmount,
            tsc.type,
            tsc.typeCode,
            tsc.anticipationOperationId,
            tsc.anticipationNetAmount,

        ))

    s3 = boto3.client('s3')
    s3.put_object(Body=output.getvalue().encode('utf-8'), Bucket="concil-api-rede", Key=f"sales/details/PaymentOrderCredit_full_1910.csv")

if __name__ == '__main__':
    to_csv()