from .models import User
from .utils import AlchemyEncoder
from sqlalchemy import desc
import json
import ast
from django.http import HttpResponse, JsonResponse
import uuid


def users_create(values, session):
    user_ref = User()
    if not values.get('id'):
        values['id'] = str(uuid.uuid4())
    if session is None:
        session = get_session()

    user_ref.update(values)
    user_ref.save(session=session)

    return _user_get(values['id'], session=session)

def user_getById(id, session):
    return _user_get(id, session)

def _user_get(user_id, session):
       result_e = model_query(User, session=session).\
           filter_by(id=user_id).first()
       if not result_e:
           print("exception caught in user_get")
       result = json.dumps(result_e, cls=AlchemyEncoder)
       return result

def model_query(*args, **kwargs):
    session = kwargs.get('session') or get_session()
    query = session.query(*args)
    return query

def users_get_all(session):
    response = []
    result = model_query(User, session=session).all()
    for entry in result:
        entry_final = json.dumps(entry, cls=AlchemyEncoder)
        response.append(entry_final)
    return response
