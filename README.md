Django Tutorial in Visual Studio Code
Django is a high-level Python framework designed for rapid, secure, and scalable web development. Django includes rich support for URL routing, page templates, and working with data.

In this Django tutorial, you create a simple Django app with three pages that use a common base template. You create this app in the context of Visual Studio Code in order to understand how to work with Django in the VS Code terminal, editor, and debugger. This tutorial does not explore various details about Django itself, such as working with data models and creating an administrative interface. For guidance on those aspects, refer to the Django documentation links at the end of this tutorial.

The completed code project from this Django tutorial can be found on GitHub: python-sample-vscode-django-tutorial.

If you have any problems, you can search for answers or ask a question on the Python extension Discussions Q&A.

Prerequisites
To successfully complete this Django tutorial, you must do the following (which are the same steps as in the general Python tutorial):

Install the Python extension.

Install a version of Python 3 (for which this tutorial is written). Options include:

(All operating systems) A download from python.org; typically use the Download Python 3.9.1 button that appears first on the page (or whatever is the latest version).
(Linux) The built-in Python 3 installation works well, but to install other Python packages you must run sudo apt install python3-pip in the terminal.
(macOS) An installation through Homebrew on macOS using brew install python3 (the system install of Python on macOS is not supported).
(All operating systems) A download from Anaconda (for data science purposes).
On Windows, make sure the location of your Python interpreter is included in your PATH environment variable. You can check the location by running path at the command prompt. If the Python interpreter's folder isn't included, open Windows Settings, search for "environment", select Edit environment variables for your account, then edit the Path variable to include that folder.

Create a project environment for the Django tutorial
In this section, you create a virtual environment in which Django is installed. Using a virtual environment avoids installing Django into a global Python environment and gives you exact control over the libraries used in an application. A virtual environment also makes it easy to Create a requirements.txt file for the environment.

On your file system, create a project folder for this tutorial, such as hello_django.

In that folder, use the following command (as appropriate to your computer) to create a virtual environment named .venv based on your current interpreter:

# Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
source .venv/bin/activate

# macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
py -3 -m venv .venv
.venv\scripts\activate
Note: Use a stock Python installation when running the above commands. If you use python.exe from an Anaconda installation, you see an error because the ensurepip module isn't available, and the environment is left in an unfinished state.

Open the project folder in VS Code by running code ., or by running VS Code and using the File > Open Folder command.

In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter command:

Django tutorial: opening the Command Palette in VS Code

The command presents a list of available interpreters that VS Code can locate automatically (your list will vary; if you don't see the desired interpreter, see Configuring Python environments). From the list, select the virtual environment in your project folder that starts with ./.venv or .\.venv:

Django tutorial: Selecting the virtual environment for Python

Run Terminal: Create New Terminal (Ctrl+Shift+`) from the Command Palette, which creates a terminal and automatically activates the virtual environment by running its activation script.

Note: On Windows, if your default terminal type is PowerShell, you may see an error that it cannot run activate.ps1 because running scripts is disabled on the system. The error provides a link for information on how to allow scripts. Otherwise, use Terminal: Select Default Profile to set "Command Prompt" or "Git Bash" as your default instead.

The selected environment appears on the right side of the VS Code status bar, and notices the ('.venv': venv) indicator that tells you that you're using a virtual environment:

Django tutorial: selected environment showing in the VS Code status bar

Update pip in the virtual environment by running the following command in the VS Code Terminal:

python -m pip install --upgrade pip
Install Django in the virtual environment by running the following command in the VS Code Terminal:

python -m pip install django
You now have a self-contained environment ready for writing Django code. VS Code activates the environment automatically when you use Terminal: Create New Terminal (Ctrl+Shift+`). If you open a separate command prompt or terminal, activate the environment by running source .venv/bin/activate (Linux/macOS) or .venv\Scripts\Activate.ps1 (Windows). You know the environment is activated when the command prompt shows (.venv) at the beginning.

Create and run a minimal Django app
In Django terminology, a "Django project" is composed of several site-level configuration files, along with one or more "apps" that you deploy to a web host to create a full web application. A Django project can contain multiple apps, each of which typically has an independent function in the project, and the same app can be in multiple Django projects. An app, for its part, is just a Python package that follows certain conventions that Django expects.

To create a minimal Django app, then, it's necessary to first create the Django project to serve as the container for the app, then create the app itself. For both purposes, you use the Django administrative utility, django-admin, which is installed when you install the Django package
