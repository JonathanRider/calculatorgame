def reverse(value = 0 ):
    def reverse_2(num):
        neg = num < 0
        num_rev = str(abs(num))[::-1]
        if(neg):
            return int(num_rev) * -1
        else:
            return int(num_rev)
    return reverse_2

def mirror(value  = 0):
    def mirror_2(num):
        num_rev = str(abs(num))[::-1]
        return int(str(num) + str(num_rev))
    return mirror_2

def times(value):
    def timesnum(num):
        return value * num
    return timesnum

def divide(value):
    def dividenum(num):
        if(num == (num / value) * value):
            return num / value
        else:
            return -999999999999
    return dividenum

def plus(value):
    def plusnum(num):
        return value + num
    return plusnum

def backspace(value = 0):
    def backspace_2(num):
        if(len(str(num))) == 1 or ( len(str(num)) == 2 and num < 0  ):
            return 0
        return int(str(num)[:-1])
    return backspace_2

def append(value):
    def appendnum(num):
        return int(str(num) + str(value))


def get_ops(numbers, operations):
    result = []
    for i in range(0, len(numbers)):
        result.append(operations[i](numbers[i]))

    return result

def allAdd(value):
    def allAdd_2(num):

        return num
    return allAdd_2

def allAdd_side_effects(value, nums, flags):
    result = []
    for i in range(0, len(nums)):
        if(flags[i] != 1):
            result.append(nums[i] + value)
        else:
            result.append(nums[i])
    return result





class Tree(object):
    def __init__(self):
        self.children = []
        self.nums = []
        self.ops = []
        self.value = None
        self.step = None
        self.parent = None




root = Tree()
root.step = 0

ops_high = [plus, plus, times, allAdd]
flags = [0, 0, 0, 1]
root.value = 5
root.nums = [4,8,3,2]
root.ops = get_ops(root.nums, ops_high)
moves = 4
end_value = 41




def calculate_children(node):
    for i in range(0, len(node.ops)):

        nums = node.nums
        node.children.append(Tree())
        node.children[i].parent = node
        node.children[i].value = node.ops[i](node.value)
        if(flags[i] == 1):
            node.children[i].nums = allAdd_side_effects(node.nums[i], node.nums, flags)
        else:
            node.children[i].nums = node.nums
        node.children[i].ops = get_ops(node.children[i].nums, ops_high)
        if(node.children[i].value == end_value):
            print("start")
            print_values(node.children[i])
            print("end")
        node.children[i].step = node.step + 1
        if(node.children[i].step < moves and node.children[i].value % 1.0 == 0):
            node.children[i].children = calculate_children(node.children[i])

def print_values(node):
    print node.value
    if(node.parent is not None):
        print node.parent.nums
        print_values(node.parent)



calculate_children(root)
