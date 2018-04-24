hoge = "let's start!"
for i in range(100):
    print(hoge)
    hoge = '{0:>3d}: '.format(i)
    if i % 2 == 0:
        hoge += 'Fizz'
    if i % 3 == 0:
        hoge += 'Buzz'
print(hoge)
