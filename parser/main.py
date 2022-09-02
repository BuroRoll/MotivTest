from datetime import datetime
from xml.etree.ElementTree import iterparse

from models.content import *
from extension.decorators import time_of_function
from extension.valuteExchange import get_curs_value


def parse_xml(file_name):
    content = None
    unique_domains = set()
    counter = 0
    for event, elem in iterparse(file_name, events=('start', 'end')):
        if elem.tag == 'content' and event == 'start':
            hash = str(int(elem.attrib.get('hash'), 16))
            dat = elem.attrib.get('includeTime')
            exchange_rate = ExchangeRate(get_curs_value(dat), datetime.now())
            exchange_rate_id = exchange_rate.save()
            content = Content(
                id=elem.attrib['id'],
                include_time=elem.attrib.get('includeTime'),
                entry_type=elem.attrib.get('entryType'),
                hash=hash,
                ts=elem.attrib.get('ts', None),
                urgency_type=elem.attrib.get('urgencyType', None),
                block_type=elem.attrib.get('blockType', None),
                exchange_rate_id=exchange_rate_id
            )
            continue
        elif elem.tag == 'decision' and event == 'end':
            decision = Decision(date=elem.attrib.get('date'), number=elem.attrib.get('number'),
                                org=elem.attrib.get('org'))
            decision_id = decision.save()
            content.decision_id = decision_id
        elif elem.tag == 'url' and event == 'end':
            content.url = elem.text.replace('\'', '\'\'')
            continue
        elif elem.tag == 'domain' and event == 'end':
            unique_domains.add(elem.text)
            domain = Domain(domain=elem.text)
            domain_id = domain.save()
            content.domain_id = domain_id
            continue
        elif elem.tag == 'ipSubnet' and event == 'end':
            content.ip_subnet = elem.text
            continue
        elif elem.tag in ['ip', 'ipv6'] and event == 'end':
            ip = Ip(type=elem.tag, ip=elem.text)
            ip_id = ip.save()
            content_ip = ContentIp(content_id=content.id, ip_id=ip_id)
            content_ip.save()
            continue
        elif elem.tag == 'content' and event == 'end':
            content.save()
            counter += 1
            elem.clear()
            print(content.id)
            content = None

    print(f'Количествово обработанных объектов: {counter}')
    print(f'Количествово уникальных доменов первого уровня: {len(unique_domains)}')


@time_of_function
def main():
    parse_xml('dump.xml')


if __name__ == '__main__':
    main()
