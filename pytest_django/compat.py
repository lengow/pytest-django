# This file cannot be imported from until Django sets up
try:
    # Django 1.11
    from django.test.utils import setup_databases, teardown_databases  # noqa: F401
except ImportError:
    # In Django prior to 1.11, teardown_databases is only available as a method on DiscoverRunner
    from django.conf import settings
    from django.test.utils import get_runner
    from functools import partial

    _runner = get_runner(settings)

    setup_databases = partial(_runner.setup_databases, _runner)
    teardown_databases = partial(_runner.teardown_databases, _runner)
