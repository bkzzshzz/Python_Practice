import json
'''This is a comment'''

house = '''
    {
        "houses": [
            {
            "place" : "Bode",
            "phone" : "987979987879",
            "internet" : "Worldlink",
            "has_basement" : false

        },
        {
            "place" : "Bottteeee",
            "phone" : "9879799erer87879",
            "internet" : "Worldnk",
            "has_basement" : true

        }
        ]
    }
'''

house_data = json.loads(house)
print(house)
print(house_data)
