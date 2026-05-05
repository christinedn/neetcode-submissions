from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1count = defaultdict(int)
        for c in s1:
            s1count[c] += 1
        
        have, need = 0, len(s1count)
        s2count = defaultdict(int)

        # build initial window
        for i in range(len(s1)):
            s2count[s2[i]] += 1

        # count how many required chars match in the initial window
        for char in s1count:
            if s1count[char] == s2count[char]:
                have += 1

        if have == need:
            return True

        l = 0

        for r in range(len(s1), len(s2)):
            right_char = s2[r]
            s2count[right_char] += 1

            if right_char in s1count:
                if s1count[right_char] == s2count[right_char]:
                    have += 1
                elif s2count[right_char] == s1count[right_char] + 1:
                    have -= 1

            left_char = s2[l]
            s2count[left_char] -= 1

            if left_char in s1count:
                if s1count[left_char] == s2count[left_char]:
                    have += 1
                elif s2count[left_char] == s1count[left_char] - 1:
                    have -= 1

            l += 1

            if have == need:
                return True

        return False