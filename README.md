<p align="center"><a href="https://github.com/juancrrn/merlin-mobile" target="_blank"><img src="https://juancrrn.io/img/merlin-github-header-rgb-expanded.svg"></a></p>

## About Merlin Classifier

Component: face detection microservice.

Merlin Desktop is the Merlin project's desktop application AI-based classifier module.

(Under developement).

## Requirements

This module requires the following packages:

- Python 3.8
- Numpy 1.22
- OpenCV 4.5

## Python virtual environment

If you are willing to use a Python virtual environment, the `python3.8-venv` package is required. In Ubuntu systems, install it running `$ sudo apt install python3.8-venv`.

To include globally-installed packages to your virtual environment, link their `.so` file from `/usr/local/lib/python3.8/site-packages` or `/usr/local/lib/python3.8/dist-packages` to your `.venv/lib/python3.8/site-packages` directory. Example:

```console
$ ln -s /usr/local/lib/python3.8/site-packages/cv2 ~/merlin-classifier/.venv/lib/python3.8/site-packages/cv2
```

## Settings

Rename the `config/config-sample.py` file to `config/config.py` and set your desirde configuration inside the `Config` class:

- `appName`: the name of the app, visible on window titles; defaults to `Merlin Classifier`.
- `dataDirectory`: the global directory in which all Merlin data is stored; defaults to `~/Merlin/Data`.
- `flaskConfig`: the desired Flask configuration.
