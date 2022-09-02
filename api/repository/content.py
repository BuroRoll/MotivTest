import json

import psycopg2
from config import config
from api.extension.json_helper import json_default
from api.models.content import Domain, Decision, ExchangeRate, Content, Ip

connection = psycopg2.connect(user=config['postgresql']['user'],
                              password=config['postgresql']['password'],
                              host=config['postgresql']['host'],
                              port=config['postgresql']['port'],
                              database=config['postgresql']['database'])
cursor = connection.cursor()


def _get_ip(content):
    sql_string = f"select * from contentip inner join ip i on contentip.ip_id = i.id where content_id = '{content.id}';"
    cursor.execute(sql_string)
    res = cursor.fetchall()
    for i in res:
        ip = Ip(type=i[4], ip=i[5])
        content.ip.append(ip)


def get_content_info(hash):
    sql_string = f"select * from content inner join (select id as domain_data_id, domain from domain) as domain_data on content.domain_id = domain_data_id inner join (select id as decision_data_id, date, org from decision) as decision_data on content.decision_id = decision_data_id inner join (select id as exchange_rate_data_id, valute, request_time from exchangerate) as exchange_rate_data on content.exchange_rate_id = exchange_rate_data_id where hash = '{hash}'"
    cursor.execute(sql_string)
    res = cursor.fetchall()
    res = res[0]
    decision = Decision(date=res[15], number=res[14], org=res[16])
    domain = Domain(domain=res[13])
    exchange_rate = ExchangeRate(valute=res[18], request_time=res[19])
    content = Content(id=res[0], include_time=res[1], entry_type=res[2], hash=res[3], ts=res[5], urgency_type=res[6],
                      block_type=res[7], url=res[8], ip_subnet=res[9], decision=decision, domain=domain,
                      exchange_rate=exchange_rate)
    _get_ip(content=content)
    return json.dumps(content, ensure_ascii=False, default=json_default)
