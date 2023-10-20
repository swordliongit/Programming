**Notes:**
1. Coroutines have type ==thread==



## Creating Coroutines:
[[Creating Coroutines]]
*Simple coroutine:*
```lua
local cortn = coroutine.create(
    function ()
        for i = 1, 10, 1 do
            print(i)
            if i > 5 then
                coroutine.yield()
            end
        end
    end
)
```

*Different definition:*
```lua
local function cortn_func()
    for i = 1, 10, 1 do
        print(i)
        if i > 5 then
            coroutine.yield()
        end
    end
end

local cortn2 = coroutine.create(cortn_func)
```

This coroutine will be in the ==suspended== state. To start this coroutine we have to ==resume== it:
```lua
coroutine.resume(cortn)
```

### yield
	yield will pause the couroutine. To activate it again, we have to resume it again.

