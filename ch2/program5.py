import MyModule5

n = 10

if __name__ == '__main__':
    rand_list = MyModule5.getDoubleRandomList(n)
    for i in range(n):
        print(rand_list[i])
