```lua
Var = 15
_G.Varstr = "Test var"
```

### Making a Local Variable Global
[[Making a Local Variable Global]]
```lua
function foo() do
	_G.Var = 45
end

print(Var)
```