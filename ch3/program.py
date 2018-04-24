import MyModule0301
import MyModule0311
import MyModule0312
import MyModule0313
import MyModule0314
import MyModule0315
import MyModule0321

from statistics import pvariance
from matplotlib import pyplot as plt

a = [1, 3, 5, 7, 9, 11, 13, 14, 15]

if __name__ == "__main__":
    print("** MyModule0301 **")
    b = MyModule0301.getAN(a, 1, 3)
    print(b)
    b = MyModule0301.getAN(a, 1, 20)
    print(b)
    
    print("** MyModule0311 **")
    b = MyModule0311.getA(5)
    MyModule0311.printA(b)
    
    print("** MyModule0312 **")
    b = MyModule0312.getA(10)
    MyModule0312.printA()
    variance = MyModule0312.getVariance(b)
    print("Variance :", variance)
    print("By stdmd :", pvariance(b))

    print("** MyModule0313 **")
    result = MyModule0313.find(a,5)
    print(result)
    result = MyModule0313.find(a,6)
    print(result)

    print("** MyModule0314 **")
    a = [-1, -2, 3, 4, 5]
    b = [5, 4, 3, -2, -1]
    norm = MyModule0314.getNorm(a)
    print(norm)
    norm = MyModule0314.getNorm(a)
    print(norm)
    product = MyModule0314.getProduct(a,b)
    print(product)

    print("** MyModule0315 **")
    MyModule0315.printEven(a)
    MyModule0315.printNumber(1000)

    print("** MyModule0321 **")
    plt.title("Escherichia coli population simulation")
    plt.xlabel("$\Delta t$")
    plt.ylabel("Population factor")
    for kx in range(5):
        k = kx*.5 + .5
        result = [MyModule0321.getNumberEColi(k, 0.1, t) for t in range(32)]
        label = "$k={}$".format(k)
        plt.plot(result, label=label)
    plt.legend()
    plt.savefig("numer_of_ecoli.png")
