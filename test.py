class OriginalException(Exception):
    pass

class AnotherException(Exception):
    pass

def raise_exception():
    raise OriginalException()

def raise_another_exception():
    raise AnotherException()

def show_something():
    try:
        raise_exception()
    except OriginalException:
        raise_another_exception()


try:
    show_something()
except Exception:
    import sys
    exc_info = sys.exc_info()
    import json
    from sentry_sdk.utils import exceptions_from_error_tuple
    print(json.dumps(exceptions_from_error_tuple(exc_info), indent=2))
