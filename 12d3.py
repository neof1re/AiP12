d = {}
f = open('en-ru.txt', encoding='utf-8')
for line in f:
    line = line.replace('\n', '')
    line = line.replace('–', '-')
    if not line.strip() or ' - ' not in line:
        continue
    en, ru = line.split(' - ')
    words = ru.split(', ')
    for w in words:
        if w not in d:
            d[w] = []
        d[w].append(en)
f = open('ru-en.txt', 'w', encoding='utf-8')
for key in sorted(d):
    f.write(key + ' - ' + ', '.join(d[key]) + '\n')
f.close()