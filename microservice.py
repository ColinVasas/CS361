import os
import requests
import json
from random import randint

while True:
    f = open('call-service.txt', 'r+')
    url = "https://api.open5e.com/v1/spells/?dnd_class__icontains=wizard&format=json"
    call = f.readline()
    f.truncate(0)
    f.close
    if call == 'call' :
        spell_data_list = []
        spells = []
        response = requests.get(url)
        f = open('call-service.txt', 'r+')

        spell = response.json()

        spell_data_list.extend(spell['results'])

        data = json.loads(response.text)
        count = 0
        while(count != 5) :
            randomValue = randint(0,49)
            spells.insert(count,spell_data_list[randomValue]['name'])
            f.write(spells[count]+"\n")
            count = count+1

        f.close()
        break