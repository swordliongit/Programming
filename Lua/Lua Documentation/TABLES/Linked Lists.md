```lua
local list = nil
local counter = 1
for line in io.lines() do
    list = {next=list, value=line}
    if counter == 5 then
        break
    end
    counter = counter + 1
end

local l = list
while l do
    print(l.value)
    l = l.next
end
```