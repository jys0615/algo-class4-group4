#### 백트래킹 ####
"""
모든 경우의 수를 확인해야 할 때 
    for로는 확인 불가한 경우(깊이가 달라질 때)

트리 방식으로 동작. 재귀함수를 구현.
"""

##### 15649 #####
"""
아이디어
    1부터 N 중에 하나를 선택한 뒤, 
    다음 1부터 N 선택할 때 이미 선택한 값이 아닌 경우 선택
    M개를 선택할 경우 프린트

시간복잡도
    중복이 가능: N^N
    중복이 불가: N!

자료구조
    방문 여부 확인 배열 int[]
    선택한 값 입력 배열 bool[]
"""

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# rs = []
# chk = [False]*(N+1) # 결괏값이 1,2 ,, 2,3 이런 식으로 저장. 

# def recur(num):
#     if num == M:
#         print(' '.join(map(str, rs)))
#         return
    
#     for i in range(1, N+1):
#         if chk[i] == False:
#             chk[i] = True
#             rs.append(i)
#             recur(num+1)
#             chk[i] = False
#             rs.pop()

# recur(0)


#### 1번 대비 템플릿 #####
from collections import Counter, defaultdict
### 1. Counter ###
arr = ['leo', 'kiki', 'eden', 'kiki', 'leo', 'leo']
cnt = Counter(arr)
print(cnt) # Counter({'leo': 3, 'kiki': 2, 'eden': 1})
print(cnt['leo'])
print(cnt["no"]) # 아예 없는 키에 대해서는 0이 나옴. 
print(cnt.most_common(1)) # [('leo', 3)]
print(cnt.most_common(1)[0][0]) # leo
print(cnt.most_common(1)[0][1]) # 3

# 두 목록 차이
A = ['leo', 'kiki', 'eden', 'kiki', 'leo']
B = ['leo', 'kiki', 'kiki']
result = Counter(A) - Counter(B)
print(result)
print(list(result.keys())) # 키에 대해서만 리스트 형태로
print(list(result.keys())[0]) # 이러한 리스트 중에서 첫번째 원소만
print(result.values())

### 2. defaultdict ###

# 그룹핑
d = defaultdict(list)
data = [('과일', '사과'), ('채소', '당근'), ('과일', '바나나')]
for key, value in data:
    d[key].append(value)
print(d['과일'])
print(d['고기']) # 없는 거에 대해서는 [] 공백 출력

# 카운팅
d2 = defaultdict(int)
print("d2")
print(d2)
for x in ['a', 'b', 'a', 'c', 'a']:
    d2[x] +=1
print("d2")
print(d2)
print(d2['a'])
print(d2['gggg']) # 0

# ============================================
# 3. sorted(key=lambda)
# ============================================
arr = [('Alice', 90), ('Bob', 95), ('Charlie', 90)]

# 단일 조건
print(sorted(arr, key=lambda x: x[1]))
# [('Alice', 90), ('Charlie', 90), ('Bob', 95)]

print(sorted(arr, key=lambda x: x[1], reverse=True))
# [('Bob', 95), ('Alice', 90), ('Charlie', 90)]

# 다중 조건: 점수 내림차순, 같으면 이름 오름차순
print(sorted(arr, key=lambda x: (-x[1], x[0])))
# [('Bob', 95), ('Alice', 90), ('Charlie', 90)]

# 문자열 커스텀 정렬 (가장 큰 수)
nums = ['3', '30', '34', '5', '9']
print(sorted(nums, key=lambda x: x*3, reverse=True))
# ['9', '5', '34', '3', '30']
print(''.join(sorted(nums, key=lambda x: x*3, reverse=True)))
# 9534330

