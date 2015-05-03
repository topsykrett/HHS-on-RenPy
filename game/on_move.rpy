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
            renpy.scene(layer='master') # Сброс картинок
            renpy.scene(layer='screens') # Сброс скринов
            renpy.show('daytime')
            if getLoc(curloc) != False: getLoc(curloc).people = [] #Сброс людей с предыдущей локации

            player.energy -= randf(2,5) #расход энергии
            resetStats(allChars) #Сброс статов
            player.checkDur() # Удаление использованных предметов
            changetime(rand(2, 5)) #изменение времени

            if where[:4] == 'loc_' and getLoc(where).position != 'tech': #Если локация - локация и если она не техническая
                addPeopleLocation(where) #Добавление людей на локацию
                if where != curloc:
                    prevloc = curloc
                    curloc = where
                    same_loc = 0
                else:
                    same_loc = 1
                checkClothes(curloc) # проверка одетости

            if rand(0,99) < 10 + (ptime - lastEventTime)*10 and where[:4] == 'loc_': tryEvent(where) # попытка дёрнуть рандомный эвент с локации. Чем больше прошло времени с последнего, тем выше шанс.

            renpy.retain_after_load() # чтобы сохранялся интерфейс, иначе ошибка
            
            renpy.show_screen('stats_screen') #При перемещении всегда появляется интерфейс
            
            renpy.jump(where) #Переход на локу
        else:
            renpy.jump('loc_home')
            
#Просто дёргает всех людей и сбрасывает выделющиеся статы
    def resetStats(input): 
        for x in input:
            x.reset()
        player.reset()

            
#Вызов эвента
    def tryEvent(location):
        if getLoc(location).position == 'classroom' and lt() > 0: location += 'Learn' #Если сейчас уроки, то добавляем к поиску локаций Learn
        if lt() == -4: location += 'Night'
        tempEv = []
        for x in locations: #перебираем локи и ищем подходящие эвенты
            if x.id == location:
                for event in x.events:
                    if x.position == 'self':
                        if event.corr <= player.corr:
                            tempEv.append(event)
                    else :
                        if event.corr <= getPar(studs, 'corr'):
                            tempEv.append(event)

        if len(tempEv) > 0:
            renpy.hide_screen('stats_screen')
            rands = rand(0,len(tempEv)-1)
            callEvent = tempEv[rands].id
            lastEventTime = ptime #запоминаем время
            renpy.jump(callEvent) #эвент
                    
#Добавление людей на локации
    def addPeopleLocation(location):
        location = getLoc(location) #Получение объекта локации
        for x in allChars:
            if rand(0,99) < location.getprob(): #В зависимости от вероятности (меняется от времени)
                temp = getChar()
                if location.people.count(temp) == 0:
                    location.people.append(temp)
                    
# Проверка одежды
    def checkClothes(location):
        location = getLoc(location)
        if location.position != 'safe':
            if player.isCover('верх','низ') == False and player.corr < 80:
                renpy.scene(layer='screens')
                renpy.jump('naked')
            elif player.isCover('верх','низ') == False and player.corr >= 80 and location.id != 'loc_beach' and location.id != 'loc_pool':
                renpy.scene(layer='screens')
                renpy.jump('naked')
            elif player.getCovPurpose('swim') and location.id != 'loc_beach' and location.id != 'loc_pool':
                renpy.scene(layer='screens')
                renpy.jump('naked')