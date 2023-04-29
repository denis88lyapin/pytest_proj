def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу,
    если ключ существует. В ином случае возвращается значение default
    """
    if not isinstance(collection, dict):
        return 'Недопустимая коллекция'

    if key not in collection:
        return default

    return collection[key]
