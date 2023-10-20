```lua
local tb = {
    x = 12,
    y = 42,
    z = 2
}

print(tb["x"]) --> 12
```

Same  thing:
```lua
local tb = {}

tb.x = 12
tb.y = 42
tb.z = 2
```

We can create sets using the constructor syntax and have any type of key we want:
```lua
local tb = {
	["first"] = "entry1",
	["second"] = "entry2",
	["third"] = "entry3"
}

print(tb["first"])
```

### Different Types of Keys
```lua
local tb = {
    ["first"] = 1,
    ["second"] = 2,
    ["third"] = 3,
    [1] = "fourth",
    [2] = 15
}

for key, value in pairs(tb) do
    print(key, value)
end
```
*Output:*
```
2       15
1       fourth
first   1
third   3
second  2
```
