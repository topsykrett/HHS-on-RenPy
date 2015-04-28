#############################################################
#Создание айтемов
#############################################################
init python:
    #Cоздание предметов
    
    napkin = Tool(purpose = 'clean')
    napkin.name = 'Салфетка'
    napkin.cost = 100
    napkin.picto = 'pic/noimage.gif'
    napkin.durability = 10
    napkin.type = 'tool'
    
    
    
    
    allItems = [napkin]