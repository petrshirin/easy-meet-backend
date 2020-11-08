from base64 import b64encode
from collections import OrderedDict
from hashlib import sha256
from hmac import HMAC
from urllib.parse import urlparse, parse_qsl, urlencode
from django.conf import settings
from typing import Union, Dict


def check_sign(*, query: dict, secret: str) -> Union[Dict, None]:
    """Check VK Apps signature"""
    vk_subset = OrderedDict(sorted(x for x in query.items() if x[0][:3] == "vk_"))
    hash_code = b64encode(HMAC(secret.encode(), urlencode(vk_subset, doseq=True).encode(), sha256).digest())
    decoded_hash_code = hash_code.decode('utf-8')[:-1].replace('+', '-').replace('/', '_')
    if query["sign"] == decoded_hash_code:
        return vk_subset


def validate_request(url: str) -> Union[Dict, None]:
    if not url:
        return None
    client_secret = settings.MINI_APP_SECRET  # Защищённый ключ из настроек вашего приложения

    query_params = dict(parse_qsl(urlparse(url).query, keep_blank_values=True))
    return check_sign(query=query_params, secret=client_secret)
