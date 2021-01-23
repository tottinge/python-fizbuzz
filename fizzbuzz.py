choices = {
    (0,1):"fizz",
    (1,0):"buzz",
    (1,1):"fizbuzz"
}
for i in range(101):
    key = ((i%5==0),(i%3==0))
    print(choices.get(key, i))
