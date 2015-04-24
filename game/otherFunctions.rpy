init -5 python:
    import random
    def rand(a, b):
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