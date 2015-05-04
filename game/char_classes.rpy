init -20 python:
    import copy
    from random import choice

    ###################################################################
    #Класс частей тела
    ###################################################################

    class BodyPart():
        def __init__(self, name, visibility = False, sperm = False, size = 0, maxSize = 0, minSize = 0):
            self.name = name
            self.visibility = visibility
            self.sperm = sperm
            self.size = size
            self.minSize = minSize
            self.maxSize = maxSize

        def normalize(self):
            self.size = max(self.minSize, min(self.size, self.maxSize))


    # Общий класс тела с частями, общими для всех
    class Body(object):
        def __init__(self, height = 140, bodyparts = {}):
            self.parts = {}
            self.parts['ноги'] = BodyPart('ноги', True)
            self.parts['лицо'] = BodyPart('лицо', True)
            self.parts['грудь'] = BodyPart('грудь', True, minSize = 0, maxSize = 10)
            self.parts['анус'] = BodyPart('анус', minSize = 0, maxSize = 25)
            self.parts['рот'] = BodyPart('рот')
            self.parts['руки'] = BodyPart('руки', True)
            self.height = height

            # Копируем и перезаписываем части тела, если надо
            for k,v in bodyparts:
                self.parts[k] = v

        @classmethod
        def random(cls):
            body = cls(height = rand(140, 170))
            body.parts['анус'].size = randf(0, 1)
            return body

        def normalize(self):
            for _,v in self.parts.iteritems():
                v.normalize()

        def sex(self):
            return 'U wot m8'

        def partsWithSperm(self):
            return [v for k,v in self.parts.iteritems() if v.sperm]


    # Мужское тело
    class MaleBody(Body):
        def __init__(self, height, bodyparts = {}, anusSize = 0, penisSize = 0):
            super(MaleBody, self).__init__(height, bodyparts)
            self.parts['пенис'] = BodyPart('пенис', minSize = 0, maxSize = 30, size = penisSize) #
            self.parts['анус'].size = anusSize

        @classmethod
        def random(cls):
            body = super(MaleBody, cls).random()
            body.parts['пенис'].size = randf(10, 15)
            return body

        def sex(self):
            return 'male'

    # Женское тело
    class FemaleBody(Body):
        def __init__(self, height, bodyparts = {}, anusSize = 0, vaginaSize = 0, breastSize = 0):
            super(FemaleBody, self).__init__(height, bodyparts)
            self.parts['вагина'] = BodyPart('вагина', minSize = 0, maxSize = 25, size = vaginaSize)
            self.parts['анус'].size = anusSize
            self.parts['грудь'].size = breastSize

        @classmethod
        def random(cls):
            body = super(FemaleBody, cls).random()
            body.parts['вагина'].size = randf(0, 1)
            body.parts['грудь'].size = randf(0, 3)
            return body

        def sex(self):
            return 'female'

    # Фута
    class FutaBody(Body):
        def __init__(self, height, bodyparts = {}, anusSize = 0, vaginaSize = 0, penisSize = 0, breastSize = 0):
            super(FutaBody, self).__init__(height, bodyparts)
            self.parts['вагина'] = BodyPart('вагина', minSize = 0, maxSize = 25, size = vaginaSize)
            self.parts['пенис'] = BodyPart('пенис', minSize = 0, maxSize = 30, size = penisSize)
            self.parts['анус'].size = anusSize
            self.parts['грудь'].size = breastSize

        @classmethod
        def random(cls):
            body = super(FutaBody, cls).random()
            body.parts['пенис'].size = randf(10, 15)
            body.parts['вагина'].size = randf(0, 1)
            body.parts['грудь'].size = randf(0, 3)
            return body

        def sex(self):
            return 'futa'

    # Параметры персонажа
    class Stats:
        def __init__(self, **stats):
            self.loyalty = stats['loyalty'] if 'loyalty' in stats else 0
            self.fun = stats['fun'] if 'fun' in stats else 0
            self.corruption = stats['corruption'] if 'corruption' in stats else 0
            self.lust = stats['lust'] if 'lust' in stats else 0
            self.will = stats['will'] if 'will' in stats else 0
            self.education = stats['education'] if 'education' in stats else 0
            self.health = stats['health'] if 'health' in stats else 0
            self.intelligence = stats['intelligence'] if 'intelligence' in stats else 0
            self.beauty = stats['beauty'] if 'beauty' in stats else 0
            self.reputation = stats['reputation'] if 'reputation' in stats else 0
            self.energy = stats['energy'] if 'energy' in stats else 0
            self.dirty = stats['dirty'] if 'dirty' in stats else 0

        def normalize(self):
            self.loyalty = min(max(self.loyalty,0),100)
            self.fun = min(max(self.fun,0),100)
            self.corruption = min(max(self.corruption,0),100)
            self.lust = min(max(self.lust,0),100)
            self.will = min(max(self.will,0),100)
            self.education = min(max(self.education,0),150)
            self.health = min(max(self.health,0),2000)
            self.energy = min(max(self.energy,0),self.health)
            self.intelligence = min(max(self.intelligence,0),100)
            self.beauty = min(max(self.beauty,0),200)
            self.dirty = min(max(self.dirty,0),30)
            self.reputation = min(max(self.reputation,0),100)

        @classmethod
        def random(cls):
            stats = cls()
            stats.loyalty = randf(0, 10)
            stats.fun = randf(10, 20)
            stats.corruption = randf(0, 5)
            stats.lust = randf(0, 5)
            stats.will = randf(0, 100)
            stats.intelligence = randf(0, 100)
            stats.education = stats.intelligence / 4
            stats.health = randf(800, 1200)
            stats.energy = stats.health
            return stats

    class Char(object):

        # Мужские имена
        maleNames = ['Александр', 'Андрей', 'Владимир', 'Алексей', 'Дмитрий', 'Николай', 'Евгений', 'Иван', 'Михаил', 'Егор', 'Тимур', 'Руслан', 'Максим', 'Даниил', 'Кирилл', 'Никита', 'Денис', 'Илья', 'Артем', 'Артур', 'Роман', 'Богдан', 'Глеб', 'Захар', 'Владислав', 'Ян', 'Павел', 'Юрий', 'Антон', 'Игорь', 'Степан', 'Вадим', 'Семен', 'Лев', 'Федор', 'Филипп', 'Виктор', 'Виталий', 'Олег']

        # Женские имена
        femaleNames = ['Софья', 'Мария', 'Анастасия', 'Дарья', 'Анна', 'Елизавета', 'Полина', 'Виктория', 'Екатерина', 'Варвара', 'Ксения', 'Александра', 'Алиса', 'Вероника', 'Арина', 'Валерия', 'Маргарита', 'Василиса', 'Ульяна', 'Алина', 'Милана', 'Ева', 'Алёна', 'Юлия', 'Диана', 'Кристина', 'Ольга', 'Вера', 'Татьяна', 'Ирина', 'Яна', 'Елена', 'Евгения', 'Ангелина', 'Марина', 'Светлана', 'Надежда', 'Олеся', 'Наталья', 'Ника']

        # Фамилии
        lastNames = ['Смирнов', 'Иванов', 'Кузнецов', 'Попов', 'Соколов', 'Козлов', 'Новиков', 'Морозов', 'Петров', 'Волков', 'Соловьев', 'Васильев', 'Зайцев', 'Павлов', 'Семенов', 'Голубев', 'Виноградов', 'Богданов', 'Воробьев', 'Федоров', 'Михайлов', 'Беляев', 'Тарасов', 'Белов', 'Комаров', 'Орлов', 'Киселев', 'Макаров', 'Андреев', 'Ковалев', 'Ильин', 'Гусев', 'Титов', 'Кузьмин', 'Кудрявцев', 'Баранов', 'Куликов', 'Алексеев', 'Степанов', 'Яковлев']

        def __init__(self, fname = '', lname = '', color = '#FFFFFF', age = 0, body = Body(), stats = Stats(), inventory = [], wear = [], club = '', picto = '', location = '', money = 0):
            self.fname = fname
            self.lname = lname
            self.age = age
            self.body = body
            self.stats = stats
            self.color = color
            self.inventory = inventory
            self.wear = wear
            self.club = club
            self.picto = picto
            self.location = location
            self.money = money
            self.say = Character (self.fullName(), kind=adv, dynamic = False, color = self.color, show_side_image = Image(self.picto, xalign=0.0, yalign=1.0), window_left_padding = 170)
            config.side_image_tag = self.picto

        # Создание случайного персонажа с полом sex ('male', 'female' или 'futa') и картинкой picto
        @classmethod
        def random(cls, sex, picto):
            #выбор пола
            body = Body()
            if sex == 'female':
                body = FemaleBody.random()
            elif sex == 'futa':
                body = FutaBody.random()
            elif sex == 'male':
                body = MaleBody.random()

            stats = Stats.random()
            firstName = choice(cls.maleNames) if body.sex() == 'male' else choice(cls.femaleNames)
            lastName = choice(cls.lastNames)
            if body.sex() != 'male':
                lastName += 'а'

            color = '#FFFFFF'
            if body.sex() == 'female':
                color = '#FF85F1'
            elif body.sex() == 'male':
                color = '#269AFF'
            elif body.sex() == 'futa':
                color = '#FC3A3A'

            character = cls(firstName, lastName, color = color, age = rand(12, 16), body = body, stats = stats, picto = picto)
            return character

        def normalize(self):
            self.body.normalize()
            self.stats.normalize()

        def fullName(self):
            return self.fname + ' ' + self.lname

###################################################################
#инвентарь
###################################################################
        #Добавление нескольких предметов в инвентарь
        def addItems(self,*args):
            flag = 0
            for x in args:
                for y in allItems:
                    if x == y.name:
                        temp = copy.copy(y)
                        self.inventory.append(temp)
                        flag += 1
            if flag == len(args):
                return True
            else:
                renpy.say('','ITEMS ARE NOT ADDED!')
                return False

        #Добавлние одного предмета (можно использовать и addItems) просто на всякий пожарный.
        def addItem(self,name):
            flag = False
            for x in allItems:
                if name == x.name:
                    temp = copy.copy(x)
                    self.inventory.append(temp)
                    flag = True
            return flag

        # Удаление айтемов
        def removeItem(self,item):
            if self.inventory.count(item) > 0:
                self.inventory.remove(item)
            if self.wear.count(item) > 0:
                self.wear.remove(item)


        # Удаление айтемов !!! Сносит ВСЕ с данным названием!!!
        def removeItems(self,*args):
            flag = 0
            for x in args:
                for y in self.inventory:
                    if x == y.name:
                        self.inventory.remove(y)
                        flag += 1
            for x in args:
                for y in self.wear:
                    if x == y.name:
                        self.wear.remove(y)
                        flag += 1
            if flag == len(args):
                return True
            else:
                return False

        # Проверка на наличие айтема
        def hasItem(self, name):
            for x in self.inventory:
                if name == x.name:
                    return True
            for x in self.wear:
                if name == x.name:
                    return True
            return False

        # Подсчёт айтемов
        def countItem(self, name):
            counter = 0
            for x in self.inventory:
                if name == x.name:
                    counter += 1
            return counter

        # Применение айтема
        def apply(self, name):
            for x in self.inventory:
                if x.name == name:
                    x.durability -= 1
                    self.checkDur()
                    return

        # Удаление всех использованных айтемов
        def checkDur(self):
            for x in self.inventory:
                if x.durability <= 0:
                    self.inventory.remove(x)
            for x in self.wear:
                if x.durability <= 0:
                    self.wear.remove(x)

        # Функция еды
        def eat(self, food):
            global last_eat
            if food.name == 'Энергетик':
                last_eat -= 2
            else:
                last_eat = ptime
            self.stats.energy += food.energy
            food.durability -= 1
            self.checkDur()

        #Вычисленная красота
        def getBeauty(self):
            return self.stats.beauty - self.stats.dirty*5

        #Есть ли сперма вообще
        def isSperm(self):
            parts = self.body.partsWithSperm()
            for i in parts:
                if i.visibility:
                    return 2
            return 1 if len(parts) > 0 else 0

        #Если ли сперма на чём то из
        def getSperm(self,*args):
            partNames = [x.name for x in self.body.partsWithSperm()]
            for x in args:
                if x in partNames:
                    return True
            return False

        #Возвратить стрингу с перечислением заляпанных частей тела
        def printSperm(self):
            partNames = [x.name for x in self.body.partsWithSperm()]
            return ", ".join(partNames)

        #Заляпать спермой части тела
        def coverSperm(self, *args):
            for x in args:
                if x in self.body.parts:
                    self.body.parts[x].sperm = True

        #Помыться
        def cleanAll(self):
            self.dirty = 0
            for _,x in self.body.parts.iteritems():
                x.sperm = False

        #Очистить часть тела
        def clean(self, *args):
            for x in args:
                if x in self.body.parts:
                    self.body.parts[x].sperm = False

        def buy(self, item, *args):
            if len(args) == 0:
                if self.money >= item.cost:
                    self.money -= item.cost
                    if self.hasItem(item.name) == True:
                        self.getItem(item.name).durability += item.durability
                    else :
                        temp = copy.copy(item)
                        self.inventory.append(temp)
            else :
                 if self.money >= item.cost:
                    self.money -= item.cost
                    temp = copy.copy(item)
                    self.inventory.append(temp)

        # Функция получения предмета по имени
        def getItem(self,name):
            for x in self.inventory:
                if x.name == name:
                    return x
            for x in self.wear:
                if x.name == name:
                    return x

        #Сброс переменных
        def reset(self):
            self.normalize()

        # Увеличение развратности
        def setCorr(self,amount):
            self.stats.corruption += amount

        # Функция одевания
        def wearing(self, cloth):
            if cloth.corr > self.stats.corruption or cloth.sex != self.body.sex():
                return False

            for x in cloth.cover:
                for y in self.wear:
                    for z in y.cover:
                        if x == z:
                            self.wear.remove(y)
                            self.inventory.append(y)
                            break


            # for item in self.wear:
                # for cov in item.cover:
                    # if cloth.cover.count(cov) > 0 or cloth.cover[0] == 'all':
                        # self.wear.remove(item)
                        # self.inventory.append(item)
                        # break

            if rand(1,100) > 90:
                cloth.durability -= 1
            self.inventory.remove(cloth)
            self.wear.append(cloth)
            self.checkDur()

        # Функция частичного раздевания
        def dewearing(self,cloth):
            if self.wear.count(cloth) > 0:
                self.wear.remove(cloth)
                self.inventory.append(cloth)
            else:
                return False

        # Функция полного раздевания
        def undress(self):
            self.inventory.extend(self.wear)
            self.wear = []

        # Возвращение всех прикрытых частей
        def getCover(self):
            temp = []
            for x in self.wear:
                temp.extend(x.cover)
            return temp

        # Проверка на прикрытость
        def isCover(self, *args):
            temp = self.getCover()
            counter = 0
            for iscovered in args:
                for covered in temp:
                    if covered == iscovered:
                        counter += 1
                        break
            if counter == len(args):
                return True
            else :
                return False

        # Проверка на определённый тип одежды
        def getCovPurpose(self, purpose):
            for x in self.wear:
                if x.purpose == purpose:
                    return True
                else:
                    return False

    def getCharByName(name):
        global allChars
        for x in allChars:
            if x.fullName() == name:
                return x
