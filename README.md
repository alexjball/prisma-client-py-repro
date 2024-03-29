Reproduce / patch https://github.com/RobertCraigie/prisma-client-py/issues/50

# Setup

Install poetry and poethepoet, or refer to the pyproject.toml file for commands/dependencies.

```
poetry install
```

To get back to a clean state after generating models, run `poe clean`

# Generate client

```bash
poe generate
```

produces the client at `prisma_repro/client` using the `generate_partials_patch` module

Import the prisma module with

```bash
poe run
```

# Reproduce original issues

```
poe reproduce
```

Imports the models directly and reproduces the error.

# Fixes

1. The `partials.py` file needs to exist in order for the partial generator to import the partially-generated client package. This is because when the partial generator executes, the `client` and `fields` modules have been generated, but not the `partials` module ([ref](https://github.com/RobertCraigie/prisma-client-py/blob/main/src/prisma/__init__.py#L27-L34)). `from . import x` produces an `ImportError`, not a `ModuleNotFoundError` as produced by a missing `from .client import *`, so the catch block doesn't handle this case.
2. The client package has its own copy of `partial_models_ctx` and generates partials to that, so the site-packages prisma generator needs to pull from the same one. From within the partial generator, we can patch the context on the models module so they are generated to the correct location.