def negative(value = 0):
    def neg(num):
        return -1 * num, 1
    return neg

def reverse(value = 0 ):
    def reverse_2(num):
        neg = -1 if num < 0 else 1
        num_rev = str(abs(num))[::-1]
        return int(num_rev) * neg, 1
    return reverse_2

def mirror(value  = 0):
    def mirror_2(num):
        num_rev = str(abs(num))[::-1]
        return int(str(num) + str(num_rev)), 1
    return mirror_2

def sum(value = 0):
    def sum_2(num):
        total = 0
        numbers = list(str(num).replace("-", ""))
        for i in range(0, len(numbers)):
            total = total + int(numbers[i])
        return total, 1
    return sum_2

def inverse(value = 0):
    def inv(num):
        neg = -1 if num < 0 else 1
        numbers = list(str(num).replace("-", ""))
        final = ""
        for i in range(0, len(numbers)):
            final = final + str( 10 - int(numbers[i]) % 10 )
        return int(final) * neg, 1
    return inv

def convert (value):
    def conv(num):
        return int( str(num).replace(str(value[0]), str(value[1]))), 1
    return conv

def shiftleft (value = 0):
    def shift(num):
        return int(str(num)[1:] + str(num)[:1] ), 1
    return shift

def shiftright (value = 0):
    def shift(num):
        return int(str(num)[-1:] + str(num)[:-1] ), 1
    return shift

def times(value):
    def timesnum(num):
        return value * num, 1
    return timesnum

def divide(value):
    def dividenum(num):
        if(num == (num / value) * value):
            return num / value, 1
        else:
            return -999999999999, 999
    return dividenum

def plus(value):
    def plusnum(num):
        return value + num, 1
    return plusnum

def backspace(value = 0):
    def backspace_2(num):
        if(len(str(num))) == 1 or ( len(str(num)) == 2 and num < 0  ):
            return 0, 1
        return int(str(num)[:-1]), 1
    return backspace_2

def append(value):
    def appendnum(num):
        return int(str(num) + str(value)), 1
    return appendnum


def get_ops(numbers, operations):
    result = []
    for i in range(0, len(numbers)):
        result.append(operations[i](numbers[i])), 1

    return result

def allAdd(value):
    def allAdd_2(num):
        return num, 1
    return allAdd_2

def allAdd_side_effects(value, nums, flags):
    result = []
    for i in range(0, len(nums)):
        if(flags[i] != 1):
            result.append(nums[i] + value)
        else:
            result.append(nums[i])
    return result

def store(value = 0):
    def store_func(num):
        return num, 0
    return store_func

def use_store(value = 0):
    def use_store_func(num, store):
        return int(str(num) + str(store)), 1
    return use_store_func



class Tree(object):
    def __init__(self):
        self.children = []
        self.nums = []
        self.ops = []
        self.value = None
        self.store = None
        self.just_stored = False
        self.step = None
        self.parent = None

root = Tree()
root.step = 0

ALL_ADD_FLAG = 1
STORE_FLAG = 2
USE_STORE_FLAG = 3


ops_high = [plus, store, use_store, negative]
flags = [0, STORE_FLAG, USE_STORE_FLAG , 0]
root.nums = [-8,0,0,0]
root.ops = get_ops(root.nums, ops_high)
root.value = 12
moves = 5
end_value = 115


def calculate_children(node):
    for i in range(0, len(node.ops)):
        print node.ops[i]

        nums = node.nums
        node.children.append(Tree())
        node.children[i].parent = node
        if(flags[i] == STORE_FLAG):
            if(node.just_stored):
                node.children[i].step  =  9999 # we never want to store twice in a row
            node.children[i].store = node.value
            node.children[i].just_stored = True
        if(flags[i] == USE_STORE_FLAG):
            if(node.store is None):
                continue
            node.children[i].value, num_operations = node.ops[i](node.value, node.store)
        else:
            node.children[i].value, num_operations = node.ops[i](node.value)

        if(flags[i] == ALL_ADD_FLAG):
            node.children[i].nums = allAdd_side_effects(node.nums[i], node.nums, flags)
        else:
            node.children[i].nums = node.nums

        node.children[i].ops = get_ops(node.children[i].nums, ops_high)
        if(node.children[i].value == end_value):
            print("start")
            print_values(node.children[i])
            print("end")
        node.children[i].step = node.step + num_operations
        print(node.children[i].step)
        if(node.children[i].step < moves and node.children[i].value % 1.0 == 0):
            node.children[i].children = calculate_children(node.children[i])

def print_values(node):
    print node.value
    if(node.parent is not None):
        print node.parent.nums
        print_values(node.parent)



calculate_children(root)
