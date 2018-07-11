from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import View

def custom_login_required(view):
    #view argument must be function
    decorator = method_decorator(login_required)
    decorated_view = decorator(view)
    return decorated_view

def required_authenticated_permissions(permission):

    def decorator(cls):
        if (not isinstance(cls, type) or not issubclass(cls, View)):
            raise ImproperlyConfigured(
                "required_authenticated_permission"
                " must be applied to subclasses "
                "of View class."
            )
        check_auth = method_decorator(login_required)
        check_perm = method_decorator(permission_required(permission, raise_exception=True))
        cls.dispatch = check_auth(check_perm(cls.dispatch))
        return cls
    return decorator


def class_login_required(cls):
    if (not isinstance(cls, type) or not issubclass(cls, View)):
        raise ImproperlyConfigured(
            "class_login_required"
            " must be applied to subclasses "
            "of View class"
        )
    decorator = method_decorator(login_required)
    cls.dispatch = decorator(cls.dispatch)
    return cls

