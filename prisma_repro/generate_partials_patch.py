import os
from pathlib import Path

if os.getenv("DEBUG_PARTIALS"):
    # The partial generator runs in a separate process from the cli, so we attach to it here
    import debugpy

    debugpy.listen(5678)
    print("Waiting for Out debugger attach on 127.0.0.1:5678")
    debugpy.wait_for_client()
    debugpy.breakpoint()

# Create partials.py file to allow importing generated client package.
# Requires knowing the relative path to the generated client directory.
partials_file = Path(__file__).parent.joinpath("client/partials.py")
partials_file.touch()

# replace partial_models_ctx of the non-site-package client with the one from
# the site-package client.
from prisma.generator.generator import (  # noqa: E402
    partial_models_ctx as pkg_partial_models_ctx,
)
from prisma_repro.client import models  # noqa: E402

models.partial_models_ctx = pkg_partial_models_ctx
