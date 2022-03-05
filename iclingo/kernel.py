"""clingo kernel for Jupyter"""
from ipykernel.kernelbase import Kernel
from .interface import ClingoInterface


class ClingoKernel(Kernel):
    implementation = "clingo"
    implementation_version = "0.1"
    language_info = {
        "name": "clingo",
        "mimetype": "text/x-clingo",
        "file_extension": ".lp",
        "version": "0.1",
    }
    banner = "iclingo - for ASP in Jupyter"

    def do_execute(
        self, code, silent, store_history=True, user_expressions=None, allow_stdin=False
    ):
        """
        Returns a dict containing the fields described in Execution results.
        https://jupyter-client.readthedocs.io/en/stable/messaging.html#execution-results

        To display output, can send messages using send_response().
        """
        # execute code
        clingo = ClingoInterface()
        error = None
        ok = True
        try:
            std_out = clingo.run_program(code)
        except Exception as e:
            error = e
            ok = False
        # handle errors
        if not ok:
            if not silent:
                error_content = {"ename": "", "evalue": str(error), "traceback": []}
                self.send_response(self.iopub_socket, "error", error_content)
            # return a dict with the execution results
            return {
                "status": "error",
                "execution_count": self.execution_count,
            }
        # in case things worked fine
        elif ok:
            if not silent:
                # show output by sending a message to the frontend
                stream_content = {"name": "stdout", "text": std_out}
                self.send_response(self.iopub_socket, "stream", stream_content)
            # return a dict with the execution results
            return {
                "status": "ok",
                "execution_count": self.execution_count,
            }
