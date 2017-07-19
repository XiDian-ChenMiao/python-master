# coding:utf-8
import requests
import re

if __name__ == '__main__':
    response = requests.get('http://www.maiziedu.com/course/list/?catagory=')
    # print(response.text)
    courses = re.findall(r'<a  href="/course/list/all-\w+/0-1/">(.*?)</a>', response.text, re.S)
    # print('结果类型为：', type(courses))
    print('麦子学院所开设的课程为：')
    for course in courses:
        print(course)

    # 通过get来绑定参数信息
    data = {'page': '2'}
    res = requests.get('http://www.imooc.com/course/list', data)
    mooc_courses = re.findall(r'data-ct=fe>(.*?)</a>', res.text, re.S)
    print('慕课网所开设的课程为：')
    for mooc_course in mooc_courses:
        print(mooc_course)

    for i in range(20):
        response = requests.get('http://www.imooc.com/course/list?page=' + str(i))
