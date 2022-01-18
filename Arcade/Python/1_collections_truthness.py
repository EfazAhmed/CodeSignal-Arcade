# What will be the value of res after the following snippet is exectued:

xs = [()]
res = [False] * 2
if xs:
    res[0] = True
if xs[0]:
    res[1] = True

# Answer => [True, False]