from __future__ import print_function

from metakernel import MetaKernel
import aiml
import os

class ChatbotKernel(MetaKernel):
    implementation = 'Chatbot'
    implementation_version = '1.0'
    language = 'text'
    language_version = '0.1'
    banner = "Calysto Chatbot - a chatbot for Jupyter"

    magic_prefixes = dict(magic='%', shell='!', help='?')
    help_suffix = None

    def get_usage(self):
        return """Calysto Chatbot
Use: 
    load aiml b
    load alice

to activate a database of rules.

Use:
    %learn /path/to/startup.xml

to load a database.
"""

    def __init__(self, *args, **kwargs):
        self.kernel = aiml.Kernel()
        os.chdir(os.path.join(os.path.dirname(aiml.__file__),
                              "standard"))
        self.kernel.learn("startup.xml")
        #self.kernel.respond("load aiml b")
        os.chdir(os.path.join(os.path.dirname(aiml.__file__),
                              "alice"))
        self.kernel.learn("startup.xml")
        #self.kernel.respond("load alice")
        super(ChatbotKernel, self).__init__(*args, **kwargs)

    def do_execute_direct(self, code):
        if code.startswith("%learn"):
            folder, filename = os.path.split(code[6:])
            os.chdir(folder.strip())
            self.kernel.learn(filename.strip())
        else:
            self.Print(self.kernel.respond(code))
        return None

