from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    result = []
    
    for item in course:
        counter = defaultdict(int) 
        
        for order in orders:
            for combo in combinations(sorted(order), item):
                counter[combo] += 1
        
        if not counter:
            continue
            
        max_cnt = max(counter.values())
        
        if max_cnt >= 2:
            for k, v in counter.items():
                if v == max_cnt:
                    result.append("".join(k))
    
    return sorted(result)