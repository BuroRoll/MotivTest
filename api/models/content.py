class Decision:
    def __init__(self, date, number, org):
        self.date = date
        self.number = number
        self.org = org


class Domain:
    def __init__(self, domain):
        self.domain = domain


class Ip:
    def __init__(self, type, ip):
        self.type = type
        self.ip = ip


class ExchangeRate:
    def __init__(self, valute, request_time):
        self.valute = valute
        self.request_time = request_time


class Content:
    def __init__(self, id, include_time, entry_type, hash, exchange_rate,
                 decision=None, block_type=None, ts=None,
                 urgency_type=None, url=None, domain=None, ip_subnet=None):
        self.id = id
        self.include_time = include_time
        self.entry_type = entry_type
        self.hash = hash

        self.decision = decision

        self.exchange_rate = exchange_rate
        self.ip = []

        self.domain = domain  # None, domain

        self.ts = ts  # None, строка с датой
        self.urgency_type = urgency_type  # None, 1

        self.block_type = block_type  # None, ip, domain, domain-mask
        self.url = url  # None, url

        self.ip_subnet = ip_subnet  # None, ip_subnet


class ContentIp:
    def __init__(self, content_id, ip_id):
        self.content_id = content_id
        self.ip_id = ip_id
