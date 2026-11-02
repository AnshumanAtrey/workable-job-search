"""Workable Job Search: the shared job engine (github.com/AnshumanAtrey/ats-jobs-engine) on Workable."""
import asyncio

from ats_jobs.engine import main

if __name__ == '__main__':
    asyncio.run(main('workable'))
