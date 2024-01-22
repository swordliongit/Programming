success, result, error = pcall(dofile, "mod.lua")

print(success, result, error)


-- local socket = require 'socket'

-- local function myFunction()
--     print("Before sleep")
--     socket.sleep(4)
--     print("After sleep")
--     socket.sleep(2)
-- end

-- local success, error_message = io.popen("myFunction")
-- print("After pcall")
