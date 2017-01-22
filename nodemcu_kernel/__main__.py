from ipykernel.kernelapp import IPKernelApp
from .kernel import NodeMcuKernel

IPKernelApp.launch_instance(kernel_class=NodeMcuKernel)
