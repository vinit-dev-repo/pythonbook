def timer_generator():
    start = time.perf_counter()
    try:
        yield                                # pause here until the caller resumes it
    finally:
        seconds = time.perf_counter() - start
        print(f"took {int(seconds * 10) / 10:.1f} seconds")
