"""clingo kernel for Jupyter"""
from ipykernel.kernelbase import Kernel
import clingo


class ClingoKernel(Kernel):
    implementation = "clingo"
    implementation_version = "0.1"
    language_info = {
        "name": "clingo",
        "mimetype": "text/x-clingo",
        "file_extension": ".lp",
        "pygments_lexer": "prolog",
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
        # TODO
        if not silent:
            # show output by sending a message to the frontend
            stream_content = {"TODO": "TODO"}
            self.send_response(self.iopub_socket, "stream", stream_content)
            # TODO
            pass
        # return a dict with the execution results
        return {
            "status": "ok",
            "execution_count": self.execution_count,
        }


if __name__ == "__main__":
    from ipykernel.kernelapp import IPKernelApp

    IPKernelApp.launch_instance(kernel_class=ClingoKernel)