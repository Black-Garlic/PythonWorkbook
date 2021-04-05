def a00():
    unit_price = int(input("사과 1개의 가격은 얼마입니까? "))
    apple_count = int(input("사과의 개수는 모두 몇 개 입니까? "))
    price = apple_count * unit_price
    print("전체 사과의 가격은 ", price, "원 입니다.")


# 나이 계산
def a01():
    birth_year = int(input("태어난 년도를 입력하시오. "))
    age = 2021 - birth_year + 1
    print("당신의 나이는 ", age, "살 입니다")


# 온도 변환
def a02():
    c_degree = float(input("섭씨 온도를 입력하시오. "))
    f_degree = c_degree * 1.8 + 32
    print("화씨 온도는", f_degree, "도 입니다")


# 직사각형 넓이 계산
def a03():
    width = int(input("직사각형의 가로 크기를 입력하시오. "))
    height = int(input("직사각형의 세로 크기를 입력하시오. "))
    area = width * height
    print("직사각형의 넓이는", area, "입니다")


# 아파트 평형 계산
def a04():
    m2_area = float(input("아파트의 분양 면적을 입력하시오. "))
    pyung_area = m2_area / 3.305
    print("아파트의 평형은", round(pyung_area, 1), "입니다")


# 날짜 계산
def a05():
    days = int(input("날 수를 입력하세요. "))
    seconds = days * 24 * 60 * 60
    print("날 수에 해당되는 시간은 모두", seconds, "초 입니다")


# 점수 계산
def a06():
    kor = int(input("국어 점수를 입력하세요. "))
    eng = int(input("영어 점수를 입력하세요. "))
    math = int(input("수학 점수를 입력하세요. "))
    total = kor + eng + math
    average = total / 3
    print("입력하신 점수의 총점은,", total, "이고,")
    print("평균은", round(average, 1), "입니다.")
    
    
# 파일 용량 계산
def a07():
    gigabytes = int(input("파일 용량을 기가바이트 단위로 입력하세요. "))
    megabytes = gigabytes * 1024
    kilobytes = megabytes * 1024
    bytes = kilobytes * 1024
    print("입력하신 파일 용량은")
    print(megabytes, "메가바이트")
    print(kilobytes, "킬로바이트")
    print(bytes, "바이트입니다.")


if __name__ == '__main__':
    a07()