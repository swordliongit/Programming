

## Array

```lua
local arr = {1, "hello", false, 4, 5}
```



## Inserting into Tables
[[Inserting Into Tables]]
```lua
table.insert(table, index, value)
```


## Removing from Tables
[[Removing From Tables]]
```lua
table.remove(table, index)
```


## Sorting Tables
[[Sorting Tables]]
```lua
table.sort(table)
```


## Displaying a Table by Concatenation
[[Displaying a Table by Concatenation]]
```lua
local arr = {1, 2, 3, 4}
print(table.concat(arr, " ")) --> 1 2 3 4
print(table.concat(arr, ",")) --> 1,2,3,4
```


## Length of Table
[[Length of a Table]]
```lua
#table
```


## Multi-dimensional Tables
[[Multi-dimensional Tables]]
```lua
local table2D = {
    {1, 2, 3},
    {12, 123, "hello", 45},
    {423, false, true}
}

for i = 1, #table2D do
   for j = 1, #table2D[i] do
    print(table2D[i][j])
   end 
end
```


## Table Constructors and Records
[[Table Constructors and Records]]
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

## Starting from Index 0
[[Starting from Index 0]]
```lua
days = {[0]="Sunday", "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday"}
```

## Linked Lists
[[Linked Lists]]
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


## Complex Tables
[[Complex Tables]]
```lua
local polyline = {color="blue", thickness=2, npoints=4,
                 {x=0,   y=0},
                 {x=-10, y=0},
                 {x=-10, y=1},
                 {x=0,   y=1}
            }
for key, value in pairs(polyline) do
    print(key, value)
end
```
*Output:*
```
1       table: 008F9D70
2       table: 008FA068
3       table: 008FA108
4       table: 008FA298
color   blue
npoints 4
thickness       2
```

*Notes:*
	As we can see, nested tables will have their indexes as integers. So we can access the nested table values like this:
```lua
print(polyline[2].x) --> -10
```