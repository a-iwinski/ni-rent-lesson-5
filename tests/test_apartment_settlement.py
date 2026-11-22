from src.manager import Manager
from src.models import Parameters


def test_settlement_with_bills():
    manager = Manager(Parameters())
    settlement = manager.create_apartment_settlement('apart-polanka', 2025, 1)
    assert settlement.apartment == 'apart-polanka'
    assert settlement.year == 2025
    assert settlement.month == 1
    assert settlement.total_rent_pln == 760.0
    assert settlement.total_bills_pln == 150.0
    assert settlement.total_due_pln == 910.0


def test_settlement_without_bills():
    manager = Manager(Parameters())
    settlement = manager.create_apartment_settlement('apart-polanka', 2025, 2)
    assert settlement.apartment == 'apart-polanka'
    assert settlement.year == 2025
    assert settlement.month == 2
    assert settlement.total_rent_pln == 0.0
    assert settlement.total_bills_pln == 0.0
    assert settlement.total_due_pln == 0.0


def test_settlement_apartment_does_not_exist():
    manager = Manager(Parameters())
    assert manager.create_apartment_settlement('apart-nonexistent', 2025, 1) is None