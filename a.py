def ring(func):
    def like():
        print("like")
        return item()

    def item():
        print("good boy")
        return func
    return like()
@ring
def notgood():
    print("regular")
    return ding()
def good(func1):
    print("Like you not")
    return func1
@good
def ding():
    print("good things")

notgood()