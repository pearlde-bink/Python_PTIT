mail = open('CONTACT.in')
a = {i.lower().strip() for i in mail}
print(*sorted(a), sep = '\n')