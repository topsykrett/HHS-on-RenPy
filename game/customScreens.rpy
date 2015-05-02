##############################################################################
# кастомные скрины
##############################################################################
init python:
    myItem = 0

screen stats_screen:
 #   tag interface
    fixed xpos 0.01 ypos 0.01:
        vbox xmaximum config.screen_width/2:
            $ currtime = gettime()
            text "[currtime]" style style.my_text
            $ vlt = lt()
            if vlt > 0: 
                text "Сейчас идёт [vlt] урок" style style.my_text
            if vlt == 0: 
                text "Сейчас перемена" style style.my_text
            if vlt < 0: 
                text "Сейчас нет уроков" style style.my_text
            
            #Warnings
            if ptime - last_eat > 24:
                text "Вы голодаете" style style.warning
            elif ptime - last_eat > 15:
                text "Вы голодны" style style.my_text
                
            if player.isSperm() > 0:
                $ temp = player.printSperm()
                text "В сперме [temp]" style style.warning
                
            if player.dirty == 1: 
                text "Вы слегка вспотели" style style.my_text
            if player.dirty == 2: 
                text "Вы вспотели" style style.my_text
            if player.dirty == 3: 
                text "От Вас воняет" style style.my_text
            if player.dirty >= 4: 
                text "От вас воняет, как от последнего бомжа" style style.warning
                
            #Buttons
            hbox style style.myBox:
                if player.getSperm('лицо') == True:
                    imagebutton auto "pic/actions/face_%s.png" action Jump('cleanFace')
                if player.getSperm('рот') == True:
                    imagebutton auto "pic/actions/mouth_%s.png" action Jump('cleanMouth')
                if player.getSperm('грудь') == True:
                    imagebutton auto "pic/actions/body_%s.png" action Jump('cleanBody')
                if player.getSperm('руки') == True:
                    imagebutton auto "pic/actions/hands_%s.png" action Jump('cleanHands')
                if player.getSperm('ноги') == True:
                    imagebutton auto "pic/actions/feet_%s.png" action Jump('cleanFeet')
                if player.getSperm('вагина') == True:
                    imagebutton auto "pic/actions/pussy_%s.png" action Jump('cleanPussy')
                if player.getSperm('анус') == True:
                    imagebutton auto "pic/actions/ass_%s.png" action Jump('cleanAss')                
                
                
    fixed xpos 0.3 ypos 0.01:
        hbox:
            grid 2 2:
                text 'Лояльность' style style.my_text
                $ temp = getPar(studs, 'loy')
                if temp > stat_loy: 
                    text ' [temp]' style style.green
                elif temp < stat_loy: 
                    text ' [temp]' style style.warning
                else :
                    text ' [temp]' style style.my_text
                python:
                    global stat_loy
                    stat_loy = temp          

                $ temp = getPar(studs, 'fun')
                text 'Счастье' style style.my_text
                if temp > stat_fun: 
                    text ' [temp]' style style.green
                elif temp < stat_fun: 
                    text ' [temp]' style style.warning
                else :
                    text ' [temp]' style style.my_text
                python:
                    global stat_fun
                    stat_fun = temp 
                
            grid 2 2:
                $temp = getPar(studs, 'lust')
                text 'Желание' style style.my_text
                if temp > stat_lust: 
                    text ' [temp]' style style.green
                elif temp < stat_lust: 
                    text ' [temp]' style style.warning
                else :
                    text ' [temp]' style style.my_text
                python:
                    global stat_lust
                    stat_lust = temp 
                
                $ temp = getPar(studs, 'corr')
                text 'Разврат' style style.my_text
                if temp > stat_corr: 
                    text ' [temp]' style style.green
                elif temp < stat_corr: 
                    text ' [temp]' style style.warning
                else :
                    text ' [temp]' style style.my_text
                python:
                    global stat_corr
                    stat_corr = temp 
                
                
            grid 2 2:
                $temp = getPar(studs, 'edu')
                text 'Учёба' style style.my_text
                if temp > stat_edu: 
                    text ' [temp]' style style.green
                elif temp < stat_edu: 
                    text ' [temp]' style style.warning
                else :
                    text ' [temp]' style style.my_text
                python:
                    global stat_edu
                    stat_edu = temp 
                
                $temp = getPar(studs, 'rep')
                text 'Репутация ' style style.my_text
                if temp > stat_rep: 
                    text ' [temp]' style style.green
                elif temp < stat_rep: 
                    text ' [temp]' style style.warning
                else :
                    text ' [temp]' style style.my_text
                python:
                    global stat_rep
                    stat_rep = temp
                
            grid 2 2:
                $ temp = round(player.energy,0)
                if temp > player.health/10:
                    text "Ваша энергия " style style.my_text
                    text ' [temp]' style style.my_text
                else:
                    text "Ваша энергия " style style.warning
                    text ' [temp]' style style.warning
                    
                $ temp = round(player.lust,0)
                text "Ваше желание " style style.my_text
                if temp > stat_plust: 
                    text ' [temp]' style style.green
                elif temp < stat_plust: 
                    text ' [temp]' style style.warning
                else :
                    text ' [temp]' style style.my_text
                python:
                    global stat_plust
                    stat_plust = temp
    
    vbox xalign 0.99 yalign 0.01:
        imagebutton auto "pic/actions/wait15_%s.png" action [Function(waiting,15)]
        imagebutton auto "pic/actions/wait60_%s.png" action [Function(waiting,60)]
        imagebutton idle im.FactorScale('pic/actions/smartphone_idle.png', 0.5) hover im.FactorScale('pic/actions/smartphone.png', 0.5) action [Hide('stats_screen'), Jump('notebook')]
        imagebutton auto "pic/actions/inventory_%s.png" action [Hide('stats_screen'), Show('inventory')]
        if getLoc(curloc) != False:
            if len(getLoc(curloc).people) > 0:
                imagebutton auto "pic/actions/eye_%s.png" action [Hide('stats_screen'),Jump('locationPeople')]


screen char_select:
    fixed:
        text 'Выберите персонаж' xalign 0.5 yalign 0.1 style style.description
        imagebutton idle "pic/Hero/1.png" hover im.FactorScale("pic/Hero/1.png",1.1) xalign 0.2 yalign 0.5 action [SetVariable('_picture',"pic/Hero/1.png"), Jump('gendir')]
        imagebutton idle "pic/Hero/2.png" hover im.FactorScale("pic/Hero/2.png",1.1) xalign 0.4 yalign 0.5 action [SetVariable('_picture',"pic/Hero/2.png"), Jump('gendir')]
        imagebutton idle "pic/Hero/3.png" hover im.FactorScale("pic/Hero/3.png",1.1) xalign 0.6 yalign 0.5 action [SetVariable('_picture',"pic/Hero/3.png"), Jump('gendir')]
        imagebutton idle "pic/Hero/4.png" hover im.FactorScale("pic/Hero/4.png",1.1) xalign 0.8 yalign 0.5 action [SetVariable('_picture',"pic/Hero/4.png"), Jump('gendir')]
        
screen inventory:
    zorder 1
    modal True
    fixed :
        add 'pic/bg.png'
    fixed xpos 0.01 ypos 0.01:
        textbutton 'Назад' action Function(move, curloc)
        
        $ xalig = 0.2
        $ yalig = 0.05
        for x in player.inventory:
            if x.type == 'food':
                imagebutton idle im.FactorScale(x.picto,0.4) hover im.FactorScale(x.picto,0.45) xalign xalig yalign yalig  action [Function(player.eat, x), Function(move,curloc)] hovered [SetVariable('myItem', x), Show('showItem')]
            elif x.type != 'hidden':
                imagebutton idle im.FactorScale(x.picto,0.4) hover im.FactorScale(x.picto,0.45) xalign xalig yalign yalig  action NullAction() hovered [SetVariable('myItem', x), Show('showItem')]
                $ xalig -= 0.09
            $ xalig += 0.09
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.2
                
screen showItem:
    zorder 1
    vbox xpos 0.01 ypos 0.1:
        if myItem != 0:
            add myItem.picto
            null height 10
            text '[myItem.name]' style style.my_text
            text 'Использований [myItem.durability]' style style.my_text
            if myItem.type == 'food':
                text 'Насыщение [myItem.energy]' style style.my_text
                
   
screen shopping:
    zorder 1
    modal True
    fixed :
        add 'pic/bg.png'
    fixed xpos 0.01 ypos 0.01:
        textbutton 'Назад' action Function(move, curloc)
        hbox xpos 0.2 ypos 0.1:
            vbox :
                textbutton napkin.name action [Function(player.buy, napkin), Show('showSellItem')] hovered [SetVariable('myItem', napkin), Show('showSellItem')]
                textbutton eDrink.name action [Function(player.buy, eDrink, 'add'), Show('showSellItem')] hovered [SetVariable('myItem', eDrink), Show('showSellItem')]
                textbutton rawFood.name action [Function(player.buy, rawFood), Show('showSellItem')] hovered [SetVariable('myItem', rawFood), Show('showSellItem')]
                    
screen showSellItem:
    zorder 1
    vbox xpos 0.01 ypos 0.1:
        if myItem != 0:
            add myItem.picto
            null height 10
            text '[myItem.name]' style style.my_text
            text 'Использований [myItem.durability]' style style.my_text
            if myItem.type == 'food':
                text 'Насыщение [myItem.energy]' style style.my_text
            if myItem.cost > player.money:
                 text 'Цена - [myItem.cost]' style style.warning
            else :
                text 'Цена - [myItem.cost]' style style.my_text
                
            if player.hasItem(myItem.name) > 0:
                $ temp_d = player.getItem(myItem.name).durability
                $ temp_c = player.countItem(myItem.name)
                text 'В наличии [temp_c] шт.' style style.my_text
                text 'Использований - [temp_d]' style style.my_text
            