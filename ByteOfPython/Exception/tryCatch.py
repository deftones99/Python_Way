try:
    text = input('Enter -->')

except EOFError:
    print('This cause a EOFError!')

except KeyboardInterrupt:
    print('This cause a KeyboardInterrupt Exception!')

else:
    print('You are enter {}'.format(text))
