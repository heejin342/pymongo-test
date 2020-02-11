a = 'spartacodingclub@gmail.com'

def check_mail(s):
    return s.find('@') > -1

#결과값
print(check_mail(a))
