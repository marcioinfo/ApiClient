from userede.base.client import RedeClient
from userede import mappers
from userede.base.verbs import GET


class Sales(RedeClient):
    query, pages, transactions = GET('/conciliation/v1/sales',
                                     mappers.sales.Request,
                                     mappers.sales.Response,
                                     paging=True,
                                     sequence_field='transactions')


class SalesInstallments(RedeClient):
    query, pages, installments = GET('/conciliation/v1/sales/installments',
                                     mappers.sales.installments.Request,
                                     mappers.sales.installments.Response,
                                     paging=True,
                                     sequence_field='installments')


class Payments(RedeClient):
    query, pages, paymentsDaily = GET('/conciliation/v1/payments',
                                      mappers.payments.Request,
                                      mappers.payments.Response,
                                      paging=True,
                                      sequence_field='paymentsDaily')


class PaymentsCreditOrders(RedeClient):
    query, pages, paymentsCreditOrders = GET('/conciliation/v1/payments/credit-orders',
                                             mappers.payments.credit_orders.Request,
                                             mappers.payments.credit_orders.Response,
                                             paging=True,
                                             sequence_field='paymentsCreditOrders')


class Receivables(RedeClient):
    query, pages, receivables = GET('/conciliation/v1/receivables',
                                    mappers.receivables.Request,
                                    mappers.receivables.Response,
                                    paging=True,
                                    sequence_field='receivables')


class ReceivablesSummary(RedeClient):
    query, pages, receivables = GET('/conciliation/v1/receivables/summary',
                                    mappers.receivables.summary.Request,
                                    mappers.receivables.summary.Response,
                                    paging=True,
                                    sequence_field='receivables')


class Charges(RedeClient):
    query, pages, receivables = GET('/conciliation/v1/charges',
                                    mappers.charges.Request,
                                    mappers.charges.Response,
                                    paging=True,
                                    sequence_field='charges')


class ChargesSummary(RedeClient):
    query = GET('/conciliation/v1/charges/summary',
                mappers.charges.summary.Request,
                mappers.charges.summary.Response)


class ChargesAdjustmentTypes(RedeClient):
    query = GET('/conciliation/v1/charges/adjustment-types',
                mappers.charges.adjustments_types.Request,
                mappers.charges.adjustments_types.Response)