class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        answer = []
        most_candy = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= most_candy:
                answer.append(True)
            else:
                answer.append(False)
        return answer

# OR

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        result = []
        for i in range(len(candies)):            
            result.append(candies[i] + extraCandies >= maxCandies)
        return result