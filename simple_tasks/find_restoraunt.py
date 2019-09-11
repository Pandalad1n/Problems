class Solution:
    def findRestaurant(self, list1, list2):
        awns = []
        min_diff = len(list1) + len(list2)
        for i_1, v_1 in enumerate(max(list1, list2)):
            for i_2, v_2 in enumerate(min(list2, list1)):
                if v_1 == v_2:
                    if i_1 + i_2 < min_diff:
                        awns.clear()
                        min_diff = i_1 + i_2
                        awns.append(v_1)
                    elif i_1 + i_2 == min_diff:
                        awns.append(v_1)
        return awns

print(Solution().findRestaurant(
    ["Shogun", "Tapioca Express", "Burger King", "KFC"],
    ["KFC", "Burger King", "Tapioca Express", "Shogun"]
    ))
