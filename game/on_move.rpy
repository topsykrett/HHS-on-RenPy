init:
    image daytime = ConditionSwitch(
        "hour < 5 or hour > 20", "#646464",
        "hour >=5  and hour <= 8", "#FFD6BD",
        "hour > 8  and hour <= 18", "#FFFFFF",
        "hour > 18  and hour <= 20", "#EB9191",
        )
    $ lastEventTime = 0
    
init python:
#базовая функция перемещения. Использовать всегда и всюду
    def move(where):
        global curloc, hour, prevloc, same_loc #объявление глобальных переменных
        if renpy.has_label(where) == True: #Проверка на то, что локация существует. Если нет, прыгаем домой.
            renpy.scene() #Сброс окна
            renpy.show('daytime')
            if getLoc(curloc) != False: getLoc(curloc).people = [] #Сброс людей с предыдущей локации
            
            if where != curloc:
                prevloc = curloc
                same_loc = 0
            else:
                same_loc = 1
            
            player.energy -= randf(2,5) #расход энергии
            resetStats(allChars) #Сброс статов
            curloc = where #Добавление курлока
            changetime(rand(2, 5)) #изменение времени

            if where[:4] == 'loc_': #Если локация - локация
                addPeopleLocation(where) #Добавление людей на локацию
                if rand(0,99) < len(getLoc(where).events) + (ptime - lastEventTime): tryEvent(where) # попытка дёрнуть рандомный эвент с локации. Чем больше эвентов, тем больше шанс

            renpy.retain_after_load() # чтобы сохранялся интерфейс, иначе ошибка
            renpy.fix_rollback() #запрет отката
            
            renpy.show_screen('stats_screen') #При перемещении всегда появляется интерфейс
            
            renpy.jump(where) #Переход на локу
        else:
            renpy.jump('loc_home')

    def resetStats(input): #Просто дёргает всех людей и сбрасывает выделющиеся статы
        for x in input:
            x.reset()
        player.reset()
            
#Вызов эвента
    def tryEvent(location):
        for x in locations:
            if x.id == location:
                if len(x.events) > 0:
                    renpy.hide_screen('stats_screen')
                    rands = rand(0,len(x.events)-1)
                    callEvent = x.events[rands].id
                    x.events.remove(x.events[rands])
                    renpy.jump(callEvent)
                    
#Добавление людей на локации
    def addPeopleLocation(location):
        location = getLoc(location) #Получение объекта локации
        for x in allChars:
            if rand(0,99) < location.getprob(): #В зависимости от вероятности (меняется от времени)
                temp = getChar()
                if location.people.count(temp) == 0:
                    lastEventTime = ptime
                    location.people.append(temp)
