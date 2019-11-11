class Solution:
    def twoCitySchedCost(self, costs):
        sort = sorted(costs, key=lambda x: abs(x[0] - x[1]), reverse=True)
        awns = 0
        info = {
            'people': len(costs) // 2,
            'A': 0,
            'B': 0,
        }
        for cost in sort:
            if cost[0] < cost[1]:
                if info['A'] < info['people']:
                    info['A'] += 1
                    awns += cost[0]
                else:
                    awns += cost[1]
            else:
                if info['B'] < info['people']:
                    info['B'] += 1
                    awns += cost[1]
                else:
                    awns += cost[0]
        return awns


print(Solution().twoCitySchedCost([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]))

