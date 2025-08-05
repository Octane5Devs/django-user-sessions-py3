try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    from importlib_metadata import version, PackageNotFoundError  # Only for Python <3.8

try:
    __version__ = version("django-user-sessions")
except PackageNotFoundError:
    __version__ = None
