# 2
import logging

print("root level:", logging.getLogger().getEffectiveLevel())
print("INFO is:", logging.INFO)
logging.info("hello")
