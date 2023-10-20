```lua
local function func(...)
    for key, value in pairs({...}) do --> ellipsis casted into a table
        print(key, value)
    end
end

func(1, 5, 32, 12, 6)
```
