
init -10 python:
    config.use_cpickle = True
    dynpicto = ''

init -2 python:
    #############################################################
    #Создание студентов
    #############################################################
    #объявление массивов
    picto_m = []
    picto_f = []
    _studs = []
    _allStuds = []
    _allChars = []
    _teachers = []
    #будущий массив студентов
    #Массив картинок
    for x in range (1,31):
        picto_m.append('pic/events/students/picto/male/%d.jpg' % x)

    for x in range (1,41):
        picto_f.append('pic/events/students/picto/female/%d.jpg' % x)

#####################################################
#Генерация директора
#####################################################

init -1 python:
    _fname = 'Имя'
    _lname = 'Фамилия'
    _age = 25
    _beauty = 20
    _health = 700
    _anus = randf(0,5)
    _vagina = randf(0,10)
    _corr = 0
    _intel = 50
    _money = 5000
    _bsize = 2
    _picture = "pic/Hero/2.png"
    history = 0
    answer = [0,0,0,0,0]


label gendir:
    show white
    show expression 'pic/new.jpg' at Position(xpos = 0.6, xanchor=0.5, ypos=0.6, yanchor=0.5)
    menu:
        'Имя: [_fname]':
            $ _fname = renpy.input("Введите имя, и нажмите Enter для продолжения", default= _fname, exclude='{1234567890}')
            jump gendir
        'Отчество: [_lname]':
            $ _lname = renpy.input("Введите отчество, и нажмите Enter для продолжения", default= _lname, exclude='{1234567890}')
            jump gendir
        "Выбрать историю" if _fname != '' and _lname != '':
            jump history
        "Закончить" if answer == [1,1,1,1,1]:
            jump skipall

label history:
    menu:
        "Младенчество" if answer[0] == 0:
            $ answer[0] = 1
            menu:
                'Вы родились красивой девочкой\n+Красота -Интеллект':
                    $ _beauty += 20
                    $ _intel -= 5
                    jump history
                'Вы смогли вставать на ножки уже в 3-х месячном возрасте\n+Здоровье':
                    $ _health += 150
                    jump history
                'Вы обожали сосать сиську, даже когда не были голодны\n+Развратность +Грудь +Дырочки --Интеллект':
                    $ _corr += 15
                    $ _anus += 5
                    $ _vagina += 5
                    $ _intel -= 10
                    $ _bsize += 1
                    jump history
                'Вы смогли осмысленно говорить уже в пол года\n ++Интеллект':
                    $ _intel += 10
                    jump history
                'Вы обожали яркие и блестящие предметы.\n +Деньги':
                    $ _money += 5000
                    jump history
        "Детство" if answer[1] == 0:
            $ answer[1] = 1
            menu:
                'Вы любили смотреть, как красится ваша мама\n+Красота -Интеллект':
                    $ _beauty += 20
                    $ _intel -= 5
                    jump history
                'Вы были очень активным ребёнком\n+Здоровье':
                    $ _health += 150
                    jump history
                'Вы показывали свою письку мальчишкам в детском саду\n+Развратность +Дырочки --Интеллект':
                    $ _corr += 15
                    $ _anus += 5
                    $ _vagina += 5
                    $ _intel -= 10
                    jump history
                'Вы рано научились читать\n ++Интеллект':
                    $ _intel += 10
                    jump history
                'Вы откладывали деньги, которые Вам давали на сладости.\n +Деньги':
                    $ _money += 5000
                    jump history
        "Школа" if answer[2] == 0:
            $answer[2] = 1
            menu:
                'В школе Вы старались выглядеть лучше своих подруг\n+Красота -Интеллект':
                    $ _beauty += 20
                    $ _intel -= 5
                    jump history
                'Вашим любимым предметом была физкультура\n+Здоровье':
                    $ _health += 150
                    jump history
                'Вы любили мастурбировать на занятиях\n+Развратность +Дырочки --Интеллект':
                    $ _corr += 15
                    $ _anus += 5
                    $ _vagina += 5
                    $ _bsize += 1
                    $ _intel -= 10
                    jump history
                'Вы принимали участие в олимпиадах, и даже занимали там призовые места\n ++Интеллект':
                    $ _intel += 10
                    jump history
                'Вы экономили на обедах, чтобы купить себе что нибудь дорогое\n +Деньги':
                    $ _money += 5000
                    jump history
        "Университет" if answer[3] == 0:
            $answer[3] = 1
            menu:
                ' Вы всегда старались быть накрашенной и ухоженной\n+Красота -Интеллект':
                    $ _beauty += 20
                    $ _intel -= 5
                    jump history
                'Вы участвовали во всех спартакиадах, и даже занимали там призовые места\n+Здоровье':
                    $ _health += 150
                    jump history
                'Вы с лёгкостью меняли сексуальных партнёров\n+Развратность +Дырочки --Интеллект':
                    $ _corr += 15
                    $ _anus += 5
                    $ _vagina += 5
                    $ _intel -= 10
                    jump history
                'Вы любили естественные науки, и всегда получали по ним хорошие оценки\n ++Интеллект':
                    $ _intel += 10
                    jump history
                'Вы давали деньги в рост одноклассникам. И Вам их даже возвращали с процентами\n +Деньги':
                    $ _money += 5000
                    jump history
        "Работа" if answer[4] == 0:
            $answer[4] = 1
            menu:
                'Вы тщательно следите за собой, и регулярно посещаете парикмахерские и салоны красоты\n+Красота -Интеллект':
                    $ _beauty += 20
                    $ _intel -= 5
                    jump history
                'Вы бегаете утром, и следите за своим здоровьем\n+Здоровье':
                    $ _health += 150
                    jump history
                'Вы использовали своё тело для продвижения по карьерной лестнице\n+Развратность +Дырочки +Грудь --Интеллект':
                    $ _corr += 15
                    $ _anus += 5
                    $ _vagina += 5
                    $ _bsize += 1
                    $ _intel -= 10
                    jump history
                'Вы регулярно повышаете свой уровень образования\n ++Интеллект':
                    $ _intel += 10
                    jump history
                'Вы любите деньги, а они любят вас\n +Деньги':
                    $ _money += 5000
                    jump history
        "Назад":
            jump gendir
        "Сбросить историю":
            $ answer = [0,0,0,0,0]
            jump history

label selchar:
    show white
    call screen char_select

label skipall:
    python:
#####################################################
#Создание директора
#####################################################
        playerBody = FemaleBody(175)
        playerBody.parts['грудь'].size = _bsize
        playerBody.parts['анус'].size = _anus
        playerBody.parts['вагина'].size = _vagina

        playerStats = Stats(
            corruption = _corr,
            lust = _corr / 10,
            education  = _intel / 2,
            intelligence = _intel,
            health = _health,
            energy = _health,
            beauty = _beauty,
        )

        player = Char(
            fname = _fname,
            lname = _lname,
            age = _age,
            body = playerBody,
            stats = playerStats,
            color = '#5A20F7',
            inventory = [],
            wear = [],
            club = '',
            picto = _picture,
            location = curloc,
            money = _money
        )
        player.addItems('Салфетка', 'Сырая еда', jaket.name, longSkirt.name, browntights.name, simpleUnderwear.name)
        player.say = Character (player.fullName(), kind=adv, dynamic = False, color = player.color, show_side_image = Image(player.picto, xalign=0.0, yalign=1.0, yanchor="center"), window_left_padding = 170)
#####################################################
#Генерация и создание студентов
#####################################################
        for x in range(1,students+1):
            #выбор пола
            _rand = rand(1, 10)
            sex = ''
            if _rand < 5:
                sex = 'female'
            elif _rand == 6:
                sex = 'futa'
            else:
                sex = 'male'
            
            if sex == 'male':
                picto = choice(picto_m) 
                picto_m.remove(picto)
            else :
                picto = choice(picto_f)
                picto_f.remove(picto)
            
            _studs.append(Char.random(sex, picto))

#######################################################
#Создание учителей
#######################################################

        kupruvna = Char(
            fname = 'Валентина',
            lname = 'Купрувна',
            age = 37,
            body = FemaleBody(
                175,
                breastSize = 5,
                vaginaSize = 8
            ),
            stats = Stats(
                will = 25,
                education = 60,
                intelligence = 50,
                beauty = 40,
                health = 1000,
                energy = 1000,
                loyalty = randf(10, 20),
                fun = randf(0, 50)
            ),
            color = '#FF85F1',
            inventory = [],
            wear = [],
            club = 'химия',
            picto = 'pic/events/teachers/50/picto.png',
            location = curloc,
            money = 10000
        )
        _teachers.append(kupruvna)

        danokova = Char(
            fname = 'Полина',
            lname = 'Данокова',
            age = 25,
            body = FemaleBody(
                160,
                breastSize = 2,
                vaginaSize = 5
            ),
            stats = Stats(
                will = 45,
                education = 20,
                intelligence = 100,
                beauty = 60,
                health = 1000,
                energy = 1000,
                loyalty = randf(10, 20),
                fun = randf(0, 50)
            ),
            color = '#FF85F1',
            inventory = [],
            wear = [],
            club = 'биология',
            picto = 'pic/events/teachers/51/picto.png',
            location = curloc,
            money = 5000
        )
        _teachers.append(danokova)

        frigidovna = Char(
            fname = 'Ангелина',
            lname = 'Фригидовна',
            age = 32,
            body = FemaleBody(
                175,
                breastSize = 6
            ),
            stats = Stats(
                will = 30,
                education = 15,
                intelligence = 40,
                beauty = 40,
                health = 1000,
                energy = 1000,
                loyalty = randf(10, 20),
                fun = randf(0, 50)
            ),
            color = '#FF85F1',
            inventory = [],
            wear = [],
            club = 'сексуальное просвящение',
            picto = 'pic/events/teachers/52/picto.png',
            location = curloc,
            money = 5000
        )
        _teachers.append(frigidovna)

        bissektrisovna = Char(
            fname = 'Валентина',
            lname = 'Биссектрисовна',
            age = 35,
            body = FemaleBody(
                165,
                breastSize = 3,
                vaginaSize = 8
            ),
            stats = Stats(
                will = 60,
                education = 60,
                intelligence = 40,
                beauty = 85,
                health = 1000,
                energy = 1000,
                loyalty = randf(10, 20),
                fun = randf(0, 50)
            ),
            color = '#FF85F1',
            inventory = [],
            wear = [],
            club = 'математика',
            picto = 'pic/events/teachers/53/picto.png',
            location = curloc,
            money = 5000
        )
        _teachers.append(bissektrisovna)

        dikovna = Char(
            fname = 'Анжела',
            lname = 'Диковна',
            age = 23,
            body = FutaBody(
                180,
                breastSize = 5,
                vaginaSize = 8,
                anusSize = 4,
                penisSize = 20
            ),
            stats = Stats(
                corruption = 20,
                will = 30,
                education = 50,
                intelligence = 50,
                beauty = 60,
                health = 1000,
                energy = 1000,
                loyalty = randf(10, 20),
                fun = randf(0, 50)
            ),
            color = '#FC3A3A',
            inventory = [],
            wear = [],
            club = 'английский язык',
            picto = 'pic/events/teachers/54/picto.png',
            location = curloc,
            money = 5000
        )
        _teachers.append(dikovna)

        mustangovich = Char(
            fname = 'Ахмед',
            lname = 'Мустангович',
            age = 22,
            body = MaleBody(
                190,
                penisSize = 30
            ),
            stats = Stats(
                will = 15,
                education = 300,
                intelligence = 40,
                beauty = 40,
                health = 1500,
                energy = 1500,
                loyalty = randf(40, 60),
                fun = randf(0, 50)
            ),
            color = '#269AFF',
            inventory = [],
            wear = [],
            club = 'физкультура',
            picto = 'pic/events/teachers/55/picto.png',
            location = curloc,
            money = 200
        )
        _teachers.append(mustangovich)
#######################################################
#Пересохранение этого добра для того, чтобы сохранялось.
#######################################################
    $ _allChars.extend(_studs)
    $ _allChars.extend(_teachers)
    $ allChars = _allChars
    $ studs = _studs
    $ teachers = _teachers
    $ move("loc_home")
