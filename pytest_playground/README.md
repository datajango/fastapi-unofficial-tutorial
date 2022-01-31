# PyTest Playground

- By Anthony Leotta

Being able to step debug unit tests is vitally important. Developing good unit tests can often be harder that developing the actual code.

## Setup

- pytest.ini

    ```
    [pytest]

    python_files = test*.py
    python_classes = Test
    python_functions = test
    addopts = --tb=native
    console_output_style = classic
    junit_duration_report = call
    filterwarnings = ignore::RuntimeWarning
    ```

- launch.json

    ```
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "PyTest",
                "type": "python",
                "request": "launch",
                "stopOnEntry": false,
                "module": "pytest",
                "args": [
                    "-sv"
                ],
                "cwd": "${workspaceRoot}",
                "env": {},
                "envFile": "${workspaceRoot}/.env",
                "debugOptions": [
                    "WaitOnAbnormalExit",
                    "WaitOnNormalExit",
                    "RedirectOutput"
                ]
            },
        ]
    }
    ```
- settings.json

    ```
    {
        "python.pythonPath": "/g/ProgramData/Anaconda3/envs/fastapi39/python",
        "python.testing.unittestEnabled": false,
        "python.testing.nosetestsEnabled": false,
        "python.testing.pytestEnabled": true,
        "python.testing.pytestArgs": [
            "--pdb"
        ],
        "git.ignoreLimitWarning": false
    }
    ```

## Testing Cookbook

```
python -m unittest discover
```


## Credits

- [Debugging pytest in VSCode (without adding files to your project)](https://keathmilligan.net/debugging-pytest-in-vscode)
- [Python debugging in VS Code](https://code.visualstudio.com/docs/python/debugging)
- [Python testing in Visual Studio Code](https://code.visualstudio.com/docs/python/testing)
- [Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)