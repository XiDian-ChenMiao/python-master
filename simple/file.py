# coding:utf-8
import io
import os
import re
# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便。
if __name__ == '__main__':
    f = open('python-regex.py', 'r', encoding='utf-8')
    # print('读取全部内容：')
    # print(f.read())
    print('默认缓存字节数为：', io.DEFAULT_BUFFER_SIZE)
    f.seek(0, os.SEEK_SET)
    print('读取前100个字节内容：')
    print(f.read(100))
    print('当前文件指针位置为：', f.tell())
    f.close()

    # f = open('file.py', 'r', encoding='utf-8')
    # wf = open('w-' + f.name, 'w+', encoding='utf-8')
    # iter_f = iter(f)
    # for line in iter_f:
    #     print(line.strip('\n'))
    #     wf.write(line)
    # f.close()  # 显式的调用close或者flush方法才能将缓存中的数据同步到磁盘中
    # wf.close()

    print('当前文件名称：', __file__)
    print('当前文件是否存在：', os.path.exists(__file__))
    print('是否为一个目录：', os.path.isdir(__file__))
    print('是否为一个文件：', os.path.isfile(__file__))
    print('当前文件的后缀名为：', os.path.splitext(__file__)[1])
    print('当前文件大小：', os.path.getsize(__file__))
    print('路径目录为：', os.path.dirname(__file__))
    print('路径文件名为：', os.path.basename(__file__))
    print('当前路径下的文件为：', os.listdir(os.path.dirname(__file__)))
    print('系统名称：', os.name)  # 如果为nt，则表明为Windows系统；如果为posix，则说明系统为linux，unix或者mac os
    print('当前绝对路径为：', os.path.abspath('.'))
    print('所有环境变量：', os.environ)
    pattern = re.compile('%(\w+)%')
    all_paths = os.environ.get('PATH').split(';')
    for path in all_paths:
        match = pattern.match(path)
        if match:
            print(os.environ.get((match.group(1))) or '配置已经丢失')
        else:
            print(path)
