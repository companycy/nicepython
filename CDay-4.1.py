# -*- coding: utf-8 -*-

import os
print os.listdir('/root')       # like ls -a, including hidden dir

# use help ('os.walk') to get usage of walk
# ex from help ('os.walk')
import os
from os.path import join, getsize
result = ''
resultList = []
for root, dirs, files in os.walk('/root/'):
    # result = root + ' consumes '
    # result += str(sum([getsize(join(root, name)) for name in files]))
    # result += ' bytes in' + str(len(files)) + ' non-dir files'
    # print result
    mysum = str(sum([getsize(join(root, name)) for name in files]))
    mylen = str(len(files))

    # todo: get AttributeError: __exit__ ?
    # with open('/tmp/output.log', 'a').write('{0} consumes {1} bytes in {2} non-dir files\n'.format(root, mysum, mylen)):
    #     pass                    # close after write

    # however, it's not good to open/close file frequently
    # should cache all string and write to file once out of loop
    # with open('/tmp/output.log', 'a') as f:
    #     f.write('{0} consumes {1} bytes in {2} non-dir files\n'.format(root, mysum, mylen))
    result += '{0} consumes {1} bytes in {2} non-dir files\n'.format(root, mysum, mylen)
    resultList.append('{0} consumes {1} bytes in {2} non-dir files\n'.format(root, mysum, mylen))

    if '.git' in dirs:
        dirs.remove('.git')      # skip .git dirs
    elif '.emacs.d' in dirs:     # todo: should be more pythonic
        dirs.remove('.emacs.d')

# print result
# print ''.join(resultList)


# test for list
# l = [1, 2, 3, 4]
# lc = l
# print l is lc
# l = []
# # del l[0:len(l)]
# # l[:] = []
# print l is lc
# print lc


# q6
result = []
with open('cdays-4-test.txt', 'r') as f:
    result = f.readlines()

def myfilter(line):
    line = line.strip()
    return line and line[0] != '#' # empty string is falsy
result = filter(myfilter, result)
with open('cdays-4-result.txt', 'w') as f:
    f.write(''.join(result))
