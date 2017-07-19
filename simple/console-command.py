# coding:utf-8
# Version: 0.1
# Author: DAQINZHIDI
# License: Copyright(c) 2016 Miao.Chen
# Summary: 控制台参数传递

import click


@click.command()
@click.option('--count', default=1, help='Number of greetings')
@click.option('--name', prompt='Your name', help='The person to greet')
def hello(count, name):
    for x in range(count):
        click.echo('Hello %s' % name)


@click.command()
@click.option('--rate', type=float, help='rate')
def show(rate):
    click.echo('rate: %s' % rate)


@click.command()
@click.option('--gender', type=click.Choice(['man', 'woman']), help='gender')
def choose_gender(gender):
    click.echo('gender: %s' % gender)


@click.command()
@click.option('--center', nargs=2, type=float, help='center of circle')
@click.option('--radius', type=float, help='radius of circle')
def circle(center, radius):
    click.echo('center: %s, radius: %s' % (center, radius))


@click.command()
@click.password_option()
def input_password(password):
    click.echo('password: %s' % password)


def print_version(ctx, param, value):
    click.echo('param: %s' % param)
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0.0')
    ctx.exit()


@click.command()
# is_eager=True: 表明该命令行选项优先级高于其他选项
# expose_value=False: 表示如果没有输入该命令行选项，会执行既定的命令行流程
# callback: 指定了输入该命令行选项时，要跳转执行的函数
@click.option('--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True)
@click.option('--name', default='Chen Miao', help='name')
def say_hello(name):
    click.echo('Hello %s!' % name)


@click.command()
@click.argument('src', nargs=-1)  # 表示接收不定量的参数，参数值以元组的形式传入
@click.argument('dst', nargs=1)
def move(src, dst):
    click.echo('move %s to %s' % (src, dst))


@click.command()
@click.option('--name', help='The person to greet')
def say_hello_with_color(name):
    click.secho('Hello %s!' % name, fg='red', underline=True)
    click.secho('Hello %s!' % name, fg='yellow', bg='blue')


if __name__ == '__main__':
    say_hello_with_color()
