
async def coroutine_add_one(number: int) -> int:
    return number + 1


def add_one(number: int) -> int:
    return number + 1

function_result = add_one(1)
# 不会执行协程中的代码，只是得到了一个协程对象
coroutine_result = coroutine_add_one(1)

print(f"Function result is {function_result} and the type is {type(function_result)}")
print(f"Coroutine result is {coroutine_result} and the type is {type(coroutine_result)}")
