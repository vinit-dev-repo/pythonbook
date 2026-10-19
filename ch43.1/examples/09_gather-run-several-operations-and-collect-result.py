async def risky(n):
    if n == 2:
        raise ValueError(f"task {n} failed")
    return f"task {n} ok"

async def main():
    results = await asyncio.gather(
        risky(1), risky(2), risky(3),
        return_exceptions=True,
    )
    for r in results:
        print(r)

asyncio.run(main())
