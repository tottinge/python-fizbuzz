choices = {
    (False,True):"fizz",
    (True,False):"buzz",
    (True,True):"fizbuzz"
}
for i in range(101):
    key = ((i%5==0),(i%3==0))
    print(choices.get(key, i))
