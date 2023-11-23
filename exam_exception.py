per = ["10.31", "", "8.00"]

new_per = [] # 리스트 초기화 

# 리스트 요소 옮겨 담기 
# for i in per:
#     try:
#         new_per.append(float(i))
#     except:
#         new_per.append(0) # 오류 발생시 0 대입
#         continue

# print(new_per)


# ZeroDivisionError 예외처리
for i in new_per:
    try:
        print(f"14를 {i}으로 나눈 값은 ?".ljust(20), end='')
        print(f"| 정답 : {14/i} ")
    except ZeroDivisionError as m:
        print(f"| {i}, 이걸로는 나누기 못해 -> ", end='')
        print(f"{m}")
        continue

# 예외처리
for i in per:
    try:
        float(i) # 실수 변환 작업
    except:
        new_per.append(0) # 예외 발생시 0 대입
        continue
    else:
        new_per.append(i) # 예외 발생하지 않았을 때 값 추가
    finally:
        print(f"{i}".ljust(5), end='') # 추가 결과 출력 
        print(f"=> 입력결과 {new_per}")


