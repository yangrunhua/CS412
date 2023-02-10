filename = 'categories.txt'
f = open(filename, 'r')
category_to_support = {}
support_list = {}
tdb = []
if f is None:
    print('File not found')
    exit(-1)
while line := f.readline().split(';'):
    line[-1] = line[-1].split('\n')[0]
    if line[0] == '':
        break
    else:
        print(line)
        tdb.append(set(line))
        for cat in line:
            if cat in category_to_support:
                category_to_support[cat] += 1
            else:
                category_to_support[cat] = 1
f_part1 = open('patterns.txt', 'w')
#f_part2 = open('patterns_2.txt', 'w')
for (key, value) in category_to_support.items():
    if value > 771:
        f_part1.write('{}:{}\n'.format(value, key))
#    if value in support_list:
#        support_list[value].append(key)
#    else:
#        support_list[value] = [key]
f_part1.close()
#for (key, values) in support_list.items():
#    f_part2.write('{}:'.format(key))
#    for i in range(len(values) - 2):
#        f_part2.write('{};'.format(values[i]))
#    f_part2.write('{}\n'.format(values[-1]))
f.close()
#f_part2.close()
f_part2 = open('patterns_2.txt', 'w')
k = 1
fs = [[], []]
ct = [[], []]
cs = [[], []]
fs1_list = []
for i in category_to_support.keys():
    if category_to_support[i] > 771:
        fs[1].append({i})
        fs1_list.append(i)
        ct[1].append(category_to_support[i])
        f_part2.write('{}:{}\n'.format(category_to_support[i], i))
print(len(fs[1]))
while len(fs[k]) != 0:
  cs.append([])
  for s in fs[k]:
      for cat in fs1_list:
          if not cat in s:
              t = s.copy()
              t.add(cat)
              if not t in cs[k+1]:
                  cs[k+1].append(t)
  print(len(cs[k+1]))
  fs.append([])
  ct.append([])
  for cand in cs[k+1]:
      count = 0
      for x in tdb:
          if cand.issubset(x):
              count += 1
      if count > 771:
          fs[k+1].append(cand)
          ct[k+1].append(count)
          print('Found one count > 771 {}'.format(cand))
          f_part2.write('{}:'.format(count))
          str = ''
          for z in cand:
              str += '{};'.format(z)
          f_part2.write('{}\n'.format(str[:-1]))

  print(len(fs[k+1]))
  print(len(ct[k+1]))
  k += 1
  print('k={}'.format(k))
print(fs)
print(ct)

f_part2.close()

