import io
import sys

from setuptools import find_packages, setup

kernel_json = {
    "argv": [sys.executable, 
	     "-m", "calysto_chatbot", 
	     "-f", "{connection_file}"],
    "display_name": "Calysto Chatbot",
    "language": "chatbot",
    "name": "calysto_chatbot"
}

with io.open('calysto_chatbot/__init__.py', 'rb') as fid:
    for line in fid:
        line = line.decode('utf-8')
        if line.startswith('__version__'):
            __version__ = line.strip().split()[-1][1:-1]
            break

with io.open('README.md') as f:
    readme = f.read()

setup(name='calysto_chatbot',
      version=__version__,
      description='A Chatbot kernel for Jupyter that can use Python libraries',
      long_description=readme,
      url="https://github.com/Calysto/calysto_chatbot",
      author='Douglas Blank',
      author_email='doug.blank@gmail.com',
      packages=find_packages(include=["calysto_chatbot", "calysto_chatbot.*"]),
      install_requires=["metakernel", "aiml"],
      classifiers = [
          'Framework :: IPython',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 2',
      ]
)
