init -5 python:
    import random
    import time
    
    dublicationChar = []
    
    def rand(a, b):
        if a == b:
            return a
        else:
            return random.randint(a,b)
        
    def randf(a, b):
        return random.uniform(a,b)
    
    def getPar(list, *args):
        temp = 0
        
        if args[0] == 'loy':
            for x in list:
                temp = temp + x.loy
            return round(temp/len(studs),2)
        
        if args[0] == 'fun':
            for x in list:
                temp = temp + x.fun
            return round(temp/len(studs),2)
            
        if args[0] == 'corr':
            for x in list:
                temp = temp + x.corr
            return round(temp/len(studs),2)

        if args[0] == 'lust':
            for x in list:
                temp = temp + x.lust
            return round(temp/len(studs),2)
            
        if args[0] == 'edu':
            for x in list:
                temp = temp + x.edu
            return round(temp/len(studs),2)

        if args[0] == 'rep':
            for x in list:
                temp = temp + x.rep
            return round(temp/len(studs),2)
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
        if len(args) == 0:
            return allChars[rand(0,len(allChars)-1)]
            
        if len(args) == 1:
            temp = []
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
            
            
    def skipEvent():
        tryEvent(curloc)