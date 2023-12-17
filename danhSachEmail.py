mail = open('CONTACT.in')
a = {i.lower().strip() for i in mail.readlines()}
print(*sorted(a), sep = '\n')