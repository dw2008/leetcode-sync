class Solution:
    #input: int array gain of length 1 <= n <= 100; different altitudes
    #output: highest altitude of a point
    #strategy: use prefix sum, and iterate through gain. keep track of a net gain of altitude, and also have a maximum altitude. update the maximum if net altitude is higher than current max for each iteration
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        current = 0

        for i in range(len(gain)):
            current += gain[i]
            highest = max(current, highest)

        return highest