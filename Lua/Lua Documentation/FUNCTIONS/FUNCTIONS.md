```lua
function <function_name>(param1, param2)
	--
end
```

## Local Functions
[[Local Functions]]
```lua
local adder = function (x, y)
    print(x+y)
end
```

## Returning Multiple Values
[[Returning Multiple Values]]
```lua
local adder = function (x, y)
    return x^2, y^2
end

local px, py = adder(2, 5)
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


## Returning Functions
[[Returning Functions]]
```lua
local function outer(x)

    return function ()
        return x^2
    end

end

local inner = outer(5) --> returns the anonymous function, inner now is that function itself

print(inner()) --> 25
```


## Variable Arguments
[[Variable Arguments]]
```lua
local function func(...)
    for key, value in pairs({...}) do --> ellipsis casted into a table
        print(key, value)
    end
end

func(1, 5, 32, 12, 6)
```

## Unpack
[[Unpack]]
Serializes a table into consecutive tuple values
```lua
function Tarr(...)

    for key, value in pairs({...}) do
        print(key, value)
    end
end

local varr = {32,2,23,1234,12412,24}
print(unpack(varr))
```