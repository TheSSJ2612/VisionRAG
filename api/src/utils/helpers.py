from datetime import datetime
import json


def datetime_serializer(obj):
    """JSON serializer for datetime objects"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")


def format_response(data):
    """Standardize API response format"""
    return {"timestamp": datetime.now().isoformat(), "data": data, "error": None}
