from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        for i in range(2,len(coordinates)): 
            if (coordinates[i][1] - coordinates[1][1])*(coordinates[1][0]-coordinates[0][0])  != (coordinates[1][1] - coordinates[0][1]) * (coordinates[i][0] - coordinates[1][0]):
                return False
        return True

if __name__ == "__main__":
    coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    print(Solution().checkStraightLine(coordinates)) # True

