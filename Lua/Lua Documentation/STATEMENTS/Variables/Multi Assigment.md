```lua
local start, end, step = 1, 10, 1
```

We can swap values using multi assigment, Lua first evaluates all the values and then executes the assigments:
```lua
x, y = y, x
a[i], a[j] = a[j], a[i]
```

Lua assigns nil to ignored variables in multi assigment
```lua
a, b, c = 0, 1
print(a,b,c) --> 0   1   nil
```