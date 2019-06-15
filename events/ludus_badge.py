import faust

class LudusBadge(faust.Record, isodates=True, serializer="json"):
    type: str = None
    username: str = None
    badge: str = None
    description: str = None
    event_type: str = None
    criteria : int = None
