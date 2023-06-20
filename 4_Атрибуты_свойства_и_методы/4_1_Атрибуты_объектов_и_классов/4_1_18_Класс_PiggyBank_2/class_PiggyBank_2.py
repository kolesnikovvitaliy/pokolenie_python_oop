''' Первый вариант решения'''
class PiggyBank:
    pass


money_box1 = PiggyBank()
money_box2 = PiggyBank()

money_box1.coins = 10
money_box2.coins = 15
money_box2.color = 'pink'

''' Второй вариант решения'''    
# class PiggyBank:...


# money_box1, money_box2 = PiggyBank(), PiggyBank()

# money_box1.coins = 10
# money_box2.__dict__.update({"color": "pink", "coins": 15})