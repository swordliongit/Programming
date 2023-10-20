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