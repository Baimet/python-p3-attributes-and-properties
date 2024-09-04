#!/usr/bin/env python3

class Person:
    APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

    def __init__(self, name="Person", job="Admin"):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()  # Convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")
            return  # Exit the constructor if the name is invalid

        if job in self.APPROVED_JOBS:
            print(f"Setting job to {job}.")
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            print(f"Setting name to {name.title()}.")
            self._name = name.title()  # Convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in self.APPROVED_JOBS:
            print(f"Setting job to {job}.")
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)

