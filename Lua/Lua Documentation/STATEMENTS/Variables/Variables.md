
## Local Variables
[[Local Variables]]
```lua
local var = 12
```

## Block Variables
```lua
do
    local a2 = 2
end
```

## Global Variables
[[Global Variables]]
```lua
Var = 15
_G.Varstr = "Test var"
```

### Making a Local Variable Global
```lua
function foo() do
	_G.Var = 45
end

print(Var)
```

## Multi Assigment
[[Multi Assigment]]
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