import json
from datetime import date, datetime


class DateTimeAwareEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)


def serialize_json(data: list[dict]) -> dict:
    json_string = json.dumps(data, cls=DateTimeAwareEncoder, ensure_ascii=False)
    return json.loads(json_string)
