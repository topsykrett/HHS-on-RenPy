init python:
    style.my_text = Style(style.default)
    style.warning = Style(style.default)
    style.description = Style(style.default)
    style.myBox = Style(style.default)
    style.navigation_button = Style(style.button_text)
    # style.navigation_button.background = Frame("pic/bg.png", 25, 25)
    # style.navigation_button.hover_background = Frame("pic/bg.png", 25, 25)
    # style.navigation_button.selected_background = Frame("images/interface/music_library_button_selected.png", 25, 25)
    style.navigation_button_text.color = "#FFFFFF"
    style.navigation_button_text.outlines = [(1, "#000000", 0, 0)]
    style.navigation_button_text.hover_color = "#0000FF"
    style.navigation_button_text.selected_color = "#00FF00"
     
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