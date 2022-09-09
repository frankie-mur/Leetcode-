class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties = [[-defense, attack] for attack, defense in properties]
        heapify(properties)
        currentMaxDefense, ans = -float('inf'), 0
        while properties:
            _, currentDefense = heappop(properties)
            if currentDefense < currentMaxDefense:
                ans += 1
            currentMaxDefense = max(currentMaxDefense, currentDefense)
        return ans