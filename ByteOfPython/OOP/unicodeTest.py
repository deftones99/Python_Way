f = open('abc.txt', 'wt', encoding='UTF-8')
f.write(u"你好dd")
f.close()

text = open('abc.txt', encoding='utf-8').read()

print(text)