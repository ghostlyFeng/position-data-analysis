#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.parse import parse_qsl

__author__ = 'Terry'


def print_headers_raw_to_dict(headers_raw_l):
    print("{\n    '" + ",\n    ".join(map(lambda s: "'" +
        "': '".join(s.strip().split(': ')) + "'", headers_raw_l))[1:-1] + "'\n}")

def print_headers_raw_to_dict_space(headers_raw_l):
    print("{\n    '" + ",\n    ".join(map(lambda s: "'" + "': '".join(s.strip().split('\t') if len(s.strip().split('\t'))>1 else [s.strip(), '']) + "'", headers_raw_l))[1:-1] + "'\n}")

def print_dict_from_copy_headers(headers_raw):
    headers_raw = headers_raw.strip()
    headers_raw_l = headers_raw.splitlines()

    if 'HTTP/1.1' in headers_raw_l[0]:
        headers_raw_l.pop(0)
    if headers_raw_l[0].startswith('Host'):
        headers_raw_l.pop(0)
    if headers_raw_l[-1].startswith('Cookie'):
        headers_raw_l.pop(-1)

    if ':' in headers_raw_l[-1] and ':' in headers_raw_l[0]:
        print_headers_raw_to_dict(headers_raw_l)
    else:
        print_headers_raw_to_dict_space(headers_raw_l)

def print_url_params(url_params):
    s = str(parse_qsl(url_params.strip(), 1))
    print("OrderedDict(\n    " + "),\n    ".join(map(lambda s: s.strip(), s.split("),")))[1:-1] + ",\n)")

def print_url_params_new(url_params):
    l = parse_qsl(url_params.strip(), 1)
    print("{\n    " + "',\n    ".join(map(lambda s: "'"+s[0]+"': '"+s[1], l)) + "',\n}")

if __name__ == '__main__':
    text_fiddler = '''
_ga	GA1.2.412882275.1531464030
user_trace_token	20180713144029-a2007481-8667-11e8-9dec-5254005c3644
LGUID	20180713144029-a20077ab-8667-11e8-9dec-5254005c3644
index_location_city	%E5%8C%97%E4%BA%AC
JSESSIONID	ABAAABAAAIAACBIDBB10AA586CC41EFE150EAEDB9C74F5B
Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6	1531464030,1531467901,1531467968,1531973904
_gid	GA1.2.596202421.1531973904
X_HTTP_TOKEN	4f6693ccf19b4cd64300278ca6d739f6
_gat	1
LGSID	20180719163131-23afaf35-8b2e-11e8-9e47-5254005c3644
PRE_UTM	
PRE_HOST	
PRE_SITE	
PRE_LAND	https%3A%2F%2Fwww.lagou.com%2F
TG-TRACK-CODE	index_search
Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6	1531989143
LGRID	20180719163224-42ebc35e-8b2e-11e8-9ea0-525400f775ce
SEARCH_ID	91706ff6784445459b8d786a9c2c6b24
    '''

    print_dict_from_copy_headers(text_fiddler)


    url_params = 'tpl=mn&apiver=v3&tt=1522120193242&class=login&gid=047897E-B6A8-4FD1-841B-23C1952428DB&loginversion=v4&logintype=dialogLogin&traceid=&callback=bd__cbs__ma4ta7'
    # print_url_params_new(url_params)