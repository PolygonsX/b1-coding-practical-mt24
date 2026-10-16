class PDController:
    """Proportional-Derivative Controller for controlling the UUV's depth.
     Implements the discrete-time control law

        u[t] = Kp * e[t] + Kd * (e[t] - e[t-1]),   e[t] = r[t] - y[t],

    with e[-1] = 0. The derivative term is a backward difference per time
    step (the simulation uses dt = 1, so no division by dt is needed).

    The controller is stateful: it stores the previous error. Call reset()
    at the start of every simulation run, and call compute_action() exactly
    once per time step.

    Attributes:
        Kp: Proportional gain.
        Kd: Derivative gain.
        prev_error: Error from the previous time step, e[t-1].
    """
    def __init__(self, Kp: float = 0.15, Kd: float = 0.6):
        self.Kp = Kp
        self.Kd = Kd
        self.prev_error = 0.0  # Instructions assume e[-1] = 0.0
        
# Code to reset the controller state for the start of each run, effectively setting e[-1] = 0.0
# as required in the assignment instructions. 
    def reset(self):
        """ Clear the stored error so a new run starts from e[-1 = 0.0]"""
        self.prev_error = 0.0 
  
    def compute_action(self, reference: float, output: float) -> float:
        """Return the control action u[t] for the current time step.
        Args:
            reference: Target depth r[t].
            output: Measured depth y[t], from Submarine.get_depth().
        Returns:
            Control action u[t] to be applied to the submarine.
        """ 
        error = reference - output
        action = self.Kp * error + self.Kd * (error - self.prev_error)
        self.prev_error = error #update after use so the next call sees e[t-1]
        return action