

import re
from simhash import Simhash


def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]


print('%x' % Simhash(get_features('How are you? I am fine. Thanks.')).value)
print('%x' % Simhash(get_features('How are u? I am fine.     Thanks.')).value)
print('%x' % Simhash(get_features('How r you?I    am fine. Thanks.')).value)


from simhash import Simhash
print(Simhash('aa').distance(Simhash('bb')))
print(Simhash('aa').distance(Simhash('aa')))


