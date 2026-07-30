class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            count = [0] * 26

            for c in word:
                # increment the correct position
                # e.g. index = "e"/101 - "a"/97 = 4 for e's position
                count[ord(c) - ord("a")] += 1   

            signature = tuple(count)

            # If signature isn't in dict...
            if signature not in groups:
                groups[signature] = []

            # Append word
            groups[signature].append(word)
        
        return list(groups.values())