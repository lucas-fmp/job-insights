from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        data = csv.DictReader(file)
        return list(data)


def get_unique_job_types(path: str) -> List[str]:
    list_of_dicts_of_jobs = read(path)
    list_of_job_types = []

    for job in list_of_dicts_of_jobs:
        if job["job_type"] not in list_of_job_types:
            if job["job_type"] != "":
                list_of_job_types.append(job["job_type"])

    return list_of_job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_jobs = []

    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs
