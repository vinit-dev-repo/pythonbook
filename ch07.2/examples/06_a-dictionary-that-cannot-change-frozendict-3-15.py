limits = frozendict(small=5, large=20)
print(limits["small"], limits.get("huge", 0), "large" in limits)
print(limits)

prices = {frozendict(size="small"): 3.5, frozendict(size="large"): 6.0}
print(prices[frozendict(size="large")])
