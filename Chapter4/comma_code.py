spam = ['apples', 'bananas', 'tofu', 'cats']
group = []
for i in range(len(spam)-1):
    group.append(spam[i])
print (', '.join(group),'and ' +spam[-1])
