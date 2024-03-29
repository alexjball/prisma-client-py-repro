import sys

try:
    from prisma_repro.client import Prisma

    print("Prisma imported successfully!", Prisma)
except Exception as e:
    print("Failed to import Prisma:", e)
    sys.exit(1)
