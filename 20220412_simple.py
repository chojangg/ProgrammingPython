#예약어
import keyword
print(keyword.kwlist)

print('-'*200)

#달력 보기
import calendar
print(calendar.month(2022, 4))
print(calendar.month(2005, 11))
print(calendar.month(2022, 12))
print(calendar.month(1972, 9))

print('-'*200)

#현재 날짜와 시각 보기
import datetime
now = datetime.datetime.now()
print(now)
print(now.year, now.month, now.day, now.hour, now.minute, now.second) #오늘 년도, 월, 날짜, 시, 분, 초 출력
birthday = datetime.datetime(2005, 11, 15)
print(now - birthday)
christmas = datetime.datetime(2022, 12,25)
print(christmas - now)

print('-'*200)
#윈도우 보기
#import tkinter as tk
#base = tk.Tk()
#base.mainloop()

#turtle
import turtle as t
t.shape('turtle')
t.speed(0.1)
t.forward(200)
t.left(144)
t.forward(200)
t.left(144)
t.forward(200)
t.left(144)
t.forward(200)
t.left(144)
t.forward(200)
t.mainloop()
