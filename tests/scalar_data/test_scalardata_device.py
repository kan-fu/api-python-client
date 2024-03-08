import pytest
import requests


@pytest.fixture
def params_multiple_pages(params_device):
    # rowLimit should be less than the total number of rows.
    return params_device | {"rowLimit": 25}


def test_invalid_param_value(requester, params_device):
    params_invalid_param_value = params_device | {"deviceCode": "XYZ123"}
    with pytest.raises(requests.HTTPError, match=r"API Error 127"):
        requester.getDirectByDevice(params_invalid_param_value)


def test_invalid_param_name(requester, params_device):
    params_invalid_param_name = params_device | {"deviceCodes": "BPR-Folger-59"}
    with pytest.raises(requests.HTTPError, match=r"API Error 129"):
        requester.getDirectByDevice(params_invalid_param_name)


def test_no_data(requester, params_device):
    params_no_data = params_device | {"dateFrom": "2000-01-01", "dateTo": "2000-01-02"}
    data = requester.getDirectByDevice(params_no_data)

    assert data["sensorData"] is None


def test_valid_params_one_page(requester, params_device, params_multiple_pages):
    data = requester.getDirectByDevice(params_device)
    data_all_pages = requester.getDirectByDevice(params_multiple_pages, allPages=True)

    assert (
        _get_row_num(data) > params_multiple_pages["rowLimit"]
    ), "Test should return at least `rowLimit` rows for each sensor."

    assert data["next"] is None, "Test should return only one page."

    assert (
        data_all_pages["sensorData"][0]["data"] == data["sensorData"][0]["data"]
    ), "Test should concatenate rows for all pages."

    assert data_all_pages["next"] is None, "Test should return only one page."


def test_valid_params_multiple_pages(requester, params_multiple_pages):
    data = requester.getDirectByDevice(params_multiple_pages)

    assert (
        _get_row_num(data) == params_multiple_pages["rowLimit"]
    ), "Test should only return `rowLimit` rows for each sensor."

    assert data["next"] is not None, "Test should return multiple pages."


def _get_row_num(data):
    return len(data["sensorData"][0]["data"]["values"])
