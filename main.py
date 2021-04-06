# 변수의 사용과 데이터 입출력
# 예시
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


# 단순 조건문 사용하기
# 예시
def b00():
    num1, num2 = input("숫자 2개를 입력하시오. ").split()  # 입력받은 문자열을 둘로 나눈다
    num1 = int(num1)  # 첫 문자열을 정수로 변환
    num2 = int(num2)  # 두번째 문자열을 정수로 변환
    if num1 == num2:
        print("두 수는 같습니다.")
    else:
        print("두 수는 같지 않습니다.")


# 나이 계산 및 미성년자 판정
def b01():
    birth_year = int(input("태어난 년도를 입력하세요. "))
    age = 2021 - birth_year + 1

    if age < 20:
        print("미성년자입니다.")
    else:
        print("미성년자가 아닙니다.")


# 온도 상호 변환
def b02():
    input_degree = float(input("온도를 입력하세요. "))
    kind = input("입력하신 온도가 섭씨 온도이면 C를, 화씨 온도라면 F를 입력하세요. ")

    if kind == 'C':
        print(input_degree * 1.8 + 32)
    else:
        print((input_degree - 32) / 1.8)


# 직사각형 넓이 계산 및 정사각형 판정
def b03():
    width = int(input("직사각형의 가로 크기를 입력하시오. "))
    height = int(input("직사각형의 세로 크기를 입력하시오. "))
    area = width * height
    print("직사각형의 넓이는", area, "이고")

    if width == height:
        print("정사각형입니다")
    else:
        print("정사각형이 아닙니다")


# 아파트 평형 계산 및 종류 판정
def b04():
    m2_area = float(input("아파트의 분양 면적을 입력하시오. "))
    pyung_area = m2_area / 3.305
    print("아파트의 평형은", round(pyung_area, 1), "이고")

    if pyung_area < 30:
        print("30평 미만이므로 작은 아파트입니다")
    else:
        print("30평 이상이므로 큰 아파트입니다")


# 날짜 계산
def b05():
    days = int(input("날 수를 입력하세요. "))
    seconds = days * 24 * 60 * 60
    m_count = int(seconds / 1000000)
    print("날 수에 해당되는 시간은 모두", seconds, "초 입니다")

    if m_count > 0:
        print("100만 초가 모두", m_count, "번 포함됩니다")


# 점수 계산
def b06():
    kor = int(input("국어 점수를 입력하세요. "))
    eng = int(input("영어 점수를 입력하세요. "))
    math = int(input("수학 점수를 입력하세요. "))
    total = kor + eng + math
    average = total / 3
    print("입력하신 점수의 총점은,", total, "이고,")
    print("평균은", round(average, 1), "입니다.")

    if kor >= 90:
        print("국어 점수가 우수합니다.")
    if eng >= 90:
        print("영어 점수가 우수합니다.")
    if math >= 90:
        print("수학 점수가 우수합니다.")


# 파일 용량 계산
def b07():
    megabytes = int(input("파일 용량을 메가바이트 단위로 입력하세요. "))
    bytes = megabytes * 1024 * 1024
    usb2 = input("USB 포트가 2.0이면 Y, 아니면 N을 입력하세요. ")

    if usb2 == 'Y':
        time = int(bytes / 60000000)
    else:
        time = int(bytes / 1500000)

    print("파일 전송 시간은", time, "초 입니다")


# 다양한 조건 판정
def b08():
    num1 = int(input("첫번째 숫자를 입력하세요 "))
    num2 = int(input("두번째 숫자를 입력하세요 "))
    num3 = int(input("세번째 숫자를 입력하세요 "))

    if num1 == num2 or num2 == num3 or num1 == num3:
        print("1번 조건 만족 : 3개의 숫자 중 적어도 두 수의 값이 같아")

    if (num1 > 50 and num2 > 50) or (num2 > 50 and num3 > 50) or (num1 > 50 and num3 > 50):
        print("2번 조건 만족 : 3개의 숫자 중 적어도 두 수의 크기가 모두 50 보다 크다")

    if num1 + num2 == num3 or num2 + num3 == num1 or num1 + num3 == num2:
        print("3번 조건 만족 : 3개의 숫자 중 어떤 두 수의 합이 나머지 하나의 숫자와 같아")

    if (num1 % num2 == 0 and num3 % num2 == 0) or (num1 % num3 == 0 and num2 % num3 == 0) or (
            num2 % num1 == 0 and num3 % num1 == 0):
        print("4번 조건 만족 : 3개의 숫자 중 어떤 하나의 수로 다른 두 수를 나누면 나누어 떨어지는 경우가 있다")


# 비만 판정
def b09():
    height = int(input("신장(cm단위)을 입력하세요 ")) * 0.01
    weight = int(input("체중(kg단위)을 입력하세요 "))
    bmi = weight / (height * height)

    if bmi >= 25:
        print("당신은 비만입니다")
    else:
        print("당신은 비만이 아닙니다")


# 복합 조건문 사용하기
# 예시
def c00():
    num1, num2 = input("숫자 2개를 입력하시오. ").split()
    num1 = int(num1)
    num2 = int(num2)
    if num1 > num2:
        print("첫 번째 숫자가 두 번째 숫자보다 큽니다.")
    elif num1 < num2:
        print("두 번째 숫자가 첫 번째 숫자보다 큽니다.")
    else:
        print("두 수는 같습니다.")


# 나이 계산 및 연령대 판정
def c01():
    birth_year = int(input("태어난 년도를 입력하세요 "))
    age = 2021 - birth_year + 1
    print(age)

    if age < 7:
        print("유아입니다")
    elif 7 <= age < 13:
        print("어린이입니다")
    elif 13 <= age < 20:
        print("청소년입니다")
    elif 20 <= age < 30:
        print("청년입니다")
    elif 30 <= age < 60:
        print("중년입니다")
    else:
        print("노년입니다")


# 물의 온도 구간 판정
def c02():
    input_degree = float(input("물의 온도를 입력하세요 "))

    if 0 <= input_degree < 25:
        print("냉수입니다")
    elif 25 <= input_degree < 40:
        print("미온수입니다")
    elif 40 <= input_degree < 80:
        print("온수입니다")
    elif 80 <= input_degree:
        print("끓는물입니다")
    else:
        print("잘못 입력하셨습니다")


# 직사각형 형태 판정
def c03():
    width = int(input("직사각형의 가로 크기를 입력하세요 "))
    height = int(input("직사각형의 세로 크기를 입력하세요 "))
    
    if width == height:
        print("정사각형입니다")
    elif width >= height * 2:
        print("좌우로 길쭉한 직사각형입니다")
    elif height >= width * 2:
        print("위아래로 길쭉한 직사각형입니다")
    elif width > height:
        print("일반적인 가로형 직사각형입니다")
    elif height > width:
        print("일반적인 세로형 직사각형입니다")


# 아파트 평형 계산 및 종류 판정
def c04():
    m2_area = int(input("아파의 분양 면적(제곱미터)를 입력하세요 "))
    pyung_area = m2_area / 3.305
    print("아파트의 평형은", round(pyung_area, 1) , "입니다")
    
    if pyung_area < 15:
        print("소형 아파트입니다")
    elif 15 <= pyung_area < 30:
        print("중소형 아파트입니다")
    elif 30 <= pyung_area < 50:
        print("중형 아파트입니다")
    else:
        print("대형 아파트입니다")


# 연중 날짜 계산
def c05():
    month = int(input("월을 입력하세요 "))
    day = int(input("일을 입력하세요 "))

    if month > 12:
        print("잘못 입력하셨습니다")
    else:
        day_count = day

        if month > 1:
            day_count += 31
        if month > 2:
            day_count += 28
        if month > 3:
            day_count += 31
        if month > 4:
            day_count += 30
        if month > 5:
            day_count += 31
        if month > 6:
            day_count += 30
        if month > 7:
            day_count += 31
        if month > 8:
            day_count += 31
        if month > 9:
            day_count += 30
        if month > 10:
            day_count += 31
        if month > 11:
            day_count += 30

        print("이 날짜는 1년 중", day_count, "번째 날에 해당됩니다")


# 점수 계산
def c06():
    kor = int(input("국어 점수를 입력하세요 "))
    eng = int(input("영어 점수를 입력하세요 "))
    math = int(input("수학 점수를 입력하세요 "))

    total = kor + eng + math
    average = total / 3
    
    print("입력하신 점수의 총점은", total, "이고")
    print("평균은", round(average, 1), "입니다")

    if 90 <= average:
        print("수 입니다")
    elif 80 <= average < 90:
        print("우 입니다")
    elif 70 <= average < 80:
        print("미 입니다")
    elif 60 <= average < 70:
        print("양 입니다")
    else:
        print("가 입니다")


# 파일 전송 시간 계산
def c07():
    megabytes = int(input("파일 용량을 메가바이트 단위로 입력하세요 "))
    kind = int(input("전송 방식을 1: Wi-Fi, 2: BlueTooth, 3: LTE, 4: USB 에서 선택하여 입력하세요 "))

    bytes = megabytes * 1024 * 1024

    if kind == 1:
        time = bytes / 1500000
    elif kind == 2:
        time = bytes / 300000
    elif kind == 3:
        time = bytes / 1000000
    else:
        time = bytes / 60000000
    
    print("파일 전송 시간은", round(time, 1), "초 입니다")


# 3개의 수 중 최댓값과 최솟값 구하기
def c08():
    num1 = int(input("첫번째 숫자를 입력하세요 "))
    num2 = int(input("두번째 숫자를 입력하세요 "))
    num3 = int(input("세번째 숫자를 입력하세요 "))

    max_num = num1
    min_num = num1
    
    if max_num < num2:
        max_num = num2
    if max_num < num3:
        max_num = num3
        
    if min_num > num2:
        min_num = num2
    if min_num > num3:
        min_num = num3
        
    print("가장 큰 수는", max_num, "이고 가장 작은 수는", min_num, "입니다")


# 소득세 계산
def c09():
    income = int(input("연봉(원 단위)을 숫자로 입력하세요 "))

    if 80000000 <= income:
        tax = income * 0.37
    elif 40000000 <= income < 80000000:
        tax = income * 0.28
    elif 10000000 <= income < 40000000:
        tax = income * 0.19
    else:
        tax = income * 0.095
        
    print("연봉 금액에 대한 소득세는", int(tax), "원 입니다")


# 간단한 사칙연산 계산기
def c10():
    num1 = int(input("숫자 1을 입력하세요 "))
    num2 = int(input("숫자 2을 입력하세요 "))
    operator = input("연산기호문자를 입력하세요 ")
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/' and num2 != 0:
        result = num1 / num2
    else:
        result = 'error'
        
    print("계산식의 결과 값은", result, "입니다")


# 윤년 판정하기
def c11():
    year = int(input("년도를 입력하세요 "))
    
    if year % 100 == 0:
        if year % 400 == 0:
            print("윤년입니다")
        else:
            print("윤년이 아닙니다")
    elif year % 4 == 0:
        print("윤년입니다")
    else:
        print("윤년이 아닙니다")


if __name__ == '__main__':
    c11()
