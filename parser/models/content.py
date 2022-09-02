from extension.database import cursor, connection

null = 'null'


class Decision:
    __slots__ = ['date', 'number', 'org']

    def __init__(self, date, number, org):
        self.date = date
        self.number = number
        self.org = org

    def save(self):
        sql_string = f"SELECT create_decision('{self.number}', '{self.date}', '{self.org}');"
        cursor.execute(sql_string)
        connection.commit()
        res = cursor.fetchall()
        return res[0][0]


class Domain:
    __slots__ = ['domain']

    def __init__(self, domain):
        self.domain = domain

    def save(self):
        sql_string = f"SELECT create_domain('{self.domain}');"
        cursor.execute(sql_string)
        connection.commit()
        res = cursor.fetchall()
        return res[0][0]


class Ip:
    __slots__ = ['type', 'ip']

    def __init__(self, type, ip):
        self.type = type
        self.ip = ip

    def save(self):
        sql_string = f"SELECT create_ip('{self.type}', '{self.ip}');"
        cursor.execute(sql_string)
        connection.commit()
        res = cursor.fetchall()
        return res[0][0]


class ExchangeRate:
    __slots__ = ['valute', 'request_time']

    def __init__(self, valute, request_time):
        self.valute = valute
        self.request_time = request_time

    def save(self):
        sql_string = f"SELECT create_exchange_rate('{self.valute}', '{self.request_time}');"
        cursor.execute(sql_string)
        connection.commit()
        res = cursor.fetchall()
        return res[0][0]


class Content:
    __slots__ = ['id', 'include_time', 'entry_type', 'hash', 'exchange_rate_id',
                 'decision_id', 'block_type', 'ts', 'urgency_type', 'url', 'domain_id', 'ip_subnet']

    def __init__(self, id, include_time, entry_type, hash, exchange_rate_id,
                 decision_id=None, block_type=None, ts=None,
                 urgency_type=None, url=None, domain_id=None, ip_subnet=None):
        self.id = id
        self.include_time = include_time
        self.entry_type = entry_type
        self.hash = hash
        self.decision_id = decision_id

        self.exchange_rate_id = exchange_rate_id

        self.ts = ts  # None, строка с датой
        self.urgency_type = urgency_type  # None, 1

        self.block_type = block_type  # None, ip, domain, domain-mask
        self.url = url  # None, url
        self.domain_id = domain_id  # None, domain
        self.ip_subnet = ip_subnet  # None, ip_subnet

    def save(self):
        sql_string = f"SELECT create_content(" \
                     f"'{self.id}'," \
                     f" '{self.include_time}'," \
                     f" '{self.entry_type}'," \
                     f" {self.hash}," \
                     f" {self.decision_id}," \
                     f" {self.exchange_rate_id}," \
                     f" '{self.ts if self.ts is not None else null}'," \
                     f" '{self.urgency_type if self.urgency_type is not None else null}'," \
                     f" '{self.block_type if self.block_type is not None else null}'," \
                     f" '{self.url if self.url is not None else null}'," \
                     f" '{self.ip_subnet if self.ip_subnet is not None else null}'," \
                     f" {self.domain_id if self.domain_id is not None else null});"
        print(sql_string)
        # s = cursor.mogrify(sql_string)
        cursor.execute(sql_string)
        connection.commit()
        res = cursor.fetchall()
        return res[0][0]


class ContentIp:
    __slots__ = ['content_id', 'ip_id']

    def __init__(self, content_id, ip_id):
        self.content_id = content_id
        self.ip_id = ip_id

    def save(self):
        sql_string = f"SELECT create_content_ip('{self.content_id}', {self.ip_id});"
        cursor.execute(sql_string)
        connection.commit()
        res = cursor.fetchall()
        return res[0][0]
