gen = echo()
gen.send("too soon")   # ERROR -- gen hasn't reached a yield yet
