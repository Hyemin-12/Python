from datetime import datetime

today = datetime.today()
weekday = today.weekday()

if weekday == 0:
    weekday = "월"
elif weekday == 1:
    weekday = "화"
elif weekday == 2:
    weekday = "수"
elif weekday == 3:
    weekday = "목"
elif weekday == 4:
    weekday = "금"
elif weekday == 5:
    weekday = "토"
else:
    weekday = "일"

print(f"오늘은 {today.year}년 {today.month}월 {today.day}일 {weekday}요일입니다.")