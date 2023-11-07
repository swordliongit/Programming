local co = coroutine.create(function()
    for k, v in pairs({ 1, 2, 3, 4, 5 }) do
        print(v)
        coroutine.yield()
    end
end)

coroutine.resume(co)
coroutine.resume(co)
