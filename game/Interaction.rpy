init python:
    
    
    class Dialogue():
        def __init__(self, id, corr):
            self.id = id
            self.corr = corr
    
    def dialogueParser():
        _locs = renpy.get_all_labels()
        textList = []
        for textLable in _locs: # перебираем все лейблы
            if textLable[:7] == 'dialog_': #находим тот, что с текстом
                corr = textLable.split("_")
                corr = corr[1]
                tempText = Dialogue(id = textLable, corr = int(corr))
                textList.append(tempText)
        return textList
    
    dialogueList = dialogueParser()
    
    def dialogueSelector(speaker):
        tempList = []
        for x in dialogueList:
            if speaker.corr >= x.corr:
                tempList.append(x)
        return tempList[rand(0,len(tempList) - 1)].id

    dummy = Char(
        fname = '',
        lname = '',
        age = 0,
        sex = '',
        bsize = 0,
        psize = 0,
        vsize = 0,
        asize = 0,
        height = 0,
        color = '#269AFF',
        loy = 0,
        fun = 0,
        inventory = [],
        wear = [],
        corr = 0,
        lust = 0,
        will = 0,
        edu = 0,
        club = '',
        picto = 'pic/events/teachers/55/picto.png',
        health = 0,
        energy = 0,
        intel = 0,
        location = curloc,
        money = 0,
        beauty = 0,
        dirty = 0,
        rep = 0,
        body = []
    )
    interactionObj = ''
    lastView = 'locationPeoplePicto'
    showHover = dummy


label locationPeople:
    show expression "pic/bg.png"
    $ renpy.call_screen(lastView)


# screen locationPeopleList:
    # tag interface
    # fixed xpos 0.01 ypos 0.01:
        # $ yalig = 0
        # $ xalig = 0.0
        # for x in getLoc(curloc).people:
            # $ yalig += 0.05
            # textbutton '[x.name]' xalign xalig yalign yalig xminimum 280 action [SetVariable('interactionObj',x), Show('show_stat')]
            # if yalig >= 0.8:
                # $ yalig = 0
                # $ xalig += 0.35
        # hbox:
            # textbutton 'Назад' action [Hide('charInfoLeft'), Show('stats_screen'), Function(move, curloc)]
            # textbutton 'Картинки' action [SetVariable('lastView','locationPeoplePicto'), Show('locationPeoplePicto')]
        

screen locationPeoplePicto:
    tag interface
    fixed xpos 0.01 ypos 0.01:
        textbutton 'Назад' action [ Hide('charInfoLeft'), Show('stats_screen'), Function(move, curloc)]
        
        $ xalig = 0.2
        $ yalig = 0.05
        for x in getLoc(curloc).people:
            imagebutton idle im.FactorScale(x.picto,0.5) hover im.FactorScale(x.picto,0.6) xalign xalig yalign yalig action [Hide('charInfoLeft'), SetVariable('interactionObj',x), Show('show_stat')] hovered [SetVariable('showHover',x),Show('charInfoLeft')]
            # add im.FactorScale(x.picto,0.6) xalign xalig yalign yalig
            $ xalig += 0.09
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.2
                
screen show_stat():
    tag interface
    fixed xpos 0.1 ypos 0.1:
        vbox:
            if teachers.count(showHover) > 0:
                add showHover.picto[:23] + '1.png'
            else :
                add showHover.picto
                 
            $ x = interactionObj
            null height 10
            text '[showHover.name]' style style.my_text
            if showHover.bsize > 0: 
                $ temp = round(showHover.bsize,1)
                text 'Размер груди [temp]' style style.my_text
            $ temp = round(showHover.height,1)
            text 'Рост [temp]' style style.my_text
            $ temp = round(showHover.edu,1)
            text 'Образование [temp]' style style.my_text
            $ temp = round(showHover.fun,1)
            text 'Счастье [temp]' style style.my_text
            $ temp = round(showHover.loy,1)
            text 'Лояльность [temp]' style style.my_text
            $ temp = round(showHover.corr,1)
            text 'Развратность [temp]' style style.my_text
            $ temp = round(showHover.beauty,1)
            text 'Красота [temp]' style style.my_text
            null height 10
           
    fixed xpos 0.3 ypos 0.1 :
        vbox xmaximum config.screen_width/2:
            text textgen(showHover) style style.my_text
    
    fixed xpos 0.8 ypos 0.1:
        vbox:
            textbutton 'Поговорить' xminimum 200 action Jump('speak') 
            textbutton 'Флирт' xminimum 200 action Jump('flirt')
            textbutton 'Назад' xminimum 200 action [Hide('show_stat'), Function(move,curloc)]
      
label speak:
    if lt() > 0 or lt() == -2: 
        $ renpy.jump('exitInteraction')
    $ user = showHover
    $ changetime(10)
    $ player.energy -= rand(5,10)
    $ user.loy += 100
    $ renpy.jump(dialogueSelector(user))
    
    call screen show_stat
    
label flirt:
    if lt() > 0 or lt() == -2: 
        $ renpy.jump('exitInteraction')
        
    $ user = showHover
    
    player.say 'Ого какие сиськи!'
    user.say 'Ага!'
    
    call screen show_stat

label exitInteraction:
    showHover.say 'Простите, мне пора на урок!'
    
    $ move(curloc)