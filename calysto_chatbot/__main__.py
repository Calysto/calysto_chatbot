from IPython.kernel.zmq.kernelapp import IPKernelApp
from .kernel import ChatbotKernel
IPKernelApp.launch_instance(kernel_class=ChatbotKernel)
