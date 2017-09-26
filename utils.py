#!/usr/bin/env python
# encoding: utf-8
import socket
import sys
import time

from pyquery import PyQuery as pq
from workflow import Workflow, ICON_CLOCK, ICON_NETWORK, ICON_WARNING


# 获得外网ip
def get_web_ip():
    doc = pq('http://ip.chinaz.com')
    return doc('.fz24').text()


# 获得本地ip
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def main(wf):
    # 获得参数
    params = wf.args[0]
    # 解析参数
    params_arr = str(params).split(':')
    # 获得关键字
    key = params_arr[0]
    # 获得其它参数
    is_have_other = len(params_arr) > 1
    if is_have_other:
        other_params = params_arr[1]
    items = []

    if key == 'time':

        if is_have_other and (len(other_params) == 10 or len(other_params) == 13):
            time_t = float(other_params)
            if len(other_params) == 13:
                time_t = time_t / 1000
            items.append(
                {'title': u'时间戳 -> 日期', 'subtitle': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_t)),
                 'icon': ICON_CLOCK})
        else:
            items.append({'title': u'时间戳(秒)', 'subtitle': str(int(time.time())), 'icon': ICON_CLOCK})
            items.append({'title': u'时间戳(毫秒)', 'subtitle': str(int(time.time() * 1000)), 'icon': ICON_CLOCK})
            items.append(
                {'title': u'当前日期', 'subtitle': time.strftime("%Y-%m-%d", time.localtime()), 'icon': ICON_CLOCK})
            items.append(
                {'title': u'当前时间', 'subtitle': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                 'icon': ICON_CLOCK})
            items.append(
                {'title': u'当前时间', 'subtitle': time.strftime("%Y%m%d%H%M%S", time.localtime()), 'icon': ICON_CLOCK})
            items.append(
                {'title': u'当前时间', 'subtitle': time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()),
                 'icon': ICON_CLOCK})
    elif key == 'ip':
        items.append({'title': u'本地IP', 'subtitle': get_host_ip(), 'icon': ICON_NETWORK})
        items.append({'title': u'外网IP', 'subtitle': get_web_ip(), 'icon': ICON_NETWORK})
    else:
        items.append({'title': u'尚不支持的关键字', 'subtitle': u'请更换关键字', 'icon': ICON_WARNING})

    for item in items:
        wf.add_item(title=item['title'], subtitle=item['subtitle'], arg=item['subtitle'], valid=True, icon=item['icon'])

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
