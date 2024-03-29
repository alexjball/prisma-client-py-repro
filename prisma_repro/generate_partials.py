import os

if os.getenv("REPRODUCE"):
    from prisma_repro.client import models
else:
    from .generate_partials_patch import models

models.user.create_partial("test_user", include={"id", "name"})
