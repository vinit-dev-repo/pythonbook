import dis
from types import CodeType

source = """class Calibration:
    events.append("class body")
    factor = 3
    def apply(self, reading):
        return reading * self.factor
"""
module_code = compile(source, "<calibration>", "exec")
events = []
namespace = {"events": events, "__name__": "runtime_lab"}
body = next(value for value in module_code.co_consts
            if isinstance(value, CodeType) and value.co_name == "Calibration")
print("before execution:", events, "Calibration" in namespace)
print("build-class instruction:", any(item.opname == "LOAD_BUILD_CLASS"
      for item in dis.get_instructions(module_code)))
print("method code stored:", any(isinstance(value, CodeType) and value.co_name == "apply"
      for value in body.co_consts))
exec(module_code, namespace)
print("after execution:", events, namespace["Calibration"]().apply(4))
