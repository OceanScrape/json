import json
person_list = []
with open('jason_fake.json') as json_file:
    data = json.load(json_file)
    for item in data:
        name = item['name']
        username = item['username']
        email = item['email']

        person = {
            'Name': name,
            'Username': username,
            'Email': email
        }

        person_list.append(person)

    print(person_list)