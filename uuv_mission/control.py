class PDController:
    # Proportional-Derivative Controller for controlling the UUV's depth.
    # The controller computes the control action based on the error between the reference depth 
    # and the observed depth, as well as the rate of change of this error.
    # The controller has two parameters: Kp (proportional gain) and Kd (derivative gain). 
    # The proportional term is responsible for reducing the error, while the derivative term
    # helps to dampen the response and reduce overshoot. Both can be tuned to acheive the desired performance 
    # of the UUV's depth control system.
   
    def __init__(self, Kp: float = 0.15, Kd: float = 0.6):
        self.kp = Kp
        self.kd = Kd

# Code to reset the controller state for the start of each run, effectively setting e[-1] = 0.0
# as required in the assignment instructions. 
    def reset(self):
        self.prev_error = 0.0 

# Code to compute the control action based on the reference depth and the observed depth.
# Need to make sure systems engineer uses same syntax and argument order.
        
    def compute_action(self, reference: float, output: float) -> float:
        error = reference - output
        action = self.kp * error + self.kd * (error - self.prev_error)
        self.prev_error = error
        return action