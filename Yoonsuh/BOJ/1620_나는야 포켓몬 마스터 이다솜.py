import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemon = [input().rstrip() for _ in range(N)]
for _ in range(M):
    q = input().rstrip()
    if q.isdigit():
        print(pokemon[int(q)-1])
    else:
        print(pokemon.index(q)+1)

## isdigit -> 문자열이 숫자로만 이루어져 있는가?
## list.index('str') -> 리스트나 문자열에서 특정 값의 첫번째 위치를 반환.