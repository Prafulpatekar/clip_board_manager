from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

APP = ['src/clipbot.py']
DATA_FILES = []
OPTIONS = {
    'iconfile': 'clipboard.icns'
}

setup(
    name="clipbot",
    version="0.0.1",
    author="Praful Patekar",
    author_email="prafulpatekar23@gmail.com",
    description="Clipboard manager using tkinter",
    python_requires=">=3.7",
    long_description=long_description,
    url="https://github.com/Prafulpatekar/clip_board_manager",
    keywords=['clip_board','clipboard', 'clipboard-manager'],
    app=APP,
    data_files=DATA_FILES,
    install_requires=["pyperclip>=1.6.4", "py2app==0.28.8"],
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    test_suite='test',
    license='NONE',
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)