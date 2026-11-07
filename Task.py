#Каждый блок проверяла отдельно через ии
#в методе get_telephone_number через ии узнала о isinstanceecho "# Sprint_3" >> README.md 
    
class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self,name):        
        if  0 == len(name) or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items +=1

    def delete_item_from_check(self,name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -=1

    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price[item])    
        if len(self.__name_items) > 10:
            return sum(total) * 0.9
        return sum(total) 
    
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
        for item in twenty_percent_tax:
            total.append(self.__item_price[item])
        sum_total = sum(total)
        if len(self.__name_items) > 10:
            tax = sum_total*0.9*0.2
        else:
            tax = sum_total*0.2
        return tax
    
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
        for item in ten_percent_tax:
            total.append(self.__item_price[item])
        sum_total = sum(total)
        if len(self.__name_items) > 10:
            tax = sum_total*0.9*0.1
        else:
            tax = sum_total*0.1
        return tax
    
    def total_tax(self): 
        total = self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()
        return  total
    
    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести число')       
        if telephone_number < 0 or telephone_number > 9999999999:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        if len(str(telephone_number)) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{telephone_number}' 

