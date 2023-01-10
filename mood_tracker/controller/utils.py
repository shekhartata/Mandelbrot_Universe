import sqlalchemy, sqlalchemy.orm
from aldjemy.core import get_engine
import json
from sqlalchemy.ext.declarative import DeclarativeMeta
import pandas as pd
from sklearn import preprocessing


cluster_mapper = {
    0: "Speechy - Lyrical / Feels",
    1: "Instrumental - Music over lyrics / Influential beats",
    2: "Energetic / upbeat music"
}


def get_session():
    engine = get_engine()
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    return session


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields

        return json.JSONEncoder.default(self, obj)


def normalise_loudness_param(songs):
    loudness = songs[['loudness']].values
    min_max_scaler = preprocessing.MinMaxScaler()
    loudness_scaled = min_max_scaler.fit_transform(loudness)
    songs['loudness'] = pd.DataFrame(loudness_scaled)
