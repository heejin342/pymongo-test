a = 'spartacodingclub@gmail.com'

def get_mail(s):
    return s.split('@')[1].split('.')[0]


print(get_mail(a))

