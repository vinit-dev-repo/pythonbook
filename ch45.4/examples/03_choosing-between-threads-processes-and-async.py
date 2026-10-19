async def add_bonus():
    balance = await read_balance()       # another task can run right here
    await write_balance(balance + 100)   # and its update is now overwritten
