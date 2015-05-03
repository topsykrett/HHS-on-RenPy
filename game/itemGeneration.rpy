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
    sex = 'female')
    jaket.cover = ['chest']
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
    sex = 'female')
    longSkirt.cover = ['leg']
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
    sex = 'female')
    browntights.cover = ['feet']
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
    sex = 'female')
    simpleUnderwear.cover = ['under']
    simpleUnderwear.durability = 20
    simpleUnderwear.name = _('Простое нижнее бельё')
    simpleUnderwear.cost = 300
    simpleUnderwear.picto = 'pic/items/simpleUnderwear.png'
    simpleUnderwear.type = 'clothing'
    clothing.append(simpleUnderwear)
    
    allItems.extend(clothing)
    