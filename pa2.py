import time

st = time.time()

filename = 'reviews_sample.txt'
f = open(filename, 'r')
review_to_support = {}
review_term_to_projectdb = {}
review_to_projectdb = {}
support_list = {}
tdb = []
record_no = 0
min_support = 0.01
if f is None:
    print('File not found')
    exit(-1)
while line := f.readline().strip().split(' '):
    if line[0] == '':
        break
    else:
        # print(line)
        record_no += 1
        tdb.append(line)
        for review_term in dict.fromkeys(line):
            if review_term in review_to_support:
                review_to_support[review_term] += 1
                review_term_to_projectdb[review_term].append(record_no-1)
            else:
                review_to_support[review_term] = 1
                review_term_to_projectdb[review_term] = [record_no-1]
f.close()

f_part3 = open('patterns_3.txt', 'w')
k = 1
fs = [[], []]
ct = [[], []]
cs = [[], []]
fs1_list = []
idx = 0
for i in review_to_support.keys():
    if review_to_support[i] >= record_no * min_support:
        fs[1].append([idx])
        review_to_projectdb[str(idx)] = review_term_to_projectdb[i]
        ct[1].append(review_to_support[i])
        f_part3.write('{}:{}\n'.format(review_to_support[i], i))
    idx += 1
    fs1_list.append(i)
print(len(fs[1]))

tdb_new = []
for i in tdb:
    tdb_new.append([])
    for j in i:
        tdb_new[-1].append(fs1_list.index(j))


def check_exists(l, lookup_list):
    for idx in range(len(l) - len(lookup_list) + 1):
        if l[idx:idx + len(lookup_list)] == lookup_list:
            return True
    return False


cs_last_set = {str(i[0]) for i in fs[1]}

while len(fs[k]) != 0:
    cs.append([])
    cs_current_set = set()
    c = 0
    # for s in fs[k]:
    #     c += 1
    #     print('Generating {}th candidate for len={}'.format(c, k + 1))
    #     for review_term in range(len(fs1_list)):
    #         t = s.copy()
    #         t.append(review_term)
    #         # if not t in cs[k + 1]:
    #
    #         cs[k + 1].append(t)

    if k == 1:
        for row in tdb_new:
            for col in range(0, len(row) - 1):
                candidate = [row[col], row[col+1]]
                hashable_str = ' '.join(str(e) for e in [row[col], row[col+1]])
                if str(row[col]) in cs_last_set and \
                   str(row[col+1]) in cs_last_set and \
                   hashable_str not in cs_current_set:
                    cs[k + 1].append(candidate)
                    cs_current_set.add(hashable_str)
    else:
        for s in fs[k]:
            for t in fs[k]:
                for z in [0]:
                    def test_and_add(candidate):
                        hashable_str = ' '.join(str(e) for e in candidate)
                        if hashable_str not in cs_current_set:
                            prune = False
                            for l in [0, len(candidate) - 1]:
                                candidate_minus_one = candidate[0:l] + candidate[l + 1:]
                                hashable_minus_one_str = ' '.join(str(e) for e in candidate_minus_one)
                                if hashable_minus_one_str not in cs_last_set:
                                    prune = True
                                    break
                            if prune:
                                print('Pruned {}'.format(candidate))
                                return
                            cs[k + 1].append(candidate)
                            cs_current_set.add(hashable_str)
                            global c
                            c += 1
                            if c % 10000 == 0:
                                print('Generating {}th candidate for len={}'.format(c, k + 1))
                    if s[0:z] + s[z + 1:] == t[0:-1]:
                        candidate = s[0:] + [t[-1]]
                        test_and_add(candidate)
                    # if s[0:z] + s[z + 1:] == t[1:]:
                    #    candidate = [t[0]] + s[0:]
                    #    test_and_add(candidate)
    print(len(cs[k + 1]))
    fs.append([])
    ct.append([])
    for cand in cs[k + 1]:
        count = 0
        hashable_str_last = ' '.join(str(e) for e in cand[:-1])
        hashable_str = hashable_str_last + ' ' + str(cand[-1])
        review_to_projectdb[hashable_str] = []
        projected_db = [i for i in review_to_projectdb[hashable_str_last]]
        for x in projected_db:
            if check_exists(tdb_new[x], cand):
                count += 1
                review_to_projectdb[hashable_str] += [x]
        if count >= record_no * min_support:
            fs[k + 1].append(cand)
            ct[k + 1].append(count)
            print('Found one count with min_support 0.01 {}'.format(cand))
            f_part3.write('{}:'.format(count))
            str_to_print = ''
            for z in cand:
                str_to_print += '{};'.format(fs1_list[z])
            f_part3.write('{}\n'.format(str_to_print[:-1]))

    print(len(fs[k + 1]))
    print(len(ct[k + 1]))
    k += 1
    cs_last_set = cs_current_set
    print('k={}'.format(k))
print(fs)
print(ct)

f_part3.close()

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
