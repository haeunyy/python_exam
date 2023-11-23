import csv


with open("매수종목1.txt", "w", encoding="utf8") as file:
    file.write("005930\n005380\n035420")

with open("매수종목2.txt", "w", encoding="utf8") as file:
    file.write("005930 삼성전자\n005380 현대차\n035420 NAVER")

with open("매수종목3.csv", mode="w", encoding="utf8", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["종목명", "종목코드", "PER"])
    writer.writerow(["삼성전자", "005930", 15.59])
    writer.writerow(["NAVER", "035420", 55.82])

with open("매수종목3.csv", mode="a+", encoding="utf8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows([["종목명", "종목코드", "PER"],\
                      ["삼성전자", "005930", 15.59],\
                        ["NAVER", "035420", 55.82]])
    




