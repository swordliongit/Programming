*file.lua:*
```lua
function Double(x)
	return x*2
end
```

From the Lua interpreter:

```lua
> dofile("file.lua")
> print(Double(5)) --> 10
```


Alternate method:
```lua
> require("file")
> print(Double(5)) --> 10
```