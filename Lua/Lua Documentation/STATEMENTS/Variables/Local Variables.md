```lua
local var = 12
```

## Block Variables
[[Block Variables]]
```lua
do
    local a2 = 2
end
```

### Premature Return
*We cannot normally return if there's a statement after the return. But we can achieve it using a do block:*
```lua
function Foo()
    do
        return
    end
    local x = 5
end
```