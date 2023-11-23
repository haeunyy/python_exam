per = ["10.31", "", "8.00"]

new_per = [] # 리스트 초기화 

# 리스트 요소 옮겨 담기 
for i in per:
    try:
        new_per.append(float(i))
    except:
        new_per.append(0) # 오류 발생시 0 대입
        continue

# ZeroDivisionError 예외처리
for i in new_per:
    try:
        print(f"14를 {i}으로 나눈 값은 ?".ljust(20), end='')
        print(f"| 정답 : {14/i} ")
    except ZeroDivisionError :
        print(f"| {i}, 이걸로는 나누기 못해 !")
        continue


print(new_per)
