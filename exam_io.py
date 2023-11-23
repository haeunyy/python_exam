import csv

# 텍스트 파일 생성
with open("매수종목1.txt", "w", encoding="utf8") as file:
    file.write("005930\n005380\n035420")

with open("매수종목2.txt", "w", encoding="utf8") as file:
    file.write("005930 삼성전자\n005380 현대차\n035420 NAVER")

with open("매수종목3.csv", mode="w", encoding="utf8", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["종목명", "종목코드", "PER"])
    writer.writerow(["삼성전자", "005930", 15.59])
    writer.writerow(["NAVER", "035420", 55.82])

# 기존 텍스트 파일에 추가 입력 
with open("매수종목3.csv", mode="a+", encoding="utf8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows([["종목명", "종목코드", "PER"],\
                      ["삼성전자", "005930", 15.59],\
                        ["NAVER", "035420", 55.82]])
    
# 파일 읽기
with open("매수종목1.txt", mode='r', encoding='utf8', newline='') as file:

    read = file.read(3) # 한글도 한글자로 인식한다. 
    readline = file.readline()
    readlines = file.readlines()

    print("read : {}".format(read))
    print("readline : {}".format(readline))
    print("readlines : {}".format(readlines))

