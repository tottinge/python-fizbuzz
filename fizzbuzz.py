should_fizz = lambda i: (i % 3 == 0)
should_buzz = lambda i: (i % 5 == 0)
choices = {
    (True, False):"fizz",
    (False, True):"buzz",
    (True, True ):"fizbuzz"
}
for i in range(1,101):
    key = should_fizz(i), should_buzz(i)
    print(choices.get(key, i))
