from math import floor

class Monkey():
    def __init__(self, monkey_number: int, items: list, operation: list, if_true: int, if_false: int, divisible_by: int):
        self.items: list = items
        self.monkey_number = monkey_number
        self.operation = operation
        self.times_inspected: int = 0
        #self.first_operation_item, self.second_operation_item, self.third_operation_item = operation
        self.if_true = int(if_true)
        self.if_false = int(if_false)
        self.divisible_by = divisible_by
            
    def __str__(self):
        return f'''Monkey number: {self.monkey_number},
    Items: {self.items},
    Inspected: {self.times_inspected}'''
# Operation: {self.operation},
# Divisible by: {self.divisible_by},
# If true and if false throw to: {self.if_true} or {self.if_false}.'''
    
    def make_operation(self, item_to_operation: int, modulo: int):
        second_operation_item, third_operation_item = self.operation[1], self.operation[2]
        
        if third_operation_item == 'old':
            third_operation_item: int = item_to_operation
        else:
            third_operation_item = int(third_operation_item)
        
        if second_operation_item == '+':
            new_operation_item: int = item_to_operation + third_operation_item
        elif second_operation_item == '-':
            new_operation_item: int = item_to_operation - third_operation_item
        # elif second_operation_item == '/':
        #     new_operation_item: int = int(item_to_operation) / int(third_operation_item)
        elif second_operation_item == '*':
            new_operation_item: int = item_to_operation * third_operation_item
        
        return new_operation_item % modulo
    
    def divided_by_3(self, item: int):
        # return floor(item / 3)
        # return int(str(item / 3).split('.')[0])
        return item // 3
    
    def test(self, item:int):
        if item % self.divisible_by == 0: return True
        else: return False
    
    def remove_item(self, item: int):
        self.items.remove(item)
        
    def add_item(self, item: int):
        self.items.append(item)
        
    def clear_list(self):
        self.items.clear()
        
    