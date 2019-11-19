import related
import os


@related.immutable
class User:
    name = related.StringField()
    password = related.StringField(repr=False)
    auth = related.SequenceField(str)


DEFAULT_USER = User(name=os.environ.get('REDE_USER'),
                    password=os.environ.get('REDE_PASSWORD'),
                    auth=(os.environ.get('REDE_AUTH_USER'), os.environ.get('REDE_AUTH_PASSWORD')))