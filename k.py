from datetime import datetime,time,timedelta
today_date=datetime.now()
new="23/5/2023"
new=datetime.strptime(new,'%d/%m/%Y')
print(new)
