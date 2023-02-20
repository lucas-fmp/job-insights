from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    list_of_dicts_of_jobs = read(path)
    list_industries = []

    for job in list_of_dicts_of_jobs:
        if job["industry"] not in list_industries:
            if job["industry"] != "":
                list_industries.append(job["industry"])

    return list_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_jobs = []

    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs.append(job)

    return filtered_jobs
