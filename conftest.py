from py.xml import html
import pytest

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(0, html.th('Chapter'))
    cells.pop()

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(0, html.td(report.chapter))
    cells.pop()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    chapIndex = report.nodeid.find("/")
    chapString = report.nodeid[:chapIndex]
    report.chapter = chapString
