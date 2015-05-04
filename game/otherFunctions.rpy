init -5 python:
    import random
    from random import choice
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
                temp = temp + x.stats.loyalty
            return round(temp/len(list),2)

        if args[0] == 'fun':
            for x in list:
                temp = temp + x.stats.fun
            return round(temp/len(list),2)

        if args[0] == 'corr':
            for x in list:
                temp = temp + x.stats.corruption
            return round(temp/len(list),2)

        if args[0] == 'lust':
            for x in list:
                temp = temp + x.stats.lust
            return round(temp/len(list),2)

        if args[0] == 'edu':
            for x in list:
                temp = temp + x.stats.education
            return round(temp/len(list),2)

        if args[0] == 'rep':
            for x in list:
                temp = temp + x.stats.reputation
            return round(temp/len(list),2)
        return 'error'

    def waiting(t):
        player.stats.energy -= randf(t/2,t)
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
            return choice(allChars)

        if len(args) == 1:
            if len(getLoc(curloc).people) > 0:
                for char in getLoc(curloc).people:
                    if char.body.sex() == args[0] and teachers.count(char) == 0 and dublicationChar.count(char) == 0:
                        temp.append(char)
                if len(temp) > 0:
                    choosen = choice(temp)
                    dublicationChar.append(choosen)
                    if len(dublicationChar) > 10:
                        dublicationChar = []
                    return choosen

            for char in studs:
                if char.body.sex() == args[0] and dublicationChar.count(char) == 0:
                    temp.append(char)

            choosen = choice(temp)
            dublicationChar.append(choosen)
            if len(dublicationChar) > 10:
                dublicationChar = []
            return choosen

        if len(args) == 2:
            for x in studs:
                if x.body.sex() == args[0] or args[0] == '':
                    temp.append(x)
            tempChar = temp[0]
            if args[1] == 'beautymax':
                return max(temp, key = lambda x: temp.stats.beauty)
            if args[1] == 'beautymin':
                return min(temp, key = lambda x: temp.stats.beauty)
            if args[1] == 'edumax':
                return max(temp, key = lambda x: temp.stats.education)
            if args[1] == 'edumin':
                return min(temp, key = lambda x: temp.stats.education)
            if args[1] == 'corrmax':
                return max(temp, key = lambda x: temp.stats.corruption)
            if args[1] == 'corrmin':
                return min(temp, key = lambda x: temp.stats.corruption)
            if args[1] == 'lustmax':
                return max(temp, key = lambda x: temp.stats.lust)
            if args[1] == 'lustmin':
                return min(temp, key = lambda x: temp.stats.lust)

    def clrscr():
        renpy.scene(layer='screens')

    def skipEvent():
        tryEvent(curloc)
