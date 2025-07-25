def keyword_serializer(keyword) -> dict:
    return {
        "id": str(keyword["_id"]),
        "keyword": keyword["keyword"],
        "results": keyword["results"],
        "timestamp": keyword["timestamp"]
    }

def data_serializer(data) -> list:
    if isinstance(data, list):
        return [keyword_serializer(item) for item in data]
    elif isinstance(data, dict):
        return keyword_serializer(data)