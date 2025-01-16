# Setup Guide

## Prerequisites

### Required Software

(See [the brief installation guide video](/docs/Kooha-2025-01-16-22-41-07.webm).)

For this class, you will need [Python](https://www.python.org/downloads/), [VSCode](https://code.visualstudio.com/download), [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [Pyenv](https://github.com/pyenv/pyenv), [Pipenv](https://pipenv.pypa.io/en/latest/installation.html), and thte [Google Cloud CLI](https://cloud.google.com/sdk/docs/install). Prior to proceeding to the setup instructions, make sure you have all of these installed for your OS (see the hyperlinks to the setup instructions).

All of this should take no more than 15-20 minutes, assuming you have none of the software installed. (Python and Git ship by default on all computers running macOS or Linux.)

#### For Windows Users

For Windows users, installation will be a little more challenging. Specifically, I find Python instllations annoying because Python isn't automatically added to your system path. To add it, try the following (you may have to change the precise path to your Python installation, and you might need to consult with online references and/or ChatGPT). Run this in PowerShell:

```
[System.Environment]::SetEnvironmentVariable('PATH', $env:PATH + ";" + $env:USERPROFILE + "\AppData\Local\Programs\Python\Python313;" + $env:USERPROFILE + "\AppData\Local\Programs\Python\Python313\Scripts", "User")
```

Also, there is no official `pyenv` for Windows; instead, there's a `pyenv-win`, which I recommend installing via `pip` after you've already installed the latest Python. Run the following in the command prompt (NOT PowerShell)

```
pip install pyenv-win --target %USERPROFILE%\\.pyenv
```

You will likely then have to [add `pyenv` to your system path](https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md#add-system-settings) like so, run in PowerShell line by line:

```
[System.Environment]::SetEnvironmentVariable('PYENV_HOME', $env:USERPROFILE + "\.pyenv\pyenv-win", "User")

[System.Environment]::SetEnvironmentVariable('PYENV_ROOT', $env:USERPROFILE + "\.pyenv\pyenv-win", "User")

[System.Environment]::SetEnvironmentVariable('PYENV', $env:USERPROFILE + "\.pyenv\pyenv-win", "User")

[System.Environment]::SetEnvironmentVariable('PATH', $env:PATH + ";" + $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims", "User")
```

Then restart your shell to see the changes:

```
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH", "User")
```

### Google Cloud Account

We will use Google Earth Engine at different points in this course. In order to do so, please [follow these instructions](https://towardsai.net/p/machine-learning/how-to-set-up-a-google-earth-engine-cloud-project) to make sure you have a Google Cloud account set up for use with Google Earth Engine.

## Setup Instructions

Once you have installed the required software and set up your Google Cloud account, open a git terminal and clone this repository in your desired location:

```
git clone https://github.com/nlebovits/musa-650-spring-2025.git/
```

Once the repo is cloned, navigate to the root directory, install Python 3.11, install dependencies, and activate the virtual environment:

```
pyenv install 3.11
pyenv local 3.11
pipenv install
```

(On Windows, run `pyenv install 3.11.0b4` and `pyenv local 3.11.0b4`.)

Finally, activate the environment in your terminal using `pipenv shell` and then run `earthengine authenticate` to set up Google Earth Engine access (see these instructions for more information).

_It is likely that you will run into issues here; please troubleshoot as a class in person or on the discussion board on GitHub so we can solve problems collectively._

Congrats! You're ready to go. :)
