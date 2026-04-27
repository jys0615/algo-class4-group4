import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    str1 = input()
    left = []
    right = []
    for item in str1:
        if item == "<":
            if left:
                right.append(left.pop())
        elif item == ">":
            if right:
                left.append(right.pop())
        elif item == "-":
            if left:
                left.pop()
        else:
            left.append(item)
    left.extend(reversed(right))
    print(''.join(left))

### .extend란? 가장 바깥쪽 iterable의 모든 항목을 넣는다.
### .append란? iterable 전체를 하나의 항목으로 넣는다.
### reversed()란? iteravle의 역순을 출력한다. 원본 변경은 아님
### iterable이란? 반복 가능한 객체. list, tuple, set, dict 등이 있다.