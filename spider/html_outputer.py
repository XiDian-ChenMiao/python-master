# coding:utf-8
"""
Created on 2016年8月29日
@author: Administrator
"""


class HtmlOutputer:
    """
    HTML的输出器
    """
    def __init__(self):
        self.datas = []

    '''收集信息的函数'''

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    '''将信息以HTML页面的形式显示出来'''

    def output(self):
        fout = open('result.html', 'w')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table border="1" cellpadding="0">')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()
