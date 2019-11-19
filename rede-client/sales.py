from userede import *
from datetime import date
import io
import csv
import boto3
import os


def to_csv():
    sales = Sales(user=DEFAULT_USER, environment=PRODUCTION)
    request = mappers.sales.Request(parentCompanyNumber=77879899,
                                    subsidiaries=77879899,
                                    startDate=date(2019, 10, 1), endDate=date(2019, 10, 31))

    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL)
    headers = '''mdrfee,saledate,mdramount,cardnumber,tid,status,discountamount,installmentquantity,capturetypecode,tracking.status,tracking.date,tracking.amount,boardingfeeamount,salehour,nsu,flexamount,capturetype,feetotal,authorizationcode,amount,netamount,device,flex,movementdate,tokenized,salesummarynumber,flexfee,devicetype,brandcode,ordernumber,merchant.companynumber,merchant.companyname,merchant.documentnumber,merchant.tradename,modality.type,modality.code,modality.product,modality.productcode'''
    writer.writerow(headers.split(','))

    tsc: mappers.sales.response.Transaction
    for tsc in sales.transactions(request).iterable():

        writer.writerow((
            tsc.mdrFee,
            tsc.saleDate,
            tsc.mdrAmount,
            tsc.cardNumber,
            tsc.tid,
            tsc.status.value,
            tsc.discountAmount,
            tsc.installmentQuantity,
            tsc.captureTypeCode,
            tsc.tracking[-1].status.value,
            tsc.tracking[-1].date,
            tsc.tracking[-1].amount,
            tsc.boardingFeeAmount,
            tsc.saleHour,
            tsc.nsu,
            tsc.flexAmount,
            tsc.captureType,
            tsc.feeTotal,
            tsc.authorizationCode,
            tsc.amount,
            tsc.netAmount,
            tsc.device,
            tsc.flex,
            tsc.movementDate,
            tsc.tokenized,
            tsc.saleSummaryNumber,
            tsc.flexFee,
            tsc.deviceType,
            tsc.brandCode.value,
            tsc.orderNumber,
            tsc.merchant.companyNumber,
            tsc.merchant.companyName,
            tsc.merchant.documentNumber,
            tsc.merchant.tradeName,
            tsc.modality.type,
            tsc.modality.code.value,
            tsc.modality.product,
            tsc.modality.productCode.value,
        ))

    s3 = boto3.client('s3')
    s3.put_object(Body=output.getvalue().encode('utf-8'), Bucket="concil-api-rede", Key=f"sales/details/full_1910_test.csv")

if __name__ == '__main__':
    to_csv()