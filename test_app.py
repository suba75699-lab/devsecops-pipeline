def test_check_status_normal():
    from app import check_status
    assert check_status(25) == "Normal"


def test_check_status_high():
    from app import check_status
    assert check_status(75) == "High"
