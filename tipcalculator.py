"""
This 'app' will calculate the total price you need to pay in a restaurant, if you would like to give the waiter a tip
"""

food_amount = float(input('Geben Sie bitte den Rechnungsbetrag ein €: '))
tip_percentage = int(input('Geben Sie den Prozentsatz für Ihr Trinkgeld ein %: '))
tip_amount = food_amount / 100 * tip_percentage
total_amount = food_amount + tip_amount
print('\n\n')
'''
# Ausgabe (Möglichkeit 1:
print('Rechnungsbetrag: ' + str(food_amount) + ' €')
print(' + Trinkgeld: ' + str(tip_amount) + ' €')
print('Gesamt: ' + str(food_amount + tip_amount) + ' €')
'''
# Ausgabe Möglichkeit 2:
print('----------------------------------')
print(f'🥘 Essen: € {food_amount}')
print(f'⚖ Trinkgeld: € {tip_amount}')
print('\n')
print(f'💰 Gesamtbetrag: € {total_amount}')
print('----------------------------------')
