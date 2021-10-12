try:
    list = [10,0,20]
    result = list[0] / list[1]
    print(result)
except ZeroDivisionError:
    print("Can't devided to zero.")
except IndexError:
    print("Index error.")
finally:
    print("done")