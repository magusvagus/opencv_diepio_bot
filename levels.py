# this file has all the coordinates and color data of the leveling UI
# NOTE: the current coordinates and RGB values in this file are just placeholders until being updated.

def skillsTree(image):

    #main dictionary
    skills = {
        # skill bar name
            'health_regen' : {
                'level1' : {
                    'level':1,
                    'coordinates':image[45,886],
                    'color':(22,22,22),
                },
                'level2' : {
                    'level':2,
                    'coordinates':image[70,886],
                    'color':(22,22,22),
                },
                'level3' : {
                    'level':3,
                    'coordinates':image[94,886],
                    'color':(33,33,33),
                },
                'level4' : {
                    'level':4,
                    'coordinates':image[117,886],
                    'color':(44,44,44),
                },
                'level5' : {
                    'level':5,
                    'coordinates':image[132,886],
                    'color':(55,55,55),
                },
                'level6' : { 
                    'level':6,
                    'coordinates':image[164,886],
                    'color':(66,66,66),
                },
                'level7' : { 
                    'level':7,
                    'coordinates':image[186,886],
                    'color':(77,77,77),
                },
            },
            'max_health' : {
                'level1' : {
                    'level':1,
                    'coordinates':image[46,910],
                    'color':(11,11,11),
                },
                'level2' : {
                    'level':2,
                    'coordinates':image[70,910],
                    'color':(22,22,22),
                },
                'level3' : {
                    'level':3,
                    'coordinates':image[94,910],
                    'color':(33,33,33),
                },
                'level4' : {
                    'level':4,
                    'coordinates':image[117,910],
                    'color':(44,44,44),
                },
                'level5' : {
                    'level':5,
                    'coordinates':image[132,910],
                    'color':(55,55,55),
                },
                'level6' : { 
                    'level':6,
                    'coordinates':image[164,910],
                    'color':(66,66,66),
                },
                'level7' : { 
                    'level':7,
                    'coordinates':image[186,910],
                    'color':(77,77,77),
                },
            },
            'body_damage' : {
                'level1' : {
                    'level':1,
                    'coordinates':image[46,932],
                    'color':(11,11,11),
                },
                'level2' : {
                    'level':2,
                    'coordinates':image[70,932],
                    'color':(22,22,22),
                },
                'level3' : {
                    'level':3,
                    'coordinates':image[94,932],
                    'color':(33,33,33),
                },
                'level4' : {
                    'level':4,
                    'coordinates':image[117,932],
                    'color':(44,44,44),
                },
                'level5' : {
                    'level':5,
                    'coordinates':image[132,932],
                    'color':(55,55,55),
                },
                'level6' : { 
                    'level':6,
                    'coordinates':image[164,932],
                    'color':(66,66,66),
                },
                'level7' : { 
                    'level':7,
                    'coordinates':image[186,932],
                    'color':(77,77,77),
                },
            },
            # NOTE: coordinates needed
            'bullet_speed' : {
                'level1' : {
                    'level':1,
                    'coordinates':image[10,10],
                    'color':(11,11,11),
                },
                'level2' : {
                    'level':2,
                    'coordinates':image[10,10],
                    'color':(22,22,22),
                },
                'level3' : {
                    'level':3,
                    'coordinates':image[10,10],
                    'color':(33,33,33),
                },
                'level4' : {
                    'level':4,
                    'coordinates':image[10,10],
                    'color':(44,44,44),
                },
                'level5' : {
                    'level':5,
                    'coordinates':image[10,10],
                    'color':(55,55,55),
                },
                'level6' : { 
                    'level':6,
                    'coordinates':image[10,10],
                    'color':(66,66,66),
                },
                'level7' : { 
                    'level':7,
                    'coordinates':image[10,10],
                    'color':(77,77,77),
                },
            },
            'bullet_penetration' : {
                'level1' : {
                    'level':1,
                    'coordinates':image[46,978],
                    'color':(11,11,11),
                },
                'level2' : {
                    'level':2,
                    'coordinates':image[73,978],
                    'color':(22,22,22),
                },
                'level3' : {
                    'level':3,
                    'coordinates':image[95,978],
                    'color':(33,33,33),
                },
                'level4' : {
                    'level':4,
                    'coordinates':image[118,979],
                    'color':(44,44,44),
                },
                'level5' : {
                    'level':5,
                    'coordinates':image[140,979],
                    'color':(55,55,55),
                },
                'level6' : { 
                    'level':6,
                    'coordinates':image[165,979],
                    'color':(66,66,66),
                },
                'level7' : { 
                    'level':7,
                    'coordinates':image[186,979],
                    'color':(77,77,77),
                },
            },
            'bullet_damage' : {
                'level1' : {
                    'level':1,
                    'coordinates':image[45,996],
                    'color':(11,11,11),
                },
                'level2' : {
                    'level':2,
                    'coordinates':image[71,1002],
                    'color':(22,22,22),
                },
                'level3' : {
                    'level':3,
                    'coordinates':image[94,1001],
                    'color':(33,33,33),
                },
                'level4' : {
                    'level':4,
                    'coordinates':image[114,1001],
                    'color':(44,44,44),
                },
                'level5' : {
                    'level':5,
                    'coordinates':image[141,1001],
                    'color':(55,55,55),
                },
                'level6' : { 
                    'level':6,
                    'coordinates':image[165,1001],
                    'color':(66,66,66),
                },
                'level7' : { 
                    'level':7,
                    'coordinates':image[188,1002],
                    'color':(77,77,77),
                },
            },
            'relaod' : {
                'level1' : {
                    'level':1,
                    'coordinates':image[44,1025],
                    'color':(11,11,11),
                },
                'level2' : {
                    'level':2,
                    'coordinates':image[70,1025],
                    'color':(22,22,22),
                },
                'level3' : {
                    'level':3,
                    'coordinates':image[94,1025],
                    'color':(33,33,33),
                },
                'level4' : {
                    'level':4,
                    'coordinates':image[117,1025],
                    'color':(44,44,44),
                },
                'level5' : {
                    'level':5,
                    'coordinates':image[141,1025],
                    'color':(55,55,55),
                },
                'level6' : { 
                    'level':6,
                    'coordinates':image[163,1025],
                    'color':(66,66,66),
                },
                'level7' : { 
                    'level':7,
                    'coordinates':image[189,1025],
                    'color':(77,77,77),
                },
            },
            'movement_speed' : {
                'level1' : {
                    'level':1,
                    'coordinates':image[44,1048],
                    'color':(11,11,11),
                },
                'level2' : {
                    'level':2,
                    'coordinates':image[70,1048],
                    'color':(22,22,22),
                },
                'level3' : {
                    'level':3,
                    'coordinates':image[94,1048],
                    'color':(33,33,33),
                },
                'level4' : {
                    'level':4,
                    'coordinates':image[117,1048],
                    'color':(44,44,44),
                },
                'level5' : {
                    'level':5,
                    'coordinates':image[137,1048],
                    'color':(55,55,55),
                },
                'level6' : { 
                    'level':6,
                    'coordinates':image[163,1048],
                    'color':(66,66,66),
                },
                'level7' : { 
                    'level':7,
                    'coordinates':image[189,1048],
                    'color':(77,77,77),
                },
            },
        }

    return skills
