# 自定义输入过短异常，继承Python原声异常

class ShortInputException(Exception):
    def __init__(self, length, atLeast):
        Exception.__init__(self)
        self.length = length
        self.atLeast = atLeast


try:
    text = input('Enter your command here:')

    if len(text) < 3:
        raise ShortInputException(len(text), 3)

except EOFError:
    print('This cause a EOFError')

except ShortInputException as ex:
    print(('ShortInputException :The input was ' +
           '{} long,excepted at least {}').format(ex.length, ex.atLeast))

else:
    print('No Exception Found!')