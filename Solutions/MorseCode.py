import types


class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        fin = []
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = []
        for letter in range(97,123):
            alphabet.append(chr(letter))
        ref = dict(zip(alphabet, morse))

        if not words:
            return 0
        if words:
            sml = str()
            lrg = []
            for i in range(len(words)):
                cur = words[i]
                for j in range(len(cur)):
                    n = ref[cur[j]]
                    sml += n
                lrg.append(sml)
                sml = str()
        for t in lrg:
            if t not in fin:
                fin.append(t)
        return len(fin)
