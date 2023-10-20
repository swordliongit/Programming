--

-- Vlan = {
--     tag = 5,
--     network = "10.0.0.0/24",
--     netmask = "255.255.255.0",
--     gateway = "10.0.0.1"
-- }

-- Define the metatable for the Vlan object
local Vlan = {}

-- Constructor function for creating new Vlan objects
function Vlan:new(tag, network, netmask, gateway)
    local obj = {
        tag = tag,
        network = network,
        netmask = netmask,
        gateway = gateway
    }
    setmetatable(obj, self)
    self.__index = self
    return obj
end

-- Info method for Vlan objects
function Vlan:Info()
    return self.tag, self.network, self.netmask, self.gateway
end

-- Create Vlan objects using the constructor
local Vlan5 = Vlan:new("5", "10.0.0.0/24", "255.255.255.0", "10.0.0.1")
local Vlan10 = Vlan:new("10", "172.16.0.0/24", "255.255.0.0", "172.16.0.1")

-- Access and print Vlan information using the Info method
print(Vlan5:Info())
print(Vlan10:Info())
