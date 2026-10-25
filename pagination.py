def validate_limit(limit) -> int:
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise ValueError('limit must be an integer')
    if limit < 1 or limit > 100:
        raise ValueError('limit must be from 1 to 100')
    return limit
