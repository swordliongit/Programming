
## Multi Line Strings:
```lua
[[
	Hello
	World
This is the third line.
]]
```

## Length of a String:

```lua
print(#str)
print(string.len(str))
```

## Concatenating Strings

```lua
print("hello" .. "world") --> helloworld
```

## Lower and Upper case Strings

```lua
string.upper(str)
string.lower(str)
```

## Substring of a String

```lua
string.sub(str, start, stop)
```

## ASCII to Character and Vice Versa

```lua
string.char(ASCII Code) --> char
string.byte("A") --> ascii code
```

## Repeat a String

```lua
print(string.rep(str, repeatnum, separator))
print(string.rep("hello", 5, " "))
```

## Formatted Strings

```lua
local str = string.format("Mr. %s your age is %i", name, age)
```

%s, %i, %.2f


## Find a String Part

Gives the starting and ending index of a substring inside another string

```lua
local str = "Hello World"
print(string.find(str, "orl")) --> 8     10
```


## Match a String

Returns the string if it finds, else returns nil

```lua
local str = "Hello World"
print(string.find(str, "orl")) --> orl
print(string.find(str, "orsl")) --> nil
```

## Replace String Parts

Replaces string parts and returns the replaced count

```lua
local str = "Hello World"
print(string.gsub(str, "hel", "lo")) --> lolo World      1
```