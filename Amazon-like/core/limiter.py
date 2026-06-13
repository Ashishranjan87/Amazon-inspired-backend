from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["10000/minute"],
    storage_uri="redis://localhost:6379/1",
)