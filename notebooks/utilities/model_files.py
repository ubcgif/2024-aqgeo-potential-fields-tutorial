import glob
from pathlib import Path
import datetime


def get_latest_model_files(path: str | Path) -> list[Path]:
    """
    Return model filenames for the latest date
    """
    # Get dates available in output directory
    dates = get_dates_of_model_files(path)
    # Get the last date
    last_date = max(dates)
    # Get the list of the files corresponding to that date
    return get_model_files(path, last_date)


def get_model_files(path: str | Path, date: datetime.datetime) -> list[Path]:
    """
    Return model filenames for a specific date
    """
    date_str = date.strftime("%Y-%m-%d-%H-%M")
    model_files = [
        Path(fname) for fname in glob.glob(str(path) + "/**.npy") if date_str in fname
    ]
    model_files.sort()
    return model_files


def get_dates_of_model_files(path: str | Path) -> list[datetime.datetime]:
    """
    Return a list with the dates of inversion model files in the given dir
    """
    # Convert path to string
    path = str(path)
    dates = []
    for fname in glob.glob(path + "/**.npy"):
        date = _get_date_of_single_model_file(fname)
        if date not in dates:
            dates.append(date)
    return dates


def _get_date_of_single_model_file(fname: str) -> datetime.datetime:
    """
    Return the date of a given inversion fname
    """
    fname = fname.split("/")[-1].replace(".npy", "")
    year, month, day, hour, mins = [int(v) for v in fname.split("-")[-5:]]
    return datetime.datetime(year=year, month=month, day=day, hour=hour, minute=mins)
