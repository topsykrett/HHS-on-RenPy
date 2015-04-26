init -3 python:
    #Start time
    minute = 0
    check_minute = 0
    hour = 6
    ptime = 0
    weekday = 1
    month = 5
    number = 1
    year = 2010
    ptime = 0
    last_sleeped = 0
    
    def gettime():
        #Дни недели
        if weekday == 1: _weekday = 'Понедельник'
        if weekday == 2: _weekday = 'Вторник'
        if weekday == 3: _weekday = 'Среда'
        if weekday == 4: _weekday = 'Четверг'
        if weekday == 5: _weekday = 'Пятница'
        if weekday == 6: _weekday = 'Суббота'
        if weekday == 7: _weekday = 'Воскресенье'


        #Месяца
        if month == 1: _month = 'Января'
        if month == 2: _month = 'Февраля'
        if month == 3: _month = 'Марта'
        if month == 4: _month = 'Апреля'
        if month == 5: _month = 'Мая'
        if month == 6: _month = 'Июня'
        if month == 7: _month = 'Июля'
        if month == 8: _month = 'Августа'
        if month == 9: _month = 'Сентября'
        if month == 10: _month = 'Октября'
        if month == 11: _month = 'Ноября'
        if month == 12: _month = 'Декабря'
        
        if minute < 10:
            output = '%d %s %d, %s. %s:0%s' % (number, _month, year, _weekday, hour, minute)
        else:
            output = '%d %s %d, %s. %s:%s' % (number, _month, year, _weekday, hour, minute)
        return output
        
    def changetime(change):
        global minute, check_minute, hour, ptime, weekday, number, year, month, ptime
        minute += change
        check_minute += change
        
        while minute >= 60:
            minute -= 60
            hour += 1
            ptime += 1
            if hour == 0: dailyRecount()
            if hour >= 24:
                hour -= 24
                weekday += 1
                if weekday >=8: weekday -=7
                number += 1
                if number >= 31:
                    number = 30
                    month += 1
                    if month == 13:
                        month -=12
                        year += 1
    
    def lt():
        #время первого урока
        if hour == 8 and minute <=40: result = 1
        #перемена
        if hour == 8 and minute > 40: result = 0
        #второй урок
        if hour == 9 and minute <=40: result = 2
        if hour == 9 and minute > 40: result = 0
        #третий урок
        if hour == 10 and minute <=40: result = 3
        if hour == 10 and minute > 40: result = 0
        #четвёртый урок
        if hour == 11 and minute <=40: result = 4
        if hour == 11 and minute > 40: result = 0
        #большая перемена
        if hour == 12: result = 0
        #пятый урок
        if hour == 13 and minute <=40: result = 5
        if hour == 13 and minute > 40: result = 0
        #шестой урок
        if hour == 14 and minute <=40: result = 6
        if hour == 14 and minute > 40: result = -1
        #внеурочное время
        if hour <= 7 or hour >= 15: result = -2
        #Выходные
        if weekday == 6 or weekday == 7: result = -3
        #Ночь
        if hour > 20 or hour < 6: result = -4
        return result