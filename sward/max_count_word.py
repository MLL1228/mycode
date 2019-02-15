#  找出一个文件中出现次数最多的单词
#  思路： 将文件读取，对每一行做 strip 和 split 处理，对每个单词进行统计

def solution():
    res={}
    with open("123.txt", "r") as f:
        for line in f:
            line_words = line.strip().split()
            for word in line_words:
                if word in res:
                    res[word] += 1
                else:
                    res[word] = 1


    # 字典转化为列表
    mylist=[]
    for i in res:
        mylist.append((res[i], i))
    mylist.sort(reverse=True)

    for j in range[10]:
        print(mylist[j])









