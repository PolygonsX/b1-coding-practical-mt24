from control import PDController

c = PDController(Kd=0.6, Kp=0.15)
print(c.compute_action(1.0, 0.0))   # expect 0.75
print(c.compute_action(1.0, 0.5))   # expect -0.225
c.reset()
print(c.prev_error)                  # expect 0.0