init 10 python:
    locations = []
    
    class Location:
        def __init__(self,id,name,base_prob, position):
            self.id = id
            self.name = name
            self.base_prob = base_prob
            self.events = []
            self.position = position
            
        def getprob(self):
            if lt() > 0 or lt() == -4:
                return -1
            else:
                return self.base_prob
    
    class Event:
        def __init__(self,id,corr):
            self.id = id
            self.corr = corr
    
    def getLoc(id):
        for x in locations:
            if x.id == id:
                return x
        return False
    
#Функция добавления эвентов в локации
    def getEvents():
        for eventLabel in _locs: # перебираем все лейблы
            if eventLabel[:6] == 'event_': #находим тот, что с евентом
                for location in locations: #начинаем перебирать локации
                    if eventLabel.find(location.id) > 0: #Если имя локации содержится в имени эвента
                        index = eventLabel.rfind(location.id) #находим правый индекс имени локации
                        corr = eventLabel[index:] #режем по нему
                        temp = corr.split("_") #разбиваем строку по _
                        corr = int(temp[2]) #находим развратность
                        event = Event(id = eventLabel, corr = corr) # создаём эвент
                        location.events.append(event) #добавляем его в массив эвентов локации
        return 0
    
#Создание массива всех локаций
    _locs = renpy.get_all_labels()
    for x in _locs:
        if x[:4] == 'loc_':
            if x == 'loc_home': loc = Location(id = x, name = 'дом', base_prob = 100, position = 'home')
            elif x == 'loc_bedroom': loc = Location(id = x, name = 'спальня', base_prob = 0, position = 'home')
            elif x == 'loc_bathroom': loc = Location(id = x, name = 'ванная', base_prob = 0, position = 'home')
            elif x == 'loc_kitchen': loc = Location(id = x, name = 'кухня', base_prob = 0, position = 'home')
            
            elif x == 'loc_street': loc = Location(id = x, name = 'улица', base_prob = 15, position = 'other')
            elif x == 'loc_beach': loc = Location(id = x, name = 'пляж', base_prob = 35, position = 'other')
            elif x == 'loc_beachChange': loc = Location(id = x, name = 'раздевалка', base_prob = 0, position = 'other')
            elif x == 'loc_shopStreet': loc = Location(id = x, name = 'торговая улица', base_prob = 25, position = 'other')
            elif x == 'loc_shop': loc = Location(id = x, name = 'магазин', base_prob = 10, position = 'other')
            elif x == 'loc_shopBeauty': loc = Location(id = x, name = 'салон красоты', base_prob = 5, position = 'other')
            elif x == 'loc_sex_shop': loc = Location(id = x, name = 'сексшоп', base_prob = 5, position = 'other')
            
            elif x == 'loc_hall': loc = Location(id = x, name = 'холл', base_prob = 15, position = 'school')
            elif x == 'loc_entrance': loc = Location(id = x, name = 'вход', base_prob = 15, position = 'school')
            elif x == 'loc_library': loc = Location(id = x, name = 'библиотека', base_prob = 10, position = 'school')
            elif x == 'loc_changeRoom': loc = Location(id = x, name = 'школьная раздевалка', base_prob = 5, position = 'school')
            elif x == 'loc_gym': loc = Location(id = x, name = 'спортивный зал', base_prob = 25, position = 'school')
            elif x == 'loc_pool': loc = Location(id = x, name = 'бассейн', base_prob = 15, position = 'school')
            elif x == 'loc_storage': loc = Location(id = x, name = 'кладовка', base_prob = 5, position = 'school')
            else: loc = Location(id = x, name = 'UNKNOWN', base_prob = 10, position = 'other')
            locations.append(loc)
            
    getEvents() #добавляю всем эвенты

init:
    image home = im.FactorScale('pic/locations/home/1.jpg', 1.5)
    image bedroom = im.FactorScale('pic/locations/home/2.jpg', 1.5)
    image bathroom = im.FactorScale('pic/locations/home/3.jpg', 1.5)
    image kitchen = im.FactorScale('pic/locations/home/4.jpg', 1.5)
    image street_day = im.FactorScale('pic/locations/street/1.jpg', 1.5)
    image street_night = im.FactorScale('pic/locations/street/2.jpg', 1.5)
    image beach_day = im.FactorScale('pic/locations/beach/1.jpg', 1.5)
    image beach_night = im.FactorScale('pic/locations/beach/2.jpg', 1.5)
    image beachChange_day = im.FactorScale('pic/locations/beach/changeRoom/1.jpg', 1.5)
    image beachChange_night = im.FactorScale('pic/locations/beach/changeRoom/2.jpg', 1.5)   
    image shopStreet_day = im.FactorScale('pic/locations/shopStreet/1.jpg', 1.5)
    image shopStreet_night = im.FactorScale('pic/locations/shopStreet/2.jpg', 1.5)
    image shop = im.FactorScale('pic/locations/shop/1.jpg', 1.5)
    image shopBeauty = im.FactorScale('pic/locations/shopBeauty/1.jpg', 1.5)
    image sex_shop = im.FactorScale('pic/locations/sex_shop/1.jpg', 1.3)
    image hall_day = im.FactorScale('pic/locations/school/hall/1.jpg', 1.5)
    image hall_night = im.FactorScale('pic/locations/school/hall/2.jpg', 1.5)
    image entrance_day = im.FactorScale('pic/locations/school/entrance/1.jpg', 1.5)
    image entrance_night = im.FactorScale('pic/locations/school/entrance/2.jpg', 1.5)
    image library_day = im.FactorScale('pic/locations/school/library/1.jpg', 1.5)
    image library_night = im.FactorScale('pic/locations/school/library/2.jpg', 1.5)
    image pool_day = im.FactorScale('pic/locations/school/pool/1.jpg', 1.5)
    image pool_night = im.FactorScale('pic/locations/school/pool/2.jpg', 1.5)
    image changeRoom = im.FactorScale('pic/locations/school/changeRoom/1.png', 1.5)
    image gym_day = im.FactorScale('pic/locations/school/gym/1.jpg', 1.5)
    image gym_night = im.FactorScale('pic/locations/school/gym/2.jpg', 1.5)
    image storage = im.FactorScale('pic/locations/school/storage/1.jpg', 1.5)
    image movie = Movie(size=(400, 300), xalign=0.2, yalign=0.5)
    image movie = Movie(size=(400, 300), xalign=0.8, yalign=0.5)

#Для теста
label test:
    python:
        player.dirty += 1
        player.coverSperm('ноги','лицо','рот','грудь','руки', 'вагина', 'анус')
        player.addItems('Салфетка','Салфетка','Салфетка')
    show daytime
    hide screen stats_screen
    screen empty:
        frame xalign 0.5 yalign 0.85:
            textbutton 'Назад' action Function(move, 'loc_home')
    call screen empty
    

##############################################################
#       Home
##############################################################
label loc_home:
    show expression im.FactorScale('pic/locations/home/1.jpg', 1.5) at left as home
    screen home:
        fixed:
            text 'Ваша маленькая квартира в этом миленьком городке. В центре комнаты стоит небольшой стеклянный столик, у стены вольготно расположилась полка с любимыми игрушками, которые Вы коллекционировали всю жизнь. Отсюда можно пойти в спальню или, если есть необходимость, в ванную. Слева выход в небольшую кухню.' xalign 0.0 yalign 1.0 style style.description
            textbutton 'Кухня' xalign 0.05 yalign 0.4 action Function(move, 'loc_kitchen')
            textbutton 'Спальня' xalign 0.05 yalign 0.5 action Function(move, 'loc_bedroom')
            textbutton 'Ванная' xalign 0.45 yalign 0.3 action Function(move, 'loc_bathroom')
            textbutton 'Улица' xalign 0.7 yalign 0.85 action Function(move, 'loc_street')
            textbutton 'Test' xalign 0.0 yalign 0.2 action Function(move,'test')
    call screen home

    label loc_bedroom:
        show bedroom at left
        screen bedroom:
            fixed:
                text 'Уютненькая маленькая спальня. Слева находится небольшой шкаф, в котором висит ваша повседневная одежда. Справа кровать, довольно удобная. Тут ещё есть телевизор, но он не работает, так что совсем не будет мешать Вам отходить ко сну.' xalign 0.0 yalign 1.0 style style.description
                textbutton 'Гостинная' xalign 0.5 yalign 0.8 action Function(move, 'loc_home')
        call screen bedroom
        return
        
    label loc_kitchen:
        show kitchen at left
        screen kitchen:
            fixed:
                text 'Микроволновка, плита, раковина, шкафчики. Кухня одним словом. \nОценив количество оставшейся еды, Вы прикидываете, что её хватит ещё на несколько раз.' xalign 0.0 yalign 1.0 style style.description
                textbutton 'Гостинная' xalign 0.5 yalign 0.8 action Function(move, 'loc_home')
                
        call screen kitchen
        return

    label loc_bathroom:
        show bathroom at left
        screen bathroom:
            fixed:
                text 'Ванная комната. Совмещённая. В лучших традициях далёкой страны. Тут можно искупаться, чтобы смыть с себя грязь и прочие человеческие нечистоты. А можно просто постоять под душем и отдохнуть.' xalign 0.0 yalign 1.0 style style.description
                textbutton 'Гостинная' xalign 0.5 yalign 0.8 action Function(move, 'loc_home')
                textbutton 'Душ' xalign 0.4 yalign 0.2 action Jump('shower')
                
        call screen bathroom
        return
    return

##############################################################
# SCHOOL
##############################################################
label loc_entrance:
    if hour >= 5 and hour <= 20:
        show entrance_day at left
    else:
        show entrance_night at left
    screen entrance:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Вход в Вашу новую школу. Ворота, крыльцо, всё как у всех, ничего необычного. Разве что кусты не особо пострижены, и дети там периодически играют, ну да ладно.' style style.description
                if is_library == 0:
                    text 'Слева от школы полно места. Вроде как там раньше стоял сарай, но он давным давно рухнул, и теперь земля пустует. Библиотеку чтоли там построить? ' style style.description
                else:
                    text 'Справа от школы виден вход в школьную библиотеку. В самом деле, замечательное приобретение! ' style style.description
                if is_wall == 0:
                    text 'Окидывая взглядом свои владения, вы видите прекрасный вид на окна школы. Выглядит конечно красиво, но как то всё напоказ. ' style style.description
                else:
                    text 'Довольно высокая стена окружает школу. С улицы вообще непонятно, толи это школа, толи режимный объект. ' style style.description
            textbutton 'Холл' xalign 0.456 yalign 0.7 action [Function(move, 'loc_hall')]
            textbutton 'Домой' xalign 0.1 yalign 0.7 action [Function(changetime, 30),Function(move, 'loc_street')]
            if is_library == 1: 
                textbutton 'Библиотека' xalign 0.8 yalign 0.7 action [Function(move, 'loc_library')]
    call screen entrance
    
    label loc_library:
        if hour >= 5 and hour <= 20:
            show library_day at left
        else:
            show libraryl_night at left
        screen library:
            fixed:
                vbox xalign 0.0 yalign 1.0:
                    text 'Недавно построенная школьная библиотека. Всё  сделано на удивление быстро и качественно. Городская библиотека выделила много книг на её заполнение, которые всё равно готовились списать.' style style.description
                    text 'В любом случае тут - прекрасное место для самообразования и не только!' style style.description
                textbutton 'Выход' xalign 0.5 yalign 0.8 action [Function(move, 'loc_entrance')]
        call screen library
        return
        
    label loc_hall:
        if hour >= 5 and hour <= 20:
            show hall_day at left
        else:
            show hall_night at left
        screen hall:
            fixed:
                vbox xalign 0.0 yalign 1.0:
                    text 'По всему холлу расставлены шкафчики для личных вещей. И еще лавочки, сидя на которых удобно переобуваться. В образующих шкафчиками коридорах легко потеряться с непривычки. По школе ходят ужасные истории, что из первого выпуска школы, ещё никто не вернулся домой. Так и бродят они до сих пор по коридорам, и воруют у новых учеников обувь, чтобы починить свои стоптанные за года блужданий ботинки. Глупая история, считаете Вы.' style style.description
                textbutton 'Первый этаж' xalign 0.1 yalign 0.7 action [Function(move, 'loc_first_floor')]
                textbutton 'Бассейн' xalign 0.8 yalign 0.7 action [Function(move, 'loc_pool')]
                textbutton 'Спортзал' xalign 0.8 yalign 0.6 action [Function(move, 'loc_gym')]
                textbutton 'Выход' xalign 0.5 yalign 0.8 action [Function(move, 'loc_entrance')]
        call screen hall

        label loc_pool:
            if hour >= 5 and hour <= 20:
                show pool_day at left
            else:
                show pool_night at left
            screen pool:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text 'Бассейн. Здесь проходят занятия по вторникам и четвергам. Хотя так же в перемены, и после уроков ученики могут придти сюда, чтобы поплавать или просто постоять глядя на воду. Вы так же можете немного потренировать своё здоровье, попытавшись проплыть стометровку пару раз.' style style.description
                        text 'Неподалеку от бассейна находится душ, где Вы в любой момент можете освежиться.' style style.description
                    textbutton 'Раздевалка' xalign 0.2 yalign 0.1 action [Function(move, 'loc_changeRoom')]
                    textbutton 'В душ' xalign 0.05 yalign 0.7 action Jump('shower')
                    textbutton 'Холл' xalign 0.5 yalign 0.8 action [Function(move, 'loc_hall')]
            call screen pool
            return
            
        label loc_changeRoom:
            show changeRoom at left
            screen changeRoom:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text 'Раздевалка. Она разделена на 2 отделения для мальчиков и девочек. Как ни странно, Вы тоже можете тут переодеваться. В отделении для девочек разумеется. Хотя кто знает, что там в соседнем отделении? Вы точно не знаете.' style style.description
                    textbutton 'Бассейн' xalign 0.2 yalign 0.8 action [Function(move, 'loc_pool')]
                    textbutton 'Спортзал' xalign 0.8 yalign 0.8 action [Function(move, 'loc_gym')]
            call screen changeRoom
            return    
            
        label loc_gym:
            if hour >= 5 and hour <= 20:
                show gym_day at left
            else:
                show gym_night at left
            screen gym:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text 'Раздевалка. Она разделена на 2 отделения для мальчиков и девочек. Как ни странно, Вы тоже можете тут переодеваться. В отделении для девочек разумеется. Хотя кто знает, что там в соседнем отделении? Вы точно не знаете.' style style.description
                    textbutton 'Кладовка' xalign 0.35 yalign 0.3 action [Function(move, 'loc_storage')]
                    textbutton 'Раздевалка' xalign 0.8 yalign 0.8 action [Function(move, 'loc_changeRoom')]
                    textbutton 'Холл' xalign 0.5 yalign 0.8 action [Function(move, 'loc_hall')]
            call screen gym
            
            label loc_storage:
                show storage at left
                screen storage:
                    fixed:
                        vbox xalign 0.0 yalign 1.0:
                            text 'Кладовка спорт инвентаря. В ней находятся мячи, маты, козлы и прочий спортинвентарь. Многие ученики  ходят сюда, чтобы немного отдохнуть и уединиться ото всех.' style style.description
                        textbutton 'Спортзал' xalign 0.5 yalign 0.8 action Function(move, 'loc_gym')
                call screen storage
                return
            return

        label first_floor:
            
            return
        return
    return

##############################################################
# OTHER
##############################################################
label loc_street:
    if hour >= 5 and hour <= 20:
        show street_day at left
    else:
        show street_night at left
    screen street:
        fixed:
            vbox xalign 0.0 yalign 1.0:
                text 'Простая улица на которой стоит Ваш дом. Вдоль улицы стоят другие дома ваших соседей. Кто знает, может быть где то по соседству живёт кто то из вашей школы?".' style style.description
                text 'Улица пересекает почти весь небольшой городок, и в конце упирается в улицу "Торговая".' style style.description
                if hour >= 5 and hour <= 20: 
                     text 'Посмотрев вдоль, Вы видите пару бегущих людей. Действительно, улица чрезвычайно удобна для пробежек.' style style.description
                else:
                     text 'Посмотрев вдоль, Вы больше не видите бегущих людей. Наверное убежали. Или же просто ночь наступила?' style style.description
            textbutton 'Домой' xalign 0.2 yalign 0.3 action Function(move, 'loc_home')
            textbutton 'Пляж' xalign 0.7 yalign 0.8 action [Function(changetime, 30),Function(move, 'loc_beach')]
            textbutton 'Торговая улица' xalign 0.35 yalign 0.3 action [Function(changetime, 15),Function(move, 'loc_shopStreet')]
            textbutton 'Школа' xalign 0.5 yalign 0.8 action [Function(changetime, 30),Function(move, 'loc_entrance')]
    call screen street
    
    label loc_beach:
        if hour >= 5 and hour <= 20:
            show beach_day at left
        else:
            show beach_night at left
        screen beach:
            fixed:
                vbox xalign 0.0 yalign 1.0:
                    text 'Пляж, просто пляж. На нём можно неплохо загореть, если уделить этому недельку времени, или же просто искупаться.' style style.description
                textbutton 'К дому' xalign 0.5 yalign 0.8 action [Function(changetime, 30),Function(move, 'loc_street')]
                textbutton 'Раздевалка' xalign 0.7 yalign 0.45 action Function(move, 'loc_beachChange')
        call screen beach
        
        label loc_beachChange:
            if hour >= 5 and hour <= 20:
                show beachChange_day at left
            else:
                show beachChange_night at left
            screen beachChange:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text 'Специально обустроенные комнатки для переодеваний. Внутри небольшая полочка для вещей, умывальник и полотенце. Очень удобно, хотя и необычно.' style style.description
                    textbutton 'Пляж' xalign 0.5 yalign 0.8 action Function(move, 'loc_beach')
            call screen beachChange
            return
    return
        
    label loc_shopStreet:
        if hour >= 5 and hour <= 20:
            show shopStreet_day at left
        else:
            show shopStreet_night at left
            screen shopStreet:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text 'Торговая улица! На ней много всяких маленьких магазинчиков, в которых закупается весь город. Говорят, что в некоторых странах Есть ОГРОМНЫЕ магазины, в которых есть ВСЁ. Но это как то бездушно. Зачем тебе это всё, когда души то нет?' style style.description
                        text 'Мини маркет работает круглосуточно.' style style.description
                        text 'Салон красоты работает с 8 до 19 ежедневно.' style style.description
                    textbutton 'К дому' xalign 0.5 yalign 0.8 action [Function(changetime, 15),Function(move, 'loc_street')]
                    textbutton 'Магазин' xalign 0.4 yalign 0.5 action [Function(move, 'loc_shop')]
                    if hour >=8 and hour <= 19: 
                        textbutton 'Салон\nКрасоты' xalign 0.2 yalign 0.55 action [Function(move, 'loc_shopBeauty')]
                        textbutton 'Сексшоп' xalign 0.65 yalign 0.45 action [Function(move, 'loc_sex_shop')]
        call screen shopStreet
        

        label loc_shop:
            show shop at left
            screen shop:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text 'Круглосуточный магазин, единственный в Вашем районе. После прогулки в нем Вы сможете без промедления набрать еды на кухню, выбрать себе напитки напитки и некоторые иные вещи.' style style.description
                    textbutton 'Назад' xalign 0.5 yalign 0.8 action [Function(move, 'loc_shopStreet')]
            call screen shop
            return
            
        label loc_shopBeauty:
            show shopBeauty at left
            screen shopBeauty:
                fixed:
                    vbox xalign 0.0 yalign 1.0:
                        text 'Салон красоты приветствует Вас чистым полом и ярким рецепшеном. Наверняка тут предлагают великолепные по качеству услуги для улучшения внешности, если природа Вас обделила. Хотя и прирождённым красавицам они безусловно тоже помогут стать ещё красивее. Вот только цена, не отпугнёт ли она случайного клиента?' style style.description
                    textbutton 'Назад' xalign 0.5 yalign 0.8 action [Function(move, 'loc_shopStreet')]
            call screen shopBeauty
            return
            
        label loc_sex_shop:
                show sex_shop at left
                screen sex_shop:
                    fixed:
                        vbox xalign 0.0 yalign 1.0:
                            text 'Вы видите перед собой магазин для взрослых. Полки уставлены различными игрушками для взрослых. Дилдо, вибраторы, резиновые дырки для мальчиков, пони с уникальным седлом для девочек. Отдельная полка для афродизиаков и прочей медицины. Глаза прямо разбегаются от обилия выбора!' style style.description
                        textbutton 'Назад' xalign 0.5 yalign 0.8 action [Function(move, 'loc_shopStreet')]
                call screen sex_shop
                return
        return
    return


label look_around:
    hide screen stats_screen
    screen grid_test:
        frame:
            vbox:
                grid 2 2:
                    text 'Кто то слева'
                    text 'Кто то справа'
                    text 'Кто то слева'
                    text 'Кто то справа'
                textbutton 'Назад' action Function(move, curloc)
    call screen grid_test
    return