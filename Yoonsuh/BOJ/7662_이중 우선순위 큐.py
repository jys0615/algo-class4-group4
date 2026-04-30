import sys
input = sys.stdin.readline
import heapq



### 시간 초과 발생 ###
# T = int(input())
# for _ in range(T):
#     k = int(input())
#     heap = []
#     for _ in range(k):
#         cmd, num = input().split()
#         if cmd == "I":
#             heapq.heappush(heap, int(num))
#         if cmd == "D":
#             if num == "1":
#                 if len(heap) != 0:
#                     maxv = max(heap)
#                     heap.remove(maxv)
#             else:
#                 if len(heap) != 0:
#                     heapq.heappop(heap)
#     if len(heap) == 0:
#         print("EMPTY")
#     else:
#         print(max(heap), heapq.heappop(heap))