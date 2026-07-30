class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Unoptomized version - sorting like that costs O(nlog(n))
        groups = {}

        for word in strs:
            # Create signature
                # Sort the word alphabetically
            signature = tuple(sorted(word))

            # If signature isn't in dict...
            if signature not in groups:
                groups[signature] = []


            # Append word
            # > groups["key"].append(value)
            groups[signature].append(word)

        return list(groups.values())