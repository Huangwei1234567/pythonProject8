#迭代器
# a= {'mm':1,'vv':7}
# b=iter(a.values())
# print(next(b))
# print(next(b))
# a=[1,2,3,[1.2,3]]
# b=a.deepcopy()
# print(id(a))
# print(id(b))
# print(id(a[-1]))
# print(id(b[-1]))
# class Hw():
#     def __init__(self):
#         self._b=0
#         self.c=1
#     def _aa(self):
#         print('xx')
#生成器
def intNum():
    print("开始执行")
    for i in range(5):
        yield i
        print("继续执行")
num = intNum()
print(next(num))
print(next(num))