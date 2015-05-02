
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
    #Массивы имён
    fn_male = ['Александр','Андрей','Владимир','Алексей','Дмитрий','Николай','Евгений','Иван','Михаил','Егор','Тимур','Руслан','Максим','Даниил','Кирилл','Никита','Денис','Илья','Артем','Артур','Роман','Богдан','Глеб','Захар','Владислав','Ян','Павел','Юрий','Антон','Игорь','Степан','Вадим','Семен','Лев','Федор','Филипп','Виктор','Виталий','Олег']
    fn_female = ['Софья','Мария','Анастасия','Дарья','Анна','Елизавета','Полина','Виктория','Екатерина','Варвара','Ксения','Александра','Алиса','Вероника','Арина','Валерия','Маргарита','Василиса','Ульяна','Алина','Милана','Ева','Алёна','Юлия','Диана','Кристина','Ольга','Вера','Татьяна','Ирина','Яна','Елена','Евгения','Ангелина','Марина','Светлана','Надежда','Олеся','Наталья','Ника']
    ln = ['Смирнов','Иванов','Кузнецов','Попов','Соколов','Козлов','Новиков','Морозов','Петров','Волков','Соловьев','Васильев','Зайцев','Павлов','Семенов','Голубев','Виноградов','Богданов','Воробьев','Федоров','Михайлов','Беляев','Тарасов','Белов','Комаров','Орлов','Киселев','Макаров','Андреев','Ковалев','Ильин','Гусев','Титов','Кузьмин','Кудрявцев','Баранов','Куликов','Алексеев','Степанов','Яковлев']
    #Массив полов
    lsex = ['male','female','futa']
    #Массив картинок
    for x in range (1,31):
        picto_m.append('pic/events/students/picto/male/%d.jpg' % x)
        
    for x in range (1,41):
        picto_f.append('pic/events/students/picto/female/%d.jpg' % x)
    #определение длинн массивов.
    end_fn_male = len(fn_male) - 1 
    end_fn_female = len(fn_female) - 1 
    end_ln = len(ln) - 1 
    
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
        player = Char(
            fname = _fname,
            lname = _lname,
            age = _age,
            sex = lsex[1],
            bsize = _bsize,
            psize = 0,
            vsize = _vagina,
            asize = _anus,
            height = 175,
            color = '#5A20F7',
            loy = 0,
            fun = 0,
            inventory = [],
            wear = [],
            corr = _corr,
            lust = _corr/10,
            will = 0,
            edu = _intel/2,
            club = '',
            picto = _picture,
            energy = _health,
            health = _health,
            intel = _intel,
            location = curloc,
            money = _money,
            beauty = _beauty,
            dirty = 0,
            rep = 0,
            body = genBody()
            )
        player.addItems('Салфетка', 'Сырая еда')
#####################################################
#Генерация и создание студентов
#####################################################
        for x in range(1,students+1):
            #выбор пола
            _rand = rand(1, 10)
            if _rand < 5:
                _sex = lsex[0]
            elif _rand == 6:
                _sex = lsex[2]
            else:
                _sex = lsex[1]
            #Если мальчик
            if _sex == lsex[0]:
                _fname = fn_male[rand(0,end_fn_male)]
                _lname = ln[rand(0,end_ln)]
                _age = rand(12,16)
                _bsize = 0
                _psize = randf(10,15)
                _vsize = 0
                _asize = randf(0,1)
                _height = rand(140,170)
                _color = '#269AFF'
                _loy = randf(0,10)
                _fun = randf(10,20)
                _inventory = []
                _wear = []
                _corr = randf(0,5)
                _lust = randf(0,5)
                _will = randf(0,100)
                _intel = randf(0,100)
                _edu = _intel/4
                _club = ''
                _picto = picto_m[rand(0,len(picto_m) - 1 )]
                picto_m.remove(_picto)
                _health = randf(800,1200)
                _energy = _health
            #Девочка
            if _sex == lsex[1]:
                _fname = fn_female[rand(0,end_fn_female)]
                _lname = ln[rand(0,end_ln)]+'а'
                _age = rand(12,16)
                _bsize = randf(0,3)
                _psize = 0
                _vsize = randf(0,1)
                _asize = randf(0,1)
                _height = rand(140,170)
                _color = '#FF85F1'
                _loy = randf(0,10)
                _fun = randf(10,20)
                _inventory = []
                _wear = []
                _corr = randf(0,5)
                _lust = randf(0,5)
                _will = randf(0,100)
                _intel = randf(0,100)
                _edu = _intel/4
                _club = ''
                _picto = picto_f[rand(0,len(picto_f) - 1 )]
                picto_f.remove(_picto)
                _health = randf(800,1200)
                _energy = _health
            #Фута
            if _sex == lsex[2]:
                _fname = fn_female[rand(0,end_fn_female)]
                _lname = ln[rand(0,end_ln)]+'а'
                _age = rand(12,16)
                _bsize = randf(0,3)
                _psize = randf(10,15)
                _vsize = randf(0,1)
                _asize = randf(0,1)
                _height = rand(140,170)
                _color = '#FC3A3A'
                _loy = randf(0,10)
                _fun = randf(10,20)
                _inventory = []
                _wear = []
                _corr = randf(0,5)
                _lust = randf(0,5)
                _will = randf(0,100)
                _intel = randf(0,100)
                _edu = _intel/4
                _club = ''
                _picto = picto_f[rand(0,len(picto_f) - 1 )]
                picto_f.remove(_picto)
                _health = randf(800,1200)
                _energy = _health
            #Создание объекта из сгенерированных кусков
            temp_char = Char(
                fname = _fname,
                lname = _lname,
                age = _age,
                sex = _sex,
                bsize = _bsize,
                psize = _psize,
                vsize = _vsize,
                asize = _asize,
                height = _height,
                color = _color,
                loy = _loy,
                fun = _fun,
                inventory = _inventory,
                wear = _wear,
                corr = _corr,
                lust = _lust,
                will = _will,
                edu = _edu,
                club = _club,
                picto = _picto,
                energy = _energy,
                health = _health,
                intel = _intel,
                location = 'street',
                money = rand(0,100),
                beauty = rand(30,85),
                dirty = 0,
                rep = 50,
                body = genBody()
                )
            #Добавление объекта к массиву студентов
            _studs.append(temp_char)
            
#######################################################
#Создание учителей
#######################################################
        kupruvna = Char(
            fname = 'Валентина',
            lname = 'Купрувна',
            age = 37,
            sex = 'female',
            bsize = 5,
            psize = 0,
            vsize = 8,
            asize = 0,
            height = 170,
            color = '#FF85F1',
            loy = randf(10,20),
            fun = randf(0,50),
            inventory = [],
            wear = [],
            corr = 0,
            lust = 0,
            will = 25,
            edu = 60,
            club = 'химия',
            picto = 'pic/events/teachers/50/picto.png',
            health = 1000,
            energy = 1000,
            intel = 50,
            location = curloc,
            money = 10000,
            beauty = 40,
            dirty = 0,
            rep = 0,
            body = genBody()
            )
        _teachers.append(kupruvna)
        
        danokova = Char(
            fname = 'Полина',
            lname = 'Данокова',
            age = 25,
            sex = 'female',
            bsize = 2,
            psize = 0,
            vsize = 5,
            asize = 0,
            height = 160,
            color = '#FF85F1',
            loy = randf(10,20),
            fun = randf(0,50),
            inventory = [],
            wear = [],
            corr = 0,
            lust = 0,
            will = 45,
            edu = 20,
            club = 'биология',
            picto = 'pic/events/teachers/51/picto.png',
            health = 1000,
            energy = 1000,
            intel = 100,
            location = curloc,
            money = 5000,
            beauty = 60,
            dirty = 0,
            rep = 0,
            body = genBody()
            )
        _teachers.append(danokova)
        
        frigidovna = Char(
            fname = 'Ангелина',
            lname = 'Фригидовна',
            age = 32,
            sex = 'female',
            bsize = 6,
            psize = 0,
            vsize = 0,
            asize = 0,
            height = 175,
            color = '#FF85F1',
            loy = randf(10,20),
            fun = randf(0,50),
            inventory = [],
            wear = [],
            corr = 0,
            lust = 0,
            will = 30,
            edu = 15,
            club = 'сексуальное просвящение',
            picto = 'pic/events/teachers/52/picto.png',
            health = 1000,
            energy = 1000,
            intel = 40,
            location = curloc,
            money = 5000,
            beauty = 40,
            dirty = 0,
            rep = 0,
            body = genBody()
            )
        _teachers.append(frigidovna)
        
        bissektrisovna = Char(
            fname = 'Валентина',
            lname = 'Биссектрисовна',
            age = 35,
            sex = 'female',
            bsize = 3,
            psize = 0,
            vsize = 8,
            asize = 0,
            height = 165,
            color = '#FF85F1',
            loy = randf(10,20),
            fun = randf(0,50),
            inventory = [],
            wear = [],
            corr = 0,
            lust = 0,
            will = 60,
            edu = 60,
            club = 'математика',
            picto = 'pic/events/teachers/53/picto.png',
            health = 1000,
            energy = 1000,
            intel = 40,
            location = curloc,
            money = 5000,
            beauty = 85,
            dirty = 0,
            rep = 0,
            body = genBody()
            )
        _teachers.append(bissektrisovna)
        
        dikovna = Char(
            fname = 'Анжела',
            lname = 'Диковна',
            age = 23,
            sex = 'futa',
            bsize = 5,
            psize = 20,
            vsize = 8,
            asize = 4,
            height = 180,
            color = '#FC3A3A',
            loy = randf(10,20),
            fun = randf(0,50),
            inventory = [],
            wear = [],
            corr = 20,
            lust = 0,
            will = 30,
            edu = 50,
            club = 'английский язык',
            picto = 'pic/events/teachers/54/picto.png',
            health = 1000,
            energy = 1000,
            intel = 50,
            location = curloc,
            money = 5000,
            beauty = 60,
            dirty = 0,
            rep = 0,
            body = genBody()
            )
        _teachers.append(dikovna)

        mustangovich = Char(
            fname = 'Ахмед',
            lname = 'Мустангович',
            age = 22,
            sex = 'male',
            bsize = 0,
            psize = 30,
            vsize = 0,
            asize = 0,
            height = 190,
            color = '#269AFF',
            loy = randf(40,60),
            fun = randf(0,50),
            inventory = [],
            wear = [],
            corr = 0,
            lust = 0,
            will = 15,
            edu = 300,
            club = 'физкультура',
            picto = 'pic/events/teachers/55/picto.png',
            health = 1500,
            energy = 1500,
            intel = 40,
            location = curloc,
            money = 200,
            beauty = 40,
            dirty = 0,
            rep = 0,
            body = genBody()
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
   