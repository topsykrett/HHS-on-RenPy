label event_loc_home_15_1:
    $ dynpicto = studs[0].picto
    studs[0].say "поймал1!"
    'пусто'
    $ move(curloc)
    
label event_loc_home_15_2:
    $ dynpicto = studs[1].picto
    studs[1].say "поймал2!"
    $ move(curloc)
    
label event_loc_home_15_3:
    $ dynpicto = studs[2].picto
    studs[2].say "поймал3!"
    $ move(curloc)
