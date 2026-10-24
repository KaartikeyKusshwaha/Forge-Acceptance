def validate_limit(limit: int) -> int:
    if limit < 0 or limit > 100:
        raise ValueError('limit must be from 1 to 100')
    return limit
