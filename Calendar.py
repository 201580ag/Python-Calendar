import calendar
from datetime import datetime

# 현재 날짜와 시간을 가져오기
now = datetime.now()

# 현재 년도와 월 추출
yy = now.year
mm = now.month

# calendar.month 함수를 사용하여 현재 년도와 월의 달력 출력
print(calendar.month(yy, mm))
