class Solution:
    def frequencySort(self, s: str) -> str:
        # Count character frequencies
        HM = Counter(s)
        # Create bucket
        max_freq = max(HM.values())
        buckets = [[] for _ in range(max_freq + 1)]
        # Fill buckets
        for char, freq in HM.items():
            buckets[freq].append(char)
        # Build result from high to low
        result = []
        for freq in range(max_freq, 0, -1):
            for char in buckets[freq]:
                result.append(char * freq)

        return "".join(result)