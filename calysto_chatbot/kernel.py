from __future__ import print_function

from metakernel import MetaKernel
import aiml
import sys
import os

class ChatbotKernel(MetaKernel):
    implementation = 'Chatbot'
    implementation_version = '1.0'
    language = 'text'
    language_version = '0.1'
    banner = "Calysto Chatbot - a chatbot for Jupyter"
    language_info = {
        'mimetype': 'text/plain',
        'name': 'text',
        'codemirror_mode': {'name': 'text'},
        'pygments_lexer': 'text',
    }

    magic_prefixes = dict(magic='%', shell='!', help='?')
    help_suffix = None

    kernel_json = {
        "argv": [sys.executable,
                 "-m", "calysto_chatbot",
                 "-f", "{connection_file}"],
        "display_name": "Calysto Chatbot",
        "language": "text",
        "codemirror_mode": "text",
        "name": "calysto_chatbot"
    }

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
        #os.chdir(os.path.join(os.path.dirname(aiml.__file__),
        #                      "botdata", "standard"))
        #self.kernel.learn("startup.xml")
        #self.kernel.respond("load aiml b")
        os.chdir(os.path.join(os.path.dirname(aiml.__file__),
                              "botdata", "alice"))
        self.kernel.learn("startup.xml")
        #self.kernel.respond("load alice")
        super(ChatbotKernel, self).__init__(*args, **kwargs)

    def do_execute_direct(self, code):
        if code.startswith("%learn"):
            AIML_PATH = os.path.join(os.path.dirname(aiml.__file__), "botdata")
            learn_path = code[6:]
            learn_path = learn_path.replace("{AIML_PATH}", AIML_PATH)
            folder, filename = os.path.split(learn_path)
            os.chdir(folder.strip())
            self.kernel.learn(filename.strip())
        else:
            response = self.kernel.respond(code)
            if not code.startswith("load "):
                if response:
                    self.Print(response)
                else:
                    self.Error("No response; consider 'load alice' or '%learn {AIML_PATH}/standard/startup.xml' followed by 'load aiml b'")
        return None

