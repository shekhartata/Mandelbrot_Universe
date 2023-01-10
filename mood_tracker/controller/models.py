from .utils import get_session
import uuid
from cassandra.cqlengine import columns as cassandra_columns
from django_cassandra_engine.models import DjangoCassandraModel


class Users(DjangoCassandraModel):
    __keyspace__ = 'db'
    id = cassandra_columns.UUID(primary_key=True, default=uuid.uuid4)
    music_mood = cassandra_columns.Text(max_length=100)
    date_stamp = cassandra_columns.Text(max_length=15)

    class Meta:
        get_pk_field = 'id'
