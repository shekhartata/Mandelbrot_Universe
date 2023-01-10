import uuid
import json
from django_cassandra_engine.connection import CassandraConnection
from django_cassandra_engine.utils import (
    get_cql_models,
    get_installed_apps,
    get_cassandra_connection,
)
from .models import Users

def get_users_all():
    return [dict(entry) for entry in Users.objects.all()]

def create_record_users(values):
    return dict(Users.objects.create(**values))

def get_users_id(usr_id):
    return [dict(entry) for entry in Users.objects.filter(id=usr_id)]

def update_record_users(usr_id, values):
    print(usr_id, values)
    Users.objects.filter(id=usr_id).update(**values)
    return [dict(entry) for entry in Users.objects.filter(id=usr_id)]
