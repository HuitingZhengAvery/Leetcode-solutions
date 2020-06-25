class Solution:
    def f(self, string):
        if string == None:
            return
        string1 = sorted(string)
        count = 1
        if len(string) > 1:
            for i in range(1, len(string)):
                if string1[i] == string1[i - 1]:
                    count += 1
                else:
                    break
        return count
    def helper(self, l, r, thelist, target):
        if l >= r:
            if thelist[l] > target:
                return len(thelist) - r
            else:
                return 0

        mid = (l+r) // 2
        if thelist[mid] > target:
            return self.helper(l, mid, thelist, target)
        else:
            return self.helper(mid + 1, r, thelist, target)
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        answer = []
        for i in range(len(words)):
            words[i] = self.f(words[i])
        words_sorted = sorted(words)

        for i in range(len(queries)):
            cur = self.f(queries[i])
            answer.append(self.helper(0, len(words_sorted) - 1, words_sorted, cur))
        return answer
