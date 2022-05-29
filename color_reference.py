# Remember, cv2 uses BGR, not RGB..
light_green = (50,205,50) 
ligth_yellow = (0,255, 255)
light_orange = (0, 130, 255)
red = (0, 0, 255)


medium_yellow = (0, 233, 233)
dark_green = (0, 102, 0)
dark_yellow = (0, 200, 215)
dark_orange = (0, 102, 204)

color_table = {
    
     1  : light_green,
     2  : ligth_yellow,
     3  : light_orange,
     4  : red,
    '1S': dark_green,
    # '1M': medium_yellow,
    '1L': dark_green,
    '2S': dark_yellow,
    '2L': dark_yellow,
    '3S': dark_orange,
    '3L': dark_orange,
}

# print(color_table['1S'])