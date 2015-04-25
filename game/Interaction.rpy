init python:
    interactionObj = ''
    lastView = 'locationPeopleList'
            

label locationPeople:
    $ renpy.call_screen(lastView)


screen locationPeopleList:
    tag interface
    fixed xpos 0.01 ypos 0.01:
        $ yalig = 0
        $ xalig = 0.0
        for x in getLoc(curloc).people:
            $ yalig += 0.05
            textbutton '[x.name]' xalign xalig yalign yalig xminimum 280 action [SetVariable('interactionObj',x), Show('show_stat')]
            if yalig >= 0.8:
                $ yalig = 0
                $ xalig += 0.35
        hbox:
            textbutton 'Назад' action [Show('stats_screen'), Function(move, curloc)]
            textbutton 'Картинки' action [SetVariable('lastView','locationPeoplePicto'), Show('locationPeoplePicto')]
        

screen locationPeoplePicto:
    tag interface
    fixed xpos 0.01 ypos 0.01:
        $ xalig = 0.1
        $ yalig = 0.05
        for x in getLoc(curloc).people:
            imagebutton idle im.FactorScale(x.picto,0.5) hover im.FactorScale(x.picto,0.6) xalign xalig yalign yalig action [SetVariable('interactionObj',x), Show('show_stat')]
            # add im.FactorScale(x.picto,0.6) xalign xalig yalign yalig
            $ xalig += 0.09
            if xalig >= 0.9:
                $ yalig += 0.15
                $ xalig = 0.1
        hbox:
            textbutton 'Назад' action [Show('stats_screen'), Function(move, curloc)]
            textbutton 'Список' action [SetVariable('lastView','locationPeopleList'), Show('locationPeopleList')]
        
screen show_stat():
    tag interface
    fixed xpos 0.1 ypos 0.1:
        vbox:
            $ x = interactionObj
            text '[x.name]' style style.my_text
            if x.bsize > 0: 
                text 'Размер груди [x.bsize]' style style.my_text
            text 'Рост [x.height]' style style.my_text
            text 'Образование [x.edu]' style style.my_text
            text 'Счастье [x.fun]' style style.my_text
            text 'Лояльность [x.loy]' style style.my_text
            text 'Развратность [x.corr]' style style.my_text
            text 'Красота [x.beauty]' style style.my_text
            textbutton 'Назад' action Show(lastView)