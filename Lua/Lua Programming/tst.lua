local file = io.open("/proc/loadavg", "r")
if file then
    local loadavg = file:read("*all")
    file:close()
    local load1, load5, load15 = loadavg:match("([%d%.]+)%s+([%d%.]+)%s+([%d%.]+)")
    if load1 and load5 and load15 then
        -- Calculate load averages as percentages
        local load1_percent = load1 * 100
        local load5_percent = load5 * 100
        local load15_percent = load15 * 100

        print("1-Minute Load Average: " .. load1_percent .. "%")
        print("5-Minute Load Average: " .. load5_percent .. "%")
        print("15-Minute Load Average: " .. load15_percent .. "%")
    else
        print("Failed to parse load averages.")
    end
else
    print("Unable to open /proc/loadavg")
end
