import importlib

def test_requests_and_reportlab_importable():
    assert importlib.import_module("requests")
    assert importlib.import_module("reportlab")
