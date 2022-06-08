# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/6/6 9:57
# 分隔工具：print( '*' * 5, '', '*' * 5 )

class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# 变量的赋值
# 只是形成两个变量，实际上还是指向同一个对象
print( '*' * 5, '变量的赋值', '*' * 5 )
cpu1 = CPU()
cpu2 = cpu1

print( cpu1 )
print( cpu2 )

# 浅拷贝
# Python拷贝一般都是浅拷贝，拷贝时，只拷贝源对象，源对象包含的子对象内容不拷贝，因此，源对象与拷贝对象都会引用同一个子对象
print( '*' * 5, '浅拷贝', '*' * 5 )
disk=Disk()
print(disk)
computer=Computer(cpu1,disk)
import  copy
computer2=copy.copy(computer)  # 源对象：computer  子对象：cup1和disk  拷贝对象：computer2

print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)

# 深拷贝
# 使用copy模块的deepcopy函数，递归拷贝源对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
print( '*' * 5, '深拷贝', '*' * 5 )

computer3=copy.deepcopy(computer)

print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)