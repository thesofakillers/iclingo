import clingo


class ClingoInterface:
    """
    Wrapper class for executing a program
    via clingo.Control

    Class necessary to keep track of state
    for some print statements
    """

    def __init__(self):
        """these need to be kept track of in state"""
        self.optimum_found = False
        self.exhausted = False
        self.sat = False

    def run_program(self, program, clear_state=True):
        """runs ASP program, returning output as a string"""
        output = ""
        if clear_state:
            self._clear_state()
        control = clingo.Control()
        control.add("base", [], program)
        control.ground([("base", [])])
        output += "Solving..."
        model_count = 0
        for model in control.solve(yield_=True, on_finish=self._on_finish):
            model_count += 1
            output += f"\nAnswer {model_count}"
            output += "\n" + str(model)
        # generic statements
        if self.sat:
            output += "\nSATISFIABLE"
        else:
            output += "\nUNSATISFIABLE"
        stats = control.statistics["summary"]
        if stats["models"]["optimal"] > 0:
            self.optimum_found = True
            output += "\nOPTIMUM FOUND"
            output += f"\nOptimization: {stats['lower'][0]:n}"
        # additional statements
        output += (
            f"\n\nModels\t\t: {stats['models']['enumerated']:n}"
            + f"{'+' if not self.exhausted else ''}"
        )
        if self.optimum_found:
            output += "\n\tOptimum\t: yes"
            output += f"\nOptimization\t: {stats['lower'][0]:n}"
        output += (
            f"\nTime\t\t: {stats['times']['total']:.3f}s "
            f"(Solving: {stats['times']['solve']:.2f}s "
            f"1st Model {stats['times']['sat']:.3f}s "
            f"Unsat: {stats['times']['unsat']:.3f}s)"
        )
        return output

    def print_answer_sets(self, program, clear_globals=True):
        print(self.run_program(program, clear_globals))

    def _on_finish(self, res):
        """update state on finish"""
        self.sat = res.satisfiable
        self.exhausted = res.exhausted

    def _clear_state(self):
        """reset our state"""
        self.optimum_found = False
        self.exhausted = False
        self.sat = False
