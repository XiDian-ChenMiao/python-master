# coding:utf8
class Run:
    def __init__(self):
        pass

    def run(self):
        print('Run')


class RunQuick(Run):
    def __init__(self):
        pass

    def run(self):
        print('Run Quick')


class RunSlow(Run):
    def __init__(self):
        pass

    def run(self):
        print('Run Slow')


class StrategyByClass:
    """
    通过类来实现策略模式
    """
    def __init__(self):
        pass

    def set_runable(self, runable):
        self.runnable = runable()

    def run(self):
        self.runnable.run()


def run_quick():
    print('Run Quick')


def run_slow():
    print('Run Slow')


class StrategyByFunction:
    """
    通过函数来实现策略模式
    """
    def __init__(self):
        pass

    def set_runable(self, runable):
        self.runnable = runable

    def run(self):
        self.runnable()


if __name__ == '__main__':
    strategy = StrategyByClass()
    strategy.set_runable(RunQuick)
    strategy.run()

    strategy.set_runable(RunSlow)
    strategy.run()

    strategy = StrategyByFunction()
    strategy.set_runable(run_quick)
    strategy.run()

    strategy.set_runable(run_slow)
    strategy.run()
