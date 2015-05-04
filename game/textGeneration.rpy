init python:
    def textgen(char):
        description = ''

        name = char.fullName()
        age = char.age
        sex = char.body.sex()
        loyalty = char.stats.loyalty
        edu = char.stats.education
        lust = char.stats.lust
        corr = char.stats.corruption
        fun = char.stats.fun

        description += 'Перед вами ' + char.fullName() + '\n'
        description += 'Это '

        if char.body.height < 150: description += 'маленького роста '
        elif char.body.height < 175: description += 'среднего роста '
        else :
            if sex == 'male':
                description += 'высокий '
            else :
                description += 'высокая '

        if age > 20:
            if sex == 'male':
                description += 'мужчина'
            elif sex == 'female' or (loyalty < 50 and sex == 'futa'):
                description += 'женщина'
            else:
                description += 'футанари'
        else:
            if sex == 'male':
                description += 'мальчик'
            elif sex == 'female' or (loyalty < 50 and sex == 'futa'):
                description += 'девочка'
            else:
                description += 'футанари'

        description += ' '+ str(age) + ' лет. '
        bsize = char.body.parts['грудь'].size
        if bsize > 0:
            if bsize < 1: description += 'У неё почти нет грудей, что не удивительно для такой молодой девочки. '
            elif bsize < 2: description += 'У неё маленькие, симпатичные титечки. '
            elif bsize < 3: description += 'У неё небольшие, аккуратные груди. '
            elif bsize < 4: description += 'У неё неплохие груди третьего размера. '
            elif bsize < 5: description += 'У неё полные, налитые титьки. '
            elif bsize < 6: description += 'У неё большие, сочные сиськи. '
            elif bsize < 7: description += 'У неё действительно большие сиськи, каждая размером с дыню. Их выпирающие округлости слегка торчат даже со спины. '
            elif bsize < 8: description += 'У неё внушительных размеров большие сиськи, мясистые и налитые, словно перезревшие дыни. Их выпирающие округлости видны даже со спины. '
            elif bsize < 9: description += 'У неё огромные буфера, кажется будто каждая размером с голову девушки. Эти шары видны даже со спины. '
            else : description += 'У неё массивные огромные сисяндры, каждая размером с голову девушки, такие бывают только у порнозвёзд. Эти выпирающие шары видны с любого ракурса. '

        description += '\n'
        if age < 20:
            if sex == 'male':
                description += 'Он '
                if edu < 20: description += 'необразован донельзя. Как будто живёт на улице...'
                elif edu < 50: description += 'посредственно учиться, и его знания оставляют желать лучшего.'
                elif edu < 80: description += 'имеет хорошее представление о всех науках, преподаваемых в школе.'
                else : description += 'отличник, спортсмен, будь женского пола был бы ещё и комсомолкой!'
            else :
                description += 'Она '
                if edu < 20: description += 'необразованна донельзя. Как будто живёт на улице...'
                elif edu < 50: description += 'посредственно учиться, и её знания оставляют желать лучшего.'
                elif edu < 80: description += 'имеет хорошее представление о всех науках, преподаваемых в школе.'
                else : description += 'отличница, спортсменка, лет 40 назад была бы ещё и комсомолкой!'
        else :
            if sex != 'male':
                description += 'Она '
            else :
                description += 'Он '
            if edu < 20: description += 'имеет слабое образование. Настолько слабое, что Вы удивлены, что этот человек работает учителем'
            elif edu < 50: description += 'имеет неплохое образование, но всё же её знания оставляют желать лучшего'
            elif edu < 80: description += 'имеет хорошее представление о своём предмете преподавания'
            else : description += 'имеет прекрасные знания не только о своём предмете, но и в смежных науках'

        description += '\n'
        description += char.fname + ' '
        if loyalty < 20: description += 'совсем не знает Вас.'
        elif loyalty < 50: description += 'не против иногда перекинуться с Вами парой словечек.'
        elif loyalty < 80: description += 'весьма хорошего о Вас мнения.'
        else : description += 'просто обожает вас.'

        if loyalty >= 50 and sex == 'futa': description += ' Девочка недавно призналась, что она не совсем девочка и прячет член под юбкой.'

        description += '\n'

        if sex == 'female':
            if lust < 20: description += ''
            elif lust < 50: description += 'Вы замечаете у неё немного покрасневшие щёчки. '
            elif lust < 80: description += 'Вы замечаете, что она сильно краснеет, когда встречается с Вами взглядом. '
            else : description += 'Вы замечаете, что она сильно краснеет, когда встречается с Вами взглядом. '
        else :
            if lust < 20: description += ''
            elif lust < 50: description += 'Вы замечаете у него немного покрасневшие щёки. '
            elif lust < 80: description += 'Вы замечаете, что он сильно краснеет, когда встречается с Вами взглядом. '
            else : description += 'Вы замечаете, что ученик переминается с ноги на ногу, и Вы замечаете видимый бугорок на его штанах. '

        if corr < 20: description += 'По слухам, ' + char.fname + ' не знает о сексе ничего.'
        elif corr < 50: description += 'По слухам, ' + char.fname + ' мастурбирет и подглядывает за парочками.'
        elif corr < 80: description += 'По слухам, ' + char.fname + ' знает как, и любит заниматься сексом.'
        else : description += 'По слухам, ' + char.fname + ' любит любой секс во всех его проявлениях и извращениях.'

        description += '\n'

        if sex == 'male':
            description += 'Сегодня он '
        else :
            description += 'Сегодня она '

        if fun < 20: description += 'выглядит расстроенно.'
        elif fun < 50: description += 'выглядит довольно весело.'
        elif fun < 80: description += 'радуется погоде и новому дню.'
        else : description += 'веселится, заражая всех своей энергией.'

        description += '\n'

        rep = char.stats.reputation

        if age < 20:
            if sex  == 'male':
                description += 'Не секрет, что его '
            else :
                description += 'Не секрет, что её '
            if rep < 20: description += 'родители просто в ярости от вас.'
            elif rep < 50: description += 'родители не очень высокого о Вас мнения.'
            elif rep < 80: description += 'родители ставят Вас в пример своим детям.'
            else : description += 'родители в восторге от вас.'

        if sex != 'female' and corr > 50:
            description += '\n[name] прозрачно намекает вам, что под одеждой от вас скрывается [char.psize] сантиметровый змий!'

        if sex == 'female':
            description += '\nНа ней сегодня '
        else:
            description += '\nНа нём сегодня '
        if char.wear == []:
            description += 'ничего нет.'
        else:
            description += ', '.join(char.wear)
        return description

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
