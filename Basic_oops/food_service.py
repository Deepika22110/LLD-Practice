class User:
    def __init__(self, user_id):
        self.__user_id = user_id
        self.__orders = []
    def get_user(self):
        return self.__user_id
    def add_order(self, order):
        self.__orders.append(order)

    def get_orders(self):
        return self.__orders



class FoodItem:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
    def get_item(self):
        return self.__name
    def get_price(self):
        return self.__price
    def get_quantity(self):
        return self.__quantity   
    
        
        

class Order:
    def __init__(self, order_id, food_items):
        self.__order_id = order_id
        self.__food_items = food_items
    
    
    def get_total_cost(self):
        total = 0
        for item in self.__food_items:
            total += item.get_price() * item.get_quantity()
        return total
            


class OrderService:
    def __init__(self):
        self.__next_order_id = 0
        self.__menu = {
                   "idli": 25,
                   "vada": 35,
                   "dosa": 55
                }
    def create_order(self, user, items):
        food_objects = []
        for name, quantity in items:
            if name in self.__menu:
                price = self.__menu[name]
                food_objects.append(FoodItem(name, price, quantity))
            else:
                print(f"{name} not on menu")
        order = Order(self.__next_order_id, food_objects)
        user.add_order(order)
        self.__next_order_id += 1
        return order
user1 = User("Tarak_123")
service = OrderService()

order1 = service.create_order(user1, [("dosa", 2), ("idli", 3)])
print("Order ID:", order1._Order__order_id)  
print("Total cost:", order1.get_total_cost())  
print("User order count:", len(user1.get_orders())) 

order2 = service.create_order(user1, [("vada", 1)])
print("Order ID:", order2._Order__order_id)  
print("User order count:", len(user1.get_orders()))  


