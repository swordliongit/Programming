```lua
local function outer(x)

    return function ()
        return x^2
    end

end

local inner = outer(5) --> returns the anonymous function, inner now is that function itself

print(inner()) --> 25
```

A function call that is not the last element of the list always returns 1 value:
```lua
function foo2 () return 'a','b' end

x,y = foo2(), 20      -- x='a', y=20, b is discarded

a = {foo2(), 5} --> {'a', 5}
```

### Forcing 1 Value Returns

By enclosing in extra parenthesis we force the function to return only 1 value:
```lua
print((foo2())) --> 'a'
```
