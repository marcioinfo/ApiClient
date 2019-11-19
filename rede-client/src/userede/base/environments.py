import related


@related.immutable
class Environment:
    name = related.StringField()
    base_url = related.StringField()


STAGING = Environment(name='Homologação', base_url='https://api-hom.userede.com.br/redelabs')
PRODUCTION = Environment(name='Produção', base_url='https://api.userede.com.br/redelabs')
MOCK = Environment(name='RedeMock', base_url='https://private-anon-4eb00cc1ec-conciliationrede.apiary-mock.com/redelabs')
PROXY = Environment(name='Debbuging Proxy', base_url='https://private-anon-0886c3692a-conciliationrede.apiary-proxy.com/redelabs')
