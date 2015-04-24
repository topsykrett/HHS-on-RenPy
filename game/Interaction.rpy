label look_around:
    hide screen stats_screen
    screen grid_test:
        fixed xpos 0.01 ypos 0.01:
            vbox:
                for x in getLoc(curloc).people:
                    textbutton '[x.name]' action Function(move, curloc)
                textbutton 'Назад' action Function(move, curloc)
    call screen grid_test
    return