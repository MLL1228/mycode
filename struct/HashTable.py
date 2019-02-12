import uuid


# table 是用来存储数据的数组，初始化有 10007 个格子（最好选素数，可得到更合理的下标分布）
# 是字典的基础。实现了 add has_key get方法
class HashTable():
    def __init__(self):
        self.table_size = 10007
        self.table = [0] * self.table_size   # 初始化一个 table_size 大小的列表，每个元素都为0

    # 实现 in 、not in 语法
    def __contains__(self, item):
        return self.has_key(item)

    # 计算元素 hash 值
    def __hash(self, key):
        '''
        输入一个字符串，生成一串对应的数字。
        计算 hash 值的方法：把字符当作 N 进制数字得到结果
                          'qwe' 被视为 q* 1 + w * 10 + e* 100 得到结果 n
        n：hash 值
        f： 位数
        :return:
        '''
        n = 1
        f = 1
        for i in key:
            n += ord(i) * f
            f *= 10
        return n

    # 计算元素的下标
    def __index(self, key):
        return self.__hash(key) % self.table_size

    # 实现插入值
    def __insert_at_index(self, index, key, value):
        '''
        检查是否是第一次插入数据，如果是，就插入 list 进行存储
        如果不是第一次插入，且没有这个 key，就进行添加
        如果不是第一次插入，且有这个 key，就对 value 进行更新
        :param index:
        :param key:
        :return:
        '''
        v = self.table[index]
        if isinstance(v, int):
            self.table[index] = [(key, value)]
            return True
        else:
            for i in v:
                if i[0] == key:
                    if i[1] != value:
                        v[v.index(i)] = (key, value)
                return True
            self.table[index].append((key, value))
            return True

    # 检查元素是否存在
    def has_key(self, key):
        '''
        :param key:
        :return:
        检查一个 key 是否存在，时间很短，是 o（1）
        如果用 list 来存储，需要遍历，是 o（n）
        '''

        index = self.__index(key)
        v = self.table[index]   # 取出对应位置的元素
        if isinstance(v, list):
            for key_of_v in v:
                if key_of_v[0] == key:
                    return True
        return False

    # 添加元素进行存储
    def add(self, key, value):
        '''
        将 key 存储进 hashmap
        :param key:
        :return:
        '''
        #  计算下标
        index = self.__index(key)
        # 在下标处插入元素
        self.__insert_at_index(index, key, value)

    def get(self, key, value=None):

        index = self.__index(key)
        v = self.table[index]

        if isinstance(v, list):
            for i in v:
                if i[0] == key:
                    return i[1]
        return value


def test():
    names = [
        'chun',
        'mian',
        'bu',
        'jue',
        'xiao',
    ]
    ht = HashTable()
    for key in names:
        value = uuid.uuid4()
        ht.add(key, value)
        print('add 元素', key, value)
    for key in names:
        v = ht.get(key)
        print('get 元素', key, v)
    print('魔法方法', 'chun' in ht)


if __name__ == '__main__':
    test()




