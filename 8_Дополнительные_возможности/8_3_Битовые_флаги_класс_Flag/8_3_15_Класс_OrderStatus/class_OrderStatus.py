''' Первый вариант решения'''
from enum import Flag


class OrderStatus(Flag):
    ORDER_PLACED = 0b1
    PAYMENT_RECEIVED = 0b1_0
    SHIPPING_COMPLETE = 0b1_00
''' Второй вариант решения'''    
# from enum import Flag, auto


# class OrderStatus(Flag):
#     ORDER_PLACED = auto()
#     PAYMENT_RECEIVED = auto()
#     SHIPPING_COMPLETE = auto()