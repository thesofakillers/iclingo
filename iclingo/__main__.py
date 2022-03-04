from ipykernel.kernelapp import IPKernelApp
from .kernel import ClingoKernel

IPKernelApp.launch_instance(kernel_class=ClingoKernel)
