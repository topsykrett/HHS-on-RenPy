init -5 python:
    import random
    import time
    from operator import attrgetter
    
    dublicationChar = []
    
    def rand(a, b):
        if b == 0:
            return b
        else :
            return random.randint(a,b)
        
    def randf(a, b):
        return random.uniform(a,b)

        
    def getPar(list, *args):
        temp = 0
        if args[0] == 'loy':
            for x in list:
                temp = temp + x.loy
            return round(temp/len(list),2)
        
        if args[0] == 'fun':
            for x in list:
                temp = temp + x.fun
            return round(temp/len(list),2)
            
        if args[0] == 'corr':
            for x in list:
                temp = temp + x.corr
            return round(temp/len(list),2)

        if args[0] == 'lust':
            for x in list:
                temp = temp + x.lust
            return round(temp/len(list),2)
            
        if args[0] == 'edu':
            for x in list:
                temp = temp + x.edu
            return round(temp/len(list),2)

        if args[0] == 'rep':
            for x in list:
                temp = temp + x.rep
            return round(temp/len(list),2)
        return 'error'
        
    def waiting(t):
        player.energy -= randf(t/2,t)
        changetime(t)
        move(curloc)

#Динамическая картинка
    def dynImage(st,at):
        return dynpicto, None

#Работа с людьми
    def getChar(*args):
        global dublicationChar
        temp = []
        
        if len(args) == 0:
            return allChars[rand(0,len(allChars)-1)]
            
        if len(args) == 1:
            if len(getLoc(curloc).people) > 0:
                for char in getLoc(curloc).people:
                    if char.sex == args[0] and teachers.count(char) == 0 and dublicationChar.count(char) == 0:
                        temp.append(char)
                if len(temp) > 0:
                    rands = rand(0,len(temp)-1)
                    dublicationChar.append(temp[rands])
                    if len(dublicationChar) > 10:
                        dublicationChar = []
                    return temp[rands]

            for char in studs:
                if char.sex == args[0] and dublicationChar.count(char) == 0:
                    temp.append(char)
            rands = rand(0,len(temp)-1)
            dublicationChar.append(temp[rands])
            if len(dublicationChar) > 10:
                dublicationChar = []
            return temp[rands]
        
        if len(args) == 2:
            for x in studs:
                if x.sex == args[0] or args[0] == '':
                    temp.append(x)
            tempChar = temp[0]
            if args[1] == 'beautymax':
                for x in temp:
                    if x.beauty > tempChar.beauty:
                        tempChar = x
                return tempChar
            if args[1] == 'beautymin':
                for x in temp:
                    if x.beauty < tempChar.beauty:
                        tempChar = x
                return tempChar
            if args[1] == 'edumax':
                for x in temp:
                    if x.edu > tempChar.edu:
                        tempChar = x
                return tempChar
            if args[1] == 'edumin':
                for x in temp:
                    if x.edu < tempChar.edu:
                        tempChar = x
                return tempChar
            if args[1] == 'corrmax':
                for x in temp:
                    if x.corr > tempChar.corr:
                        tempChar = x
                return tempChar
            if args[1] == 'corrmin':
                for x in temp:
                    if x.corr < tempChar.corr:
                        tempChar = x
                return tempChar
            if args[1] == 'lustmax':
                for x in temp:
                    if x.lust > tempChar.lust:
                        tempChar = x
                return tempChar
            if args[1] == 'lustmin':
                for x in temp:
                    if x.lust < tempChar.lust:
                        tempChar = x
                return tempChar
                
                
                
    def skipEvent():
        tryEvent(curloc)
        