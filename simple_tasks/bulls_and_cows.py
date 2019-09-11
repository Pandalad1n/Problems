class Solution:
    def getHint(self, secret, guess):
        cows = 0
        bulls = 0
        excluded_ids = []

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                excluded_ids.append(i)

        for i in range(len(secret)):
            for j in range(len(secret)):
                if j in excluded_ids or i in excluded_ids:
                    continue
                if secret[i] == guess[j]:
                    cows += 1
                    excluded_ids.append(j)
                    break

        return str(bulls) + "A" + str(cows) + "B"

print(Solution().getHint("1123", "0111"))