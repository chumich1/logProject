import calendar as cal
import Tkinter as tk
import datetime
import os.path
window = tk.Tk()



# Menu variables:
year = tk.IntVar()
month = tk.IntVar()
day = tk.IntVar()
hour = tk.IntVar()
minute = tk.IntVar()
dur_hour = tk.IntVar()
dur_minute = tk.IntVar()
duration = tk.StringVar()
start = tk.StringVar()

#            list initializations    

list_of_years = []
list_of_months = []
list_of_hours = []
list_of_days = []
list_of_minutes = []


def year_setter(value):
    year.set(value)
    all_for_day()

def all_for_day(): #checks if the data needed to determine number of days in the month is present
    list_of_days = []
    y = year.get()
    m = month.get()
    lenght_of_month = cal.monthrange(y,m)
    lenght_of_month2 = lenght_of_month[1]
    if m != 0 and y != 0:
        make_daylist(lenght_of_month2)
        make_daymenu()

def month_setter(value):
    month.set(value)
    all_for_day()

def day_setter(value):
    day.set(value)

def time_parameters():
    the_date = datetime.datetime(1,1,1,0,0,0,0)
    the_date = the_date.now()
    end_year = the_date.year  
    make_yearlist(1995, end_year)
    make_monthlist()
    make_hourlist()
    make_minutelist()

def make_yearlist(the_year, end_year):
    while the_year <= end_year:
        list_of_years.append(the_year)
        the_year += 1

def make_monthlist():
    for i in range(12):
        list_of_months.append(i + 1)

def make_daylist(num_days):
    for i in range(num_days):
        list_of_days.append(i + 1)

def make_hourlist():
    for i in range(24):
        list_of_hours.append(i)

def make_minutelist():
    for i in range(60):
        list_of_minutes.append(i)

def make_daymenu():
    daymenu.delete(0,31) 
    for the_day in list_of_days:
        daymenu.add_command(label=the_day, command=lambda : day_setter(the_day))
    window.config(menu=menubar)



# The following constructs the menu
time_parameters()
menubar = tk.Menu(window)

yearmenu = tk.Menu(menubar)
for the_year in list_of_years:
    yearmenu.add_command(label=str(the_year), command=lambda the_year=the_year: year_setter(the_year))
menubar.add_cascade(label = 'Year', menu=yearmenu)
window.config(menu=menubar)

monthmenu = tk.Menu(menubar)
for the_month in list_of_months:
    monthmenu.add_command(label=the_month, command=lambda the_month=the_month: month_setter(the_month))
menubar.add_cascade(label = 'Month', menu=monthmenu)
window.config(menu=menubar)  

daymenu = tk.Menu(menubar)
menubar.add_cascade(label = 'Day', menu=daymenu)
window.config(menu=menubar)

window.mainloop()
