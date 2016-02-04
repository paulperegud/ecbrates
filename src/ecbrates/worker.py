import threading
from django.db import IntegrityError
from .parser import fetch_and_parse

def background_parsing(uris):
    """single threaded background parsing"""
    t = threading.Thread(target=worker, args=(uris,))
    t.start()

def worker(uris):
    """safely fetches and parses every URI"""
    for feed in uris:
        process_feed(feed)
    return

def process_feed(feed):
    rates = fetch_and_parse(feed)
    for i in rates:
        try:
            i.save()
        except IntegrityError:
            pass
