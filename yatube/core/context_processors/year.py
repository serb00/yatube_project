from datetime import datetime


def getCurrentYear(request) -> int:
    '''context processor which returns current year
    \nto use in footer template'''
    return {
        "year": datetime.now().year
    }
