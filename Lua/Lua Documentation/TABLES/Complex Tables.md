```lua
local polyline = {color="blue", thickness=2, npoints=4,
                 {x=0,   y=0},
                 {x=-10, y=0},
                 {x=-10, y=1},
                 {x=0,   y=1},
                 ["+"] = 14,
                 ["/"] = 20
            }
for key, value in pairs(polyline) do
    print(key, value)
end
```
*Output:*
```
1       table: 00F29C58
2       table: 00F29CD0
3       table: 00F2A248
4       table: 00F2A1F8
thickness       2
+       14
color   blue
npoints 4
/       20
```

*Notes:*
	As we can see, nested tables will have their indexes as integers. So we can access the nested table values like this:
```lua
print(polyline[2].x) --> -10
```