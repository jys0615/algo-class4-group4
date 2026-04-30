import sys
input = sys.stdin.readline

dwarf = [int(input().rstrip()) for _ in range(9)]

sumv = sum(dwarf)
found = False
for j in range(9):
    if found == True:
        break
    for i in range(j+1, 9):
        result = sumv - dwarf[j] - dwarf[i]
        if result == 100:
            fake1 = j
            fake2 = i
            found = True
            break

for idx, number in enumerate(dwarf):
    if idx!= fake1 and idx!=fake2:
        print(number)
"""
기존 방식은 값을 가져다가 제거하는 방식인데 이 방식은 먼저 있는 걸 없애서 부정확
인덱스 기준으로 반복문을 돌려서 해당하는 값을 제거.
그리고 break를 2중 for문에서 사용할 때는 추가 장치가 필요. 위 상황에서 Break는
내부 반복문에 대해서만 탈출이 됨. 따라서 boolean 변수를 활용해서 외부 반복문 탈출도 명시를 해야 한다.
안 그러면 계속 외부 반복문이 돌아서 가짜 난쟁이들이 바뀌어서 오답이 발생한다.
"""