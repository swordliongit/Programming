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