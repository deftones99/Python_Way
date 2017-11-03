# 测试是否为回文，通过切片，第三个参数为步长，步长为-1时将反转文本

def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter text:")

if is_palindrome(something):
    print("Yes it is a palindrome")

else:
    print("No ,it is not a palindrome")
