start = time.perf_counter()
asyncio.run(main())
print(f"total: {round(time.perf_counter() - start)}.0s")
