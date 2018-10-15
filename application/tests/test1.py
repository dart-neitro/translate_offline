"""
ff
"""


class Test(object):

    def __enter__(self):
        print('enter')

    def __del__(self):
        print('del')

    def __exit__(self, exception_type, exception_value, traceback):
        print('exit')


with Test() as f:
    1 / 0

print('instance')

t = Test()

print('The end')