# technical_reports.py

TECHNICAL_REPORTS = [
    {
        "title": "Technical Report on Topic 1",
        "author": "Author 1",
        "desc": "Description of Technical Report 1",
        "date": "2022-01-01",
        "file": "technical_report_1.pdf"
    },
    {
        "title": "Technical Report on Topic 2",
        "author": "Author 2",
        "desc": "Description of Technical Report 2",
        "date": "2021-12-15",
        "file": "technical_report_2.pdf"
    },
    {
        "title": "Technical Report on Topic 3",
        "author": "Author 3",
        "desc": "Description of Technical Report 3",
        "date": "2021-11-01",
        "file": "technical_report_3.pdf"
    }
]

def get_technical_reports():
    """
    Get a list of all technical reports

    Returns:
        A list of dictionaries, each containing information about a technical report

    """
    return TECHNICAL_REPORTS

def get_technical_report(report_index):
    """
    Get a specific technical report

    Args:
        report_index (int): The index of the technical report in the `TECHNICAL_REPORTS` list

    Returns:
        A dictionary containing information about the technical report

    Raises:
        IndexError: If `report_index` is out of range

    """
    if report_index < 0 or report_index >= len(TECHNICAL_REPORTS):
        raise IndexError(f"Invalid report index: {report_index}")
    return TECHNICAL_REPORTS[report_index]

def get_technical_report_file_path(report_index):
    """
    Get the file path of a technical report

    Args:
        report_index (int): The index of the technical report in the `TECHNICAL_REPORTS` list

    Returns:
        A string representing the file path of the technical report

    Raises:
        IndexError: If `report_index` is out of range

    """
    if report_index < 0 or report_index >= len(TECHNICAL_REPORTS):
        raise IndexError(f"Invalid report index: {report_index}")
    return f"resources/technical_reports/{TECHNICAL_REPORTS[report_index]['file']}"
