#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.parse import urlencode

import requests

__author__ = 'ghostly峰'
__time__ = '2018/7/13 15:02'
import urllib.parse
import json
import csv
from lxml import etree

# job = 'python数据分析'
# city = '北京'
# distr = '朝阳区'
# exp = '3年及以下'
# edu = '本科'
# industry = '移动互联网'

def max_page_get(job, city):
    s = requests.session()
    s.trust_env = False
    s.verify = False
    url = f"https://www.lagou.com/jobs/list_{coding(job)}"
    headers = {
        'Connection': 'keep-alive',
        'Origin': 'https://www.lagou.com',
        'X-Anit-Forge-Code': '0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Anit-Forge-Token': 'None',
        'Referer': f'https://www.lagou.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    params = {
        'px': 'default',
        'city': city
    }
    cookies = {
        '_ga': 'GA1.2.412882275.1531464030',
        'user_trace_token': '20180713144029-a2007481-8667-11e8-9dec-5254005c3644',
        'LGUID': '20180713144029-a20077ab-8667-11e8-9dec-5254005c3644',
        'index_location_city': '%E5%8C%97%E4%BA%AC',
        'JSESSIONID': 'ABAAABAAAIAACBIDBB10AA586CC41EFE150EAEDB9C74F5B',
        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1531464030,1531467901,1531467968,1531973904',
        '_gid': 'GA1.2.596202421.1531973904',
        'X_HTTP_TOKEN': '4f6693ccf19b4cd64300278ca6d739f6',
        '_gat': '1',
        'LGSID': '20180719163131-23afaf35-8b2e-11e8-9e47-5254005c3644',
        'PRE_UTM': '',
        'PRE_HOST': '',
        'PRE_SITE': '',
        'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F',
        'TG-TRACK-CODE': 'index_search',
        'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1531989143',
        'LGRID': '20180719163224-42ebc35e-8b2e-11e8-9ea0-525400f775ce',
        'SEARCH_ID': '91706ff6784445459b8d786a9c2c6b24'
}
    r = s.post(url, headers=headers, params=params, cookies=cookies)
    tree = etree.HTML(r.text)
    max_page = tree.xpath('//*[@id="order"]/li/div[4]/div[3]/span[2]')[0].text
    return max_page


def coding(param):
    return urllib.parse.quote(param)

# def options():
#
#     jobs_li = ['python数据分析', '算法工程师', '数据挖掘', '深度学习', '机器学习']
#     citys_li = {'北京':['海淀区', '朝阳区', '昌平区'], '上海':['浦东新区', '徐汇区', '长宁区'], '深圳':['南山区', '福田区', '宝安区'], '广州':['天河区', '海珠区', '越秀区'], '杭州':['西湖区', '滨江区', '余杭区'], '成都':['高新区', '锦江区', '武侯区']}
#     experiences_li = ['应届毕业生', '3年及以下', '3-5年', '5-10年', '10年以上', '不要求']
#     education_li = ['大专', '本科', '硕士', '博士', '不要求']
#     industrys_li = ['移动互联网', '电子商务', '金融', '教育' ,'文化娱乐']
#     for j in jobs_li:
#         for c in citys_li.keys():
#             for d in citys_li[c]:
#                 for ex in experiences_li:
#                     for ed in education_li:
#                         for i in industrys_li:
#
#                             r = s.post(url=url, headers=headers, params=params, data=data, cookies=cookies)
#                             dataSave(r)

def param_upload(job, city, ex, ed, pn):
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    headers = {
        'Connection': 'keep-alive',
        'Origin': 'https://www.lagou.com',
        'X-Anit-Forge-Code': '0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Anit-Forge-Token': 'None',
        'Referer': f'https://www.lagou.com/jobs/list_{coding(job)}?px=default&gj={coding(ex)}&xl={coding(ed)}&city={coding(city)}',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    params = {
        'px': 'default',
        'gj': ex,
        'xl': ed,
        'city': city,
        'needAddtionalResult': 'false'
    }
    data = {
        'first': 'true',
        'pn': pn,
        'kd': job
    }

    # cookies = {
    #     'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1531464030,1531467901,1531467968',
    #     'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1531653298',
    #     'LGRID': '20180715191458-4f0f06f8-8820-11e8-9dec-5254005c3644',
    #     'SEARCH_ID': '872c4d588d3741b495564cd563a3c17d'
    # }
    cookies = {
        '_ga': 'GA1.2.412882275.1531464030',
        'user_trace_token': '20180713144029-a2007481-8667-11e8-9dec-5254005c3644',
        'LGUID': '20180713144029-a20077ab-8667-11e8-9dec-5254005c3644',
        'index_location_city': '%E5%8C%97%E4%BA%AC',
        'JSESSIONID': 'ABAAABAAAIAACBIDBB10AA586CC41EFE150EAEDB9C74F5B',
        'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1531464030,1531467901,1531467968,1531973904',
        '_gid': 'GA1.2.596202421.1531973904',
        'X_HTTP_TOKEN': '4f6693ccf19b4cd64300278ca6d739f6',
        '_gat': '1',
        'LGSID': '20180719163131-23afaf35-8b2e-11e8-9e47-5254005c3644',
        'PRE_UTM': '',
        'PRE_HOST': '',
        'PRE_SITE': '',
        'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F',
        'TG-TRACK-CODE': 'index_search',
        'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1531989143',
        'LGRID': '20180719163224-42ebc35e-8b2e-11e8-9ea0-525400f775ce',
        'SEARCH_ID': '91706ff6784445459b8d786a9c2c6b24'
    }
    return url, headers, params, data, cookies

if __name__ == '__main__':
    s = requests.session()
    s.trust_env = False
    s.verify = False
    jobs_li = ['python爬虫', 'Django', 'django', 'python数据分析', '数据分析', '图像处理', '图像识别', '语音识别', '计算机视觉', '自然语言处理' 'python算法工程师', 'python数据挖掘', '数据挖掘', '深度学习', '机器学习', 'AI工程师', 'ai工程师', 'AI', 'ai']
    city_li = ['北京', '上海', '深圳', '广州', '杭州', '成都', '武汉', '南京', '西安']
    exp_li = ['3年及以下','3-5年','5-10年','不要求']
    edu_li = ['大专', '本科', '硕士','博士','不要求']
    with open('lago.csv', 'wt', encoding='utf-8') as f:
        field_li = ['positionName','workYear','education','jobNature','financeStage','industryField','companyShortName','city','salary','district','createTime','positionLables','companySize','firstType','secondType','isSchoolJob']
        r_li = [j for j in range(len(field_li))]
        info = csv.writer(f)
        info.writerow(field_li)
        for j in jobs_li:
            for c in city_li:
                for ex in exp_li:
                    for edu in edu_li:
                        mp = int(max_page_get(j, c))
                        for pn in range(1, mp+1):
                            url, headers, params, data, cookies = param_upload(j, c, ex, edu, pn)
                            r = s.post(url=url, headers=headers, params=params, data=data, cookies=cookies)
                            json_data = json.loads(r.text)
                            res = json_data["content"]["positionResult"]['result']
                            for row in res:
                                for field in row:
                                    if field in field_li:
                                        i = field_li.index(field)
                                        r_li[i] = row.get(field)
                                info.writerow(r_li)
                                r_li = [j for j in range(len(field_li))]

