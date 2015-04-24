init:
    image daytime = ConditionSwitch(
        "hour < 5 or hour > 20", "#646464",
        "hour >=5  and hour <= 8", "#FFD6BD",
        "hour > 8  and hour <= 18", "#FFFFFF",
        "hour > 18  and hour <= 20", "#EB9191",
        )
    
init python:
#базовая функция перемещения. Использовать всегда и всюду
    def move(where):
        global curloc, hour, prevloc, same_loc #объявление глобальных переменных
        if renpy.has_label(where) == True: #Проверка на то, что локация существует. Если нет, прыгаем домой.
            renpy.scene() #Сброс окна
            renpy.show('daytime')
            
            if where != curloc:
                prevloc = curloc
                same_loc = 0
            else:
                same_loc = 1
            
            renpy.retain_after_load() # чтобы сохранялся интерфейс, иначе ошибка
            renpy.fix_rollback() #запрет отката
            renpy.show_screen('stats_screen') #При перемещении всегда появляется интерфейс
            
            player.energy -= randf(2,5)
            resetStats(allChars)
            curloc = where
            changetime(rand(2, 5))
            
            if where[:4] == 'loc_':
                if rand(1,100) < getLoc(where).getprob(): tryEvent(where) # попытка дёрнуть рандомный эвент с локации

            renpy.jump(where)
        else:
            renpy.jump('loc_home')
            
    def resetStats(input):
        for x in input:
            x.reset()
    
    def tryEvent(location):
        for x in locations:
            if x.id == location:
                if len(x.events) > 0:
                    renpy.hide_screen('stats_screen')
                    rands = rand(0,len(x.events)-1)
                    renpy.jump(x.events[rands].id)
        