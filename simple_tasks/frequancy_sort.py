import collections

class Solution:
    def frequency_sort(self, s) -> str:
        awns = ''
        counted = collections.Counter(s).most_common()
        for c, q in counted:
            awns += c * q
        return awns


print(Solution().frequency_sort('sobaka'))
