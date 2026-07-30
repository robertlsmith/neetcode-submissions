class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Optimized version - looping like this costs O(n)
        groups = {}

        for word in strs:
            count = [0] * 26

            for c in word:
                # Convert the letter to its alphabet index.
                # Example: ord("e") - ord("a") = 101 - 97 = 4
                count[ord(c) - ord("a")] += 1   

            signature = tuple(count)

            # If signature isn't in dict...
            if signature not in groups:
                groups[signature] = []

            # Append word
            groups[signature].append(word)
        
        return list(groups.values())