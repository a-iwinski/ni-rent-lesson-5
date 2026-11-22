import pytest
from src.manager import Manager
from src.models import Parameters


def test_apartment_does_not_exist():
    manager = Manager(Parameters())
    with pytest.raises(ValueError):
        manager.get_apartment_costs('apart-nonexistent', 2025, 1)


def test_no_bills_in_month():
    manager = Manager(Parameters())
    assert manager.get_apartment_costs('apart-polanka', 2025, 2) == 0.0


def test_bills_in_month():
    manager = Manager(Parameters())
    assert manager.get_apartment_costs('apart-polanka', 2025, 1) == 910.0