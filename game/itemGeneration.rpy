#############################################################
#Создание айтемов
#############################################################
init python:
    clothing = []
    #Cоздание предметов
    
    napkin = Tool(purpose = 'clean')
    napkin.name = _('Салфетка')
    napkin.cost = 100
    napkin.picto = 'pic/items/napkin.jpg'
    napkin.durability = 10
    napkin.type = 'tool'
    
    sandwich = Food( energy = 250 )
    sandwich.name = _('Сэндвич')
    sandwich.cost = 0
    sandwich.picto = 'pic/items/sandwich.jpg'
    sandwich.durability = 1
    sandwich.type = 'food'

    eDrink = Food(energy = 100)
    eDrink.name = _('Энергетик')
    eDrink.cost = 150
    eDrink.picto = 'pic/items/edrink.jpg'
    eDrink.durability = 1
    eDrink.type = 'food'

    rawFood = Food(energy = 400)
    rawFood.name = _('Сырая еда')
    rawFood.cost = 500
    rawFood.picto = 'pic/items/food.jpg'
    rawFood.durability = 10
    rawFood.type = 'hidden'
    
    allItems = [napkin, sandwich, eDrink, rawFood]

    
    # Ваша одежда
    jaket = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'teacher',
    sex = 'female',
    purpose = 'usual')
    jaket.cover = ['верх']
    jaket.durability = 100
    jaket.name = _('Пиджак')
    jaket.cost = 1500
    jaket.picto = 'pic/items/jaket.png'
    jaket.type = 'clothing'
    clothing.append(jaket)
    
    
    longSkirt = Clothing(
    lust = 0,
    corr = 0,
    reputation = 1,
    char = 'teacher',
    sex = 'female',
    purpose = 'usual')
    longSkirt.cover = ['низ']
    longSkirt.durability = 100
    longSkirt.name = _('Длинная юбка')
    longSkirt.cost = 1000
    longSkirt.picto = 'pic/items/longSkirt.png'
    longSkirt.type = 'clothing'
    clothing.append(longSkirt)
    
    browntights = Clothing(
    lust = 5,
    corr = 0,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'usual')
    browntights.cover = ['ноги']
    browntights.durability = 10
    browntights.name = _('Телесные колготки')
    browntights.cost = 150
    browntights.picto = 'pic/items/browntights.png'
    browntights.type = 'clothing'
    clothing.append(browntights)
    
    simpleUnderwear = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'usual')
    simpleUnderwear.cover = ['грудь','попа']
    simpleUnderwear.durability = 20
    simpleUnderwear.name = _('Простое нижнее бельё')
    simpleUnderwear.cost = 300
    simpleUnderwear.picto = 'pic/items/simpleUnderwear.png'
    simpleUnderwear.type = 'clothing'
    clothing.append(simpleUnderwear)

    swimsuit = Clothing(
    lust = 0,
    corr = 0,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'swim')
    swimsuit.cover = ['грудь','попа','верх','низ','ноги']
    swimsuit.durability = 40
    swimsuit.name = _('Купальник')
    swimsuit.cost = 500
    swimsuit.picto = 'pic/items/swimsuit.png'
    swimsuit.type = 'clothing'
    clothing.append(swimsuit)
    
    bikini_top = Clothing(
    lust = 5,
    corr = 30,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'swim')
    bikini_top.cover = ['грудь','верх']
    bikini_top.durability = 20
    bikini_top.name = _('Бикини верх')
    bikini_top.cost = 500
    bikini_top.picto = 'pic/items/bikini_top.png'
    bikini_top.type = 'clothing'
    clothing.append(bikini_top)

    bikini_bottom = Clothing(
    lust = 5,
    corr = 30,
    reputation = 0,
    char = 'teacher',
    sex = 'female',
    purpose = 'swim')
    bikini_bottom.cover = ['попа','низ','ноги']
    bikini_bottom.durability = 20
    bikini_bottom.name = _('Бикини низ')
    bikini_bottom.cost = 500
    bikini_bottom.picto = 'pic/items/bikini_bottom.png'
    bikini_bottom.type = 'clothing'
    clothing.append(bikini_bottom)
    
    allItems.extend(clothing)
    