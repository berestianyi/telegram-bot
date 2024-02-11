import execjs
import asyncio

script_path = "vidminok.js"

ctx = execjs.compile(open(script_path).read())


async def call_async_js_function():
    result = await asyncio.to_thread(ctx.call, "myFunction")
    print(result)

asyncio.run(call_async_js_function())

