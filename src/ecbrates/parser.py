import feedparser
from datetime import datetime
from pytz import timezone

from .models import ECBRate

def fetch_and_parse(uri):
    arr = []
    for entry in feedparser.parse(uri).entries:
        parsed = parse_entry(entry)
        arr.append(parsed)
    return arr

def parse_entry(entry):
    [rate, base] = entry.cb_exchangerate.split('\n')
    target = entry.cb_targetcurrency
    date = parse_datetime(entry.updated)
    return ECBRate(date=date, base=base, target=target, rate=rate)

def parse_datetime(dtstring):
    noTz = datetime.strptime(dtstring[:-6], '%Y-%m-%dT%H:%M:%S')
    eTz = dtstring[-6:] # not parseable by strptime since in +HH:MM instead of +HHMM
    assert eTz == "+01:00", "there is not time to write proper parser of non-standard timezone representation"
    return noTz.replace(tzinfo = timezone('Europe/Berlin'))
