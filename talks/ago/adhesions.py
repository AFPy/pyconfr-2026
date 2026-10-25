import csv
import re

def capitalize(s):
    parts = re.split(r'(\W+)', s)
    return ''.join(p.capitalize() for p in parts).strip()

with open('adhesions.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=';')
    #rows = list(reader)
    rows = {
        (capitalize(row['Nom adhérent']), capitalize(row['Prénom adhérent'])): row['Date de la commande'].split()[0]
        for row in reader
    }

print('<html><body><p>')
for (last_name, first_name), date in sorted(rows.items()):
    print(f'<input type="checkbox"/> {first_name} {last_name} <small>({date}), arrivé·e à ………</small> <br/>')
print('</p></body></html>')
