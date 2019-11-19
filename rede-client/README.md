# Cliente API Rede

Documentação da API:

* Conciliação.: https://conciliationrede.docs.apiary.io

* Credenciamento.: https://affiliationrede.docs.apiary.io

### Forma de uso:

Exemplo:

```
>>> from userede import *
>>> sales = Sales(user=DEFAULT_USER, environment=PRODUCTION)  
>>> request = mappers.sales.Request(parentCompanyNumber=77879899, subsidiaries=77879899, startDate='2019-07-01', endDate='2019-07-01')
>>> for tsc in sales.transactions(request).iterable(): 
...     print(tsc.saleDate) 
...                                                                                                                                                                                           
2019-07-01
2019-07-01
2019-07-01
2019-07-01
2019-07-01
...
```
### Endpoints disponíveis

#### Conciliação
* Consultar Vendas (consultarVendas)
* Consultar Parcelas (consultarParcelas)
* Consultar Pagamentos - Visão Sumarizada CIP (consultarPagamentosSumarizadosCIP)
* Consultar Pagamentos - Visão Ordem de Crédito (Sem método, API EM CONSTRUÇÃO)
* Consultar Recebíveis (Sem método, API EM CONSTRUÇÃO)
* Consultar Recebíveis - Visão Sumarizada (consultarRecebiveisSumarizados)
* Consultar Débitos - Visão Detalhada (consultarDebitos)
* Consultar Débitos - Visão Sumarizada (Sem método, API EM CONSTRUÇÃO)
* Consultar Lista de Ajustes de Débito (consultarListaAjusteDebitos)

## TODO
* POST factory
* PUT factory
* Doc TODO

### Endpoints TODO

#### Credenciamento
* Realizar Proposta de Credenciamento (criarPropostaCredenciamento)
* Consultar Proposta de Credenciamento por Id (consultarPropostaCredenciamentoPorId)
* Consultar Estabelecimento Comercial (consultarEstabelecimentoComercial)
* Cancelar Estabelecimento Comercial (cancelarEstabelecimentoComercial)
* Consultar Preços (consultarPrecos)
* Consultar MCCs (consultarMCCs)
* Realizar Lead Credenciamento (createLeadCredenciamento)
