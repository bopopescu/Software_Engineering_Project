from functools import wraps

from App.Models import (
    DefaultConfig,
    User
)

from flask import (
    request,
    abort
)
    
class DefaultAuthorization:
    """
    Authorization class that provides function wrappers to require token authorization for a route
    """

    def __init__(self, config=None):
        if not config:
            config = DefaultConfig()

        self._config = DefaultConfig()


    def __str__(self):
        return "Default Authorization"


    def require_auth(self, scope):
        """
        Decorator for methods that will require a properly scoped jwt in the request header
        """
        def decorator(func):
            """
            Function decorator for authorization
            """
            @wraps(func)
            def wrapper(*args, **kwargs):
                headers = request.headers
                authorization = headers.get("Authorization", None)

                if authorization:
                    token = authorization.split(' ')[1]

                    if token:
                        user = User.from_token(token)

                        if user.scope == scope:
                            return func(user)

                return abort(401)
            return wrapper
        return decorator
