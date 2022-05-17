# assignment 2 problem 2
class Flower:
    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None 

    def set_flower_name(self,flower_name):
        self.__flower_name = flower_name

    def get_flower_name(self):
        return self.__flower_name

    def set_price_per_kg(self,price_per_kg):
        self.__price_per_kg = price_per_kg

    def get_price_per_kg(self):
        return self.__price_per_kg

    def set_stock_available(self,stock_available):
        self.__stock_available = stock_available

    def get_stock_available(self):
        return self.__stock_available

    def validate_flower(self):
        if self.__flower_name in ("Orchid","Rose","Jasmine"):
            return True
        else:
            return False
    
    def validate_stock(self,required_quantity):
        if self.__stock_available >= required_quantity:
            return True
        else : return False

    def check_level(self):
        if self.__flower_name == "Rose" and self.stock_available >= 15:
            return False
        elif self.__flower_name == "Orchid" and self.stock_available >=25:
            return False
        elif self.__flower_name == "Jasmine" and self.stock_available >= 40:
            return True
        else : 
            return False


    def  sell_flower(self,required_quantity):
        validate_flower = self.validate_flower()
        validate_stock = self.validate_stock(required_quantity)
        print(validate_flower,validate_stock)
        if validate_flower == True and validate_stock == True :
            self.__stock_available = self.__stock_available - required_quantity

rose = Flower()
rose.set_flower_name("jasmine")
rose.set_price_per_kg(200)
rose.set_stock_available(24)
print("stock available :: ",rose.get_stock_available())
rose.sell_flower(5)
print("stock after selling :: ",rose.get_flower_name(),str(rose.get_price_per_kg()),rose.get_stock_available())

print(rose.validate_flower())

# assignment 2 problem 3

#lex_auth_012727085763518464103
#Start writing your code here
class CallDetail:
    def __init__(self,phoneno,called_no,duration,call_type):
        self.__phoneno = phoneno
        self.__called_no = called_no
        self.__duration = duration
        self.__call_type = call_type

class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        pass

call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)