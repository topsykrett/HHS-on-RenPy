init python:
    def textgen(char):
        description = ''
        
        description += 'Перед вами ' + char.name + '\n'
        description += 'Это '
        
        if char.height < 150: description += 'маленького роста '    
        elif char.height < 175: description += 'среднего роста '  
        else : 
            if char.sex == 'male':
                description += 'высокий '
            else :
                description += 'высокая'
        
        if char.age > 20:
            if char.sex == 'male': description += 'мужчина'
            elif char.sex == 'female' or (char.loy < 50 and char.sex == 'futa'): description += 'женщина'
            else : description += 'футанари'
        else :
            if char.sex == 'male': description += 'мальчик'
            elif char.sex == 'female' or (char.loy < 50 and char.sex == 'futa'): description += 'девочка'
            else : description += 'футанари'
 
        description += ' '+ str(char.age) + ' лет. '
        if char.bsize > 0: 
            if char.bsize < 1: description += 'У неё почти нет грудей, что не удивительно для такой молодой девочки. '
            elif char.bsize < 2: description += 'У неё маленькие, симпатичные титечки. '
            elif char.bsize < 3: description += 'У неё небольшие, аккуратные груди. '
            elif char.bsize < 4: description += 'У неё неплохие груди третьего размера. '
            elif char.bsize < 5: description += 'У неё полные, налитые титьки. '
            elif char.bsize < 6: description += 'У неё большие, сочные сиськи. '
            elif char.bsize < 7: description += 'У неё действительно большие сиськи, каждая размером с дыню. Их выпирающие округлости слегка торчат даже со спины. '
            elif char.bsize < 8: description += 'У неё внушительных размеров большие сиськи, мясистые и налитые, словно перезревшие дыни. Их выпирающие округлости видны даже со спины. '
            elif char.bsize < 9: description += 'У неё огромные буфера, кажется будто каждая размером с голову девушки. Эти шары видны даже со спины. '
            else : description += 'У неё массивные огромные сисяндры, каждая размером с голову девушки, такие бывают только у порнозвёзд. Эти выпирающие шары видны с любого ракурса. '
        
        description += '\n'
        if char.age < 20:
            if char.sex == 'male':
                description += 'Он '
                if char.edu < 20: description += 'необразован донельзя. Как будто живёт на улице...'
                elif char.edu < 50: description += 'посредственно учиться, и его знания оставляют желать лучшего.'
                elif char.edu < 80: description += 'имеет хорошее представление о всех науках, преподаваемых в школе.'
                else : description += 'отличник, спортсмен, будь женского пола был бы ещё и комсомолкой!'
            else :
                description += 'Она '
                if char.edu < 20: description += 'необразованна донельзя. Как будто живёт на улице...'
                elif char.edu < 50: description += 'посредственно учиться, и её знания оставляют желать лучшего.'
                elif char.edu < 80: description += 'имеет хорошее представление о всех науках, преподаваемых в школе.'
                else : description += 'отличница, спортсменка, лет 40 назад была бы ещё и комсомолкой!'
        else :
            if char.sex != 'male':
                description += 'Она '
            else :
                description += 'Он '
            if char.edu < 20: description += 'имеет слабое образование. Настолько слабое, что Вы удивлены, что этот человек работает учителем'
            elif char.edu < 50: description += 'имеет неплохое образование, но всё же её знания оставляют желать лучшего'
            elif char.edu < 80: description += 'имеет хорошее представление о своём предмете преподавания'
            else : description += 'имеет прекрасные знания не только о своём предмете, но и в смежных науках'
            
        description += '\n'
        description += char.fname + ' '
        if char.loy < 20: description += 'совсем не знает Вас.'
        elif char.loy < 50: description += 'не против иногда перекинуться с Вами парой словечек.'
        elif char.loy < 80: description += 'весьма хорошего о Вас мнения.'
        else : description += 'просто обожает вас.'
        
        if char.loy >= 50 and char.sex == 'futa': description += ' Девочка недавно призналась, что она не совсем девочка и прячет член под юбкой.'
        
        description += '\n'
        
        if char.sex == 'female':
            if char.lust < 20: description += ''
            elif char.lust < 50: description += 'Вы замечаете у неё немного покрасневшие щёчки. '
            elif char.lust < 80: description += 'Вы замечаете, что она сильно краснеет, когда встречается с Вами взглядом. '
            else : description += 'Вы замечаете, что она сильно краснеет, когда встречается с Вами взглядом. '
        else :
            if char.lust < 20: description += ''
            elif char.lust < 50: description += 'Вы замечаете у него немного покрасневшие щёки. '
            elif char.lust < 80: description += 'Вы замечаете, что он сильно краснеет, когда встречается с Вами взглядом. '
            else : description += 'Вы замечаете, что ученик переминается с ноги на ногу, и Вы замечаете видимый бугорок на его штанах. '
            
        if char.corr < 20: description += 'По слухам, ' + char.fname + ' не знает о сексе ничего.'
        elif char.corr < 50: description += 'По слухам, ' + char.fname + ' мастурбирет и подглядывает за парочками.'
        elif char.corr < 80: description += 'По слухам, ' + char.fname + ' знает как, и любит заниматься сексом.'
        else : description += 'По слухам, ' + char.fname + ' любит любой секс во всех его проявлениях и извращениях.'
        
        description += '\n'
        
        if char.sex == 'male': 
            description += 'Сегодня он '
        else :
            description += 'Сегодня она '
            
        if char.fun < 20: description += 'выглядит расстроенно.'
        elif char.fun < 50: description += 'выглядит довольно весело.'
        elif char.fun < 80: description += 'радуется погоде и новому дню.'
        else : description += 'веселится, заражая всех своей энергией.'
        
        description += '\n'
        if char.age < 20:
            if char.sex  == 'male':
                description += 'Не секрет, что его '
            else :
                description += 'Не секрет, что её '
            if char.rep < 20: description += 'родители просто в ярости от вас.'
            elif char.rep < 50: description += 'родители не очень высокого о Вас мнения.'
            elif char.rep < 80: description += 'родители ставят Вас в пример своим детям.'
            else : description += 'родители в восторге от вас.'
        
        
        return description
        
# self.psize = psize
# self.vsize = vsize
# self.asize = asize
# self.inventory = inventory
# self.wear = wear
# self.will = will
# self.club = club
# self.energy = energy
# self.health = health
# self.intel = intel
# self.body = body
# self.beauty = beauty
# self.dirty = dirty
# self.rep = rep