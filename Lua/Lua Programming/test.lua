function Cfunc()
    return io.close("asdsa")
end

local success, result = pcall(Cfunc)

if success then
    print("File opened successfully")
else
    print("An error occurred:", result)
end

print("Continuing...")
