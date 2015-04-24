init python:
     style.my_text = Style(style.default)
     style.warning = Style(style.default)
     style.description = Style(style.default)
     style.myBox = Style(style.default)
     
style my_text is text:
    size 15
    outlines [(1, "#000000", 0, 0)]
    
style warning is text:
    size 15
    outlines [(1, "#000000", 0, 0)]
    color "#FF1E1E"
    
style description is text:
    outlines [(2, "#000000", 0, 0)]

style statButton is button:
    size 15
    
style myBox is box:
    spacing 5