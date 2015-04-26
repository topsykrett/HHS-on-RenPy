init -3 python:
    i = 500
    curloc = 'loc_home'
    is_library = 1
    is_wall = 1
    students = 50

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