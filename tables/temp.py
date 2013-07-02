#!/usr/bin/env python

categories = ['Linguistics', 'Lore\:Region\, Own', 'Lore\:*', 'Lore\:*', 'Mathematics',
              'Body Development', 'Running',
              'Unarmed Combat',
              'Animal Handling\:*', 'Riding\:*', 'Survival\: Region\, Own',
              'Navigation\:Terrestrial', 'Perception', 'Tracking',
              'Social Awareness',
              'Stalk/Hide',
              '(Crafting|Composition|Performance Art)\:*','(Crafting|Composition|Performance Art)\:*',
                 'Mechanical\:*', 'Medical\:First Aid', 'Vocation\:*','Vocation\:*']
              
f = open('Cultures.txt','w')
while True:
    name = raw_input('Name: ')
    if name:
        f.write(name)
        bonuses = []
        for cat in categories:
            bonus = raw_input(cat).strip()
            if bonus and int(bonus):
                bonuses.append(cat+'{0:+d}'.format(int(bonus)))
        if bonuses:
            f.write(' {')
            f.write(', '.join(bonuses))
            f.write('}')
        f.write('\n')
    else:
        break

f.close()
