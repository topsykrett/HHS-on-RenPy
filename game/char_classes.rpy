init -20 python:
    import copy
    class Char:
        def __init__(self,fname,lname,age,sex,bsize,psize,vsize,asize,height,color,loy,fun,inventory,wear,corr,lust,will,edu,club,picto,energy,health,intel,location,body,money,beauty,rep,dirty):
            self.fname = fname
            self.lname = lname
            self.age = age
            self.name = fname + ' ' + lname
            self.sex = sex
            self.bsize = bsize
            self.psize = psize
            self.vsize = vsize
            self.asize = asize
            self.height = height
            self.color = color
            self.loy = loy
            self.fun = fun
            self.inventory = inventory
            self.wear = wear
            self.corr = corr
            self.lust = lust
            self.will = will
            self.edu = edu
            self.club = club
            self.picto = picto
            self.energy = energy
            self.health = health
            self.intel = intel
            self.location = location
            self.body = body
            self.money = money
            self.beauty = beauty
            self.dirty = dirty
            self.rep = rep
            self.say = Character (self.name, kind=adv, dynamic = False, color = self.color, show_side_image = Image(self.picto, xalign=0.0, yalign=1.0), window_left_padding = 170)
            config.side_image_tag = self.picto

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

        def removeItem(self,*args):
            flag = 0
            for x in args:
                for y in self.inventory:
                    if x == y.name:
                        self.inventory.remove(y)
                        flag += 1
            if flag == len(args):
                return True
            else:
                return False
                
        def removeItems(self,*args):
            flag = 0
            for x in args:
                for y in self.inventory:
                    if x == y.name:
                        self.inventory.remove(y)
                        flag += 1
            if flag == len(args):
                return True
            else:
                return False
                
        def hasItem(self, name):
            for x in self.inventory:
                if name == x.name:
                    return True
            return False
            
        def countItem(self, name):
            counter = 0
            for x in self.inventory:
                if name == x.name:
                    counter += 1
            return counter
            
        def apply(self, name):
            for x in self.inventory:
                if x.name == name:
                    x.durability -= 1
                    self.checkDur()
                    return
                
        def checkDur(self):
            for x in self.inventory:
                if x.durability <= 0:
                    self.inventory.remove(x)
                    
        def eat(self, food):
            global last_eat
            if food.name == 'Энергетик':
                last_eat -= 2
            else:
                last_eat = ptime
            self.energy += food.energy
            food.durability -= 1
            self.checkDur()
                    
#Вычисленная красота
        def getBeauty(self):
            return self.beauty - self.dirty*5

#Есть ли сперма вообще
        def isSperm(self):
            for x in self.body:
                if x.sperm == True:
                    if x.visibility == 1:
                        return 2
                    else:
                        return 1
            return 0
            
#Если ли сперма на чём то из
        def getSperm(self,*args):
            flag = 0
            for x in args:
                for y in self.body:
                    if x == y.name and y.sperm == True:
                        flag = 1
            return flag

#Возвратить стрингу с перечислением заляпанных частей тела
        def printSperm(self):
            temp = ''
            counter = 0
            for x in self.body:
                if x.sperm == True:
                    if counter == 0:
                        temp = x.name
                        counter = 1
                    else:
                        temp = temp + ', ' + x.name
            return temp
            
#Заляпать спермой части тела
        def coverSperm(self, *args):
            for x in args:
                for y in self.body:
                    if x == y.name:
                        y.sperm = True
#Помыться
        def cleanAll(self):
            self.dirty = 0
            for x in self.body:
                x.sperm = False
                
#Очистить часть тела
        def clean(self, *args):
            for x in args:
                for y in self.body:
                    if x == y.name:
                        y.sperm = False

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
        
        def getItem(self,name):
            for x in self.inventory:
                if x.name == name:
                    return x

#Сброс переменных
        def reset(self):
            self.bsize = min(max(self.bsize,0),10)
            self.psize = min(max(self.psize,0),30)
            self.vsize = min(max(self.vsize,0),25)
            self.asize = min(max(self.asize,0),25)
            self.loy = min(max(self.loy,0),100)
            self.fun = min(max(self.fun,0),100)
            self.corr = min(max(self.corr,0),100)
            self.lust = min(max(self.lust,0),100)
            self.will = min(max(self.will,0),100)
            self.edu = min(max(self.edu,0),150)
            self.health = min(max(self.health,0),2000)
            self.energy = min(max(self.energy,0),self.health)
            self.intel = min(max(self.intel,0),100)
            self.beauty = min(max(self.beauty,0),200)
            self.dirty = min(max(self.dirty,0),30)
            self.rep = min(max(self.rep,0),100)
        
        def setCorr(self,amount):
            self.corr += amount

###################################################################
#Класс частей тела
###################################################################
    class BodyPart():
        def __init__(self, name, visibility, sperm):
            self.name = name
            self.visibility = visibility
            self.sperm = sperm
        
    def genBody():
        leg = BodyPart('ноги', True, False)
        face = BodyPart('лицо', True, False)
        chest = BodyPart('грудь', True, False)
        vagina = BodyPart('вагина', False, False)
        anus = BodyPart('анус', False, False)
        mouth = BodyPart('рот', False, False)
        hands = BodyPart('руки', True, False)
        body = [face,hands,chest,leg,mouth,vagina,anus]
        return body
        
    def getCharByName(name):
        global allChars
        for x in allChars:
            if x.name == name:
                return x
                
                
                