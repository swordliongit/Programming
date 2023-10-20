1. nil and boolean false --> Falsy
2. all numbers and boolean true --> Truthy

### OR
*if the result is true, it evaluates the first operand, otherwise evaluates the second operand*

```lua
local var = nil

var = var or 5 --> var is 5 because var is nil, truthy value gets assigned to the var
```

Equivalent to:
```lua
if not var then var = 5
```

### AND

*if the the result is true, it evaluates the second operand, otherwise evaluates the first operand*

#### TERNARY
*If x > y is true, it will compare x or y and if it's true too, it will evaluate x. So in short, if the condition is true, assings the first value, otherwise assigns the second value*
```lua
max = (x > y) and x or y
```
