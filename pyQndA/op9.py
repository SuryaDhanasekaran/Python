def demo(x,y=[]):
    y.append(x)
    return y

demo(1)
demo(2)
z = demo(3)
print(z)