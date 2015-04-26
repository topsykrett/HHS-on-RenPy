init python:
    lastNotebookScreen = 'studList'
label notebook:
    show expression "pic/bg.png"
    call screen notebook
    
screen notebook:
    fixed xpos 0.01 ypos 0.01:
        hbox :
            textbutton 'Назад' action [Show('stats_screen'), Hide('studList'), Hide('teacherList'), Function(move, curloc)]
            textbutton 'Вы' action [Hide ('charInfoLeft'), Show('personalInfo')]
            textbutton 'Список учеников' action Show('studList')
            textbutton 'Список учителей' action Show('teacherList')
        
        
screen studList:
    tag notebookList
    fixed xpos 0.01 ypos 0.1:
        $ xalig = 0.17
        $ yalig = 0.01
        for x in studs:
            imagebutton idle im.FactorScale(x.picto,0.5) hover im.FactorScale(x.picto,0.6) xalign xalig yalign yalig action NullAction() hovered [SetVariable('showHover',x),Show('charInfoLeft')]
            $ xalig += 0.09
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.17
        
screen teacherList:
    tag notebookList
    fixed xpos 0.01 ypos 0.1:
        $ xalig = 0.17
        $ yalig = 0.01
        for x in teachers:
            imagebutton idle im.FactorScale(x.picto[:23] + '1.png',0.5) hover im.FactorScale(x.picto[:23] + '1.png',0.6) xalign xalig yalign yalig action NullAction() hovered [SetVariable('showHover',x),Show('charInfoLeft')]
            $ xalig += 0.15
            if xalig >= 0.99:
                $ yalig += 0.15
                $ xalig = 0.17

screen charInfoLeft:
    tag interface
    vbox xpos 0.01 ypos 0.1:
        if showHover.age > 0:
            add showHover.picto
            null height 10
            text '[showHover.name]' style style.my_text
            if showHover.bsize > 0: 
                $ temp = round(showHover.bsize,1)
                text 'Размер груди [temp]' style style.my_text
            else:
                text '' style style.my_text
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

screen personalInfo:
    tag notebookList interface
    fixed xpos 0.1 ypos 0.1:
        vbox:
            add player.picto
            null height 10
            text '[player.name]' style style.my_text
            if player.bsize > 0: 
                $ temp = round(player.bsize,1)
                text 'Размер груди [temp]' style style.my_text
            $ temp = round(player.height,1)
            text 'Рост [temp]' style style.my_text
            $ temp = round(player.edu,1)
            text 'Образование [temp]' style style.my_text
            $ temp = round(player.fun,1)
            text 'Счастье [temp]' style style.my_text
            $ temp = round(player.loy,1)
            text 'Лояльность [temp]' style style.my_text
            $ temp = round(player.corr,1)
            text 'Развратность [temp]' style style.my_text
            $ temp = round(player.beauty,1)
            text 'Красота [temp]' style style.my_text
            
    fixed xpos 0.3 ypos 0.1 :
        vbox xmaximum config.screen_width/2:
            text textgen(player) style style.my_text