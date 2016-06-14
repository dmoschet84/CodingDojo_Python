users = {
 'Students': [
     {'number': 1, 'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'number': 2, 'first_name' : 'John', 'last_name' : 'Rosales'},
     {'number': 3, 'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'number': 4, 'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'number': 1, 'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'number': 2, 'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
for keys in users:
        print(keys)
        for value in users[keys]:
            print value["number"],"-",value["first_name"],value["last_name"],"-",len(value["first_name"])+len(value["last_name"])
