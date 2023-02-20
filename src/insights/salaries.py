from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs
    Must call `read`
    Parameters
    ----------
    path : str
        Must be passed to `read`
    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """

    list_of_dicts_of_jobs = read(path)
    max_salary = 0

    for job in list_of_dicts_of_jobs:
        if job["max_salary"].isdigit():
            if int(job["max_salary"]) > max_salary:
                max_salary = int(job["max_salary"])

    return max_salary


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs
    Must call `read`
    Parameters
    ----------
    path : str
        Must be passed to `read`
    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """

    list_of_dicts_of_jobs = read(path)
    min_salary = None

    for job in list_of_dicts_of_jobs:
        if job["min_salary"].isdigit():
            if min_salary is None or int(job["min_salary"]) < min_salary:
                min_salary = int(job["min_salary"])

    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job
    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job
    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise
    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError

    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)
    except (ValueError, TypeError):
        raise ValueError

    if min_salary > max_salary:
        raise ValueError

    return min_salary <= salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range
    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter
    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """

    filtered_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except (ValueError):
            pass

    return filtered_jobs
