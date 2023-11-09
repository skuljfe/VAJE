import json

with open(r'C:\Users\as4061\Desktop\DN3\DATA\zacetniData', 'r') as original_file:
    zacetniData = json.load(original_file)

with open(r'C:\Users\as4061\Desktop\DN3\DATA\updateData', 'r') as updated_file:
    updateData = json.load(updated_file)

zacetni_slovar = {oseba['name']: oseba for oseba in zacetniData['persons']}

for oseba in updateData['persons']:
    if oseba['name'] in zacetni_slovar:
        zacetni_slovar[oseba['name']].update(oseba)

zacetni_slovar = list(zacetni_slovar.values())

posodobljena_datoteka = {'persons': zacetni_slovar}

with open(r'.\nova', 'w') as izhodna_file:
    json.dump(posodobljena_datoteka, izhodna_file, indent=2)