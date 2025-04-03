# Template MVC Tkinter Python app

It seems to be a bit fiddly to get python TKinter app all wired up to work and build when using uv python environment manager.

Check that build and packaging is working.

```bash
uv build
uv pip install -e .
my-tkinter-app.exe
```

To install a local package using uv, follow these steps:

1 - Navigate to the directory of your local package.

Use the command: 
`python -m uv pip install --system --prerelease=allow -r pyproject.toml` to install all dependencies described in your pyproject.toml file. 
Alternatively

For editable install, you can use: 
`uv pip install -e .`
to install the package in editable mode. 

If you have a built package, you can install it locally using:

`pip install dist/my_package-0.1.0-py3-none-any.whl`

Added to develop branch

