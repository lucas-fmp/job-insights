from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents
    Parameters
    ----------
    path : str
        Full path to file
    Returns
    -------
    list
        List of rows as dicts
    """

    with open(path, encoding="utf-8") as file:
        data = csv.DictReader(file)
        return list(data)


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them
    Must call `read`
    Parameters
    ----------
    path : str
        Must be passed to `read`
    Returns
    -------
    list
        List of unique job types
    """

    list_of_dicts_of_jobs = read(path)
    list_of_job_types = []

    for job in list_of_dicts_of_jobs:
        if job["job_type"] not in list_of_job_types:
            if job["job_type"] != "":
                list_of_job_types.append(job["job_type"])

    return list_of_job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type
    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter
    Returns
    -------
    list
        List of jobs with provided job_type
    """

    filtered_jobs = []

    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs
