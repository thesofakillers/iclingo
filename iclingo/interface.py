import clingo


class ClingoInterface:
    def __init__(self):
        self.optimum_found = False
        self.exhausted = False
        self.sat = False

    def generate_output(self, program, clear_globals=True):
        output = ""
        if clear_globals:
            self._clear_globals()
        control = clingo.Control()
        control.add("base", [], program)
        control.ground([("base", [])])
        output += "Solving..."
        model_count = 0
        for model in control.solve(yield_=True, on_finish=self._on_finish):
            model_count += 1
            output += f"\nAnswer {model_count}"
            output += "\n" + str(model)

        if self.sat:
            output += "\nSATISFIABLE"
        else:
            output += "\nUNSATISFIABLE"

        stats = control.statistics["summary"]
        if stats["models"]["optimal"] > 0:
            self.optimum_found = True
            output += "\nOPTIMUM FOUND"
            output += f"\nOptimization: {stats['lower'][0]:n}"

        output += (
            f"\nModels\t\t: {stats['models']['enumerated']:n}"
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
        print(self.generate_output(program, clear_globals))

    def _on_finish(self, res):
        self.sat = res.satisfiable
        self.exhausted = res.exhausted

    def _clear_globals(self):
        self.optimum_found = False
        self.exhausted = False
        self.sat = False
