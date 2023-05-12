import re


# Méthode de conversion du camelCase vers le snake_case
def camel_to_snake(name: str) -> str:
    """
    Conversion d'une string camelCase en string snake_case.
    """
    string_1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', string_1).lower()
