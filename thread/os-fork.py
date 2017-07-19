import os

pid = os.fork()
if pid < 0:
    print('create process failure')
elif pid == 0:
    print('child process id:', os.getpid(), ' parent process id:', os.getppid())
else:
    print('parent process id:', os.getpid())
