init -3 python:
    i = 500
    curloc = 'loc_home'
    is_library = 0
    is_wall = 0
    students = 50
    last_eat = 0
    
    stat_loy = 0
    stat_fun = 0
    stat_lust = 0
    stat_corr = 0
    stat_edu = 0
    stat_rep = 0
    stat_penergy = 0
    stat_plust = 0

init:
    image white = "#FFFFFF"
    
label start:
    show white
    python:
        for x in locations:
            if x.name == 'UNKNOWN':
                renpy.say('','WRONG LOCATION! ADD TO LOCATIONS LIST! LABEL = [x.id]')
    menu:
        'selchar':
            jump selchar
        'skipall':
            jump skipall
    return


label after_load:
    $ _allChars = allChars
    $ _studs = studs
    $ studs = []
    $ allChars = []
    $ allChars = _allChars
    $ studs = _studs
    return