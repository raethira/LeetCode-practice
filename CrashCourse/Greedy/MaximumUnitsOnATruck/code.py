class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        maxUnits = 0

        for numberOfBoxesi, numberOfUnitsPerBoxi in boxTypes:

            if truckSize > 0:
                boxesLefti = min(truckSize, numberOfBoxesi)

                maxUnits += boxesLefti * numberOfUnitsPerBoxi
                truckSize -= boxesLefti

        return maxUnits
