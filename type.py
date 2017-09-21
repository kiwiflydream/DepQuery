#!/usr/bin/env python
# encoding: utf-8

import sys
from collections import OrderedDict

from pyquery import PyQuery as pq
from workflow import Workflow

log = None
# 构建工具类型
types = OrderedDict([('Maven', 'maven-a'), ('Gradle', 'gradle-a'), ('Ivy', 'ivy-a')])


# types = {'Maven': 'maven-a', 'Gradle': 'gradle-a', 'SBT': 'sbt-a', 'Ivy': 'ivy-a', 'Grape': 'grape-a',
#          'Leiningen': 'leiningen-a', 'Buildr': 'buildr-a'}


def main(wf):
    # 获得参数
    params = wf.args[0]
    # params = "http://mvnrepository.com/artifact/org.springframework/spring-context/5.0.0.RC2"
    doc = pq(params)
    for type_ in types.keys():
        type_id = types[type_]
        dependency = doc('#' + type_id).text()
        wf.add_item(title=type_, subtitle=u'选择后自动复制到粘贴板', arg=dependency, valid=True, icon='icon/' + type_id + '.png')
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
