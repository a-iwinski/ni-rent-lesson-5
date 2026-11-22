from src.manager import Manager
from src.models import Parameters, Tenant


def test_settlements_with_three_tenants():
    manager = Manager(Parameters())
    apartment_settlement = manager.create_apartment_settlement('apart-polanka', 2025, 1)
    settlements = manager.create_tenant_settlements(apartment_settlement)
    assert len(settlements) == 3
    assert settlements[0].apartment_settlement == 'apart-polanka'
    assert settlements[0].month == 1
    assert settlements[0].year == 2025
    for s in settlements:
        assert s.rent_pln == round(760.0 / 3, 2)
        assert s.bills_pln == 50.0
        assert s.total_due_pln == round(910.0 / 3, 2)
    assert {s.tenant for s in settlements} == {'tenant-1', 'tenant-2', 'tenant-3'}


def test_settlements_with_one_tenant():
    manager = Manager(Parameters())
    del manager.tenants['tenant-2']
    del manager.tenants['tenant-3']
    apartment_settlement = manager.create_apartment_settlement('apart-polanka', 2025, 1)
    settlements = manager.create_tenant_settlements(apartment_settlement)
    assert len(settlements) == 1
    assert settlements[0].tenant == 'tenant-1'
    assert settlements[0].rent_pln == 760.0
    assert settlements[0].bills_pln == 150.0
    assert settlements[0].total_due_pln == 910.0


def test_settlements_with_two_tenants():
    manager = Manager(Parameters())
    del manager.tenants['tenant-3']
    apartment_settlement = manager.create_apartment_settlement('apart-polanka', 2025, 1)
    settlements = manager.create_tenant_settlements(apartment_settlement)
    assert len(settlements) == 2
    for s in settlements:
        assert s.rent_pln == 380.0
        assert s.bills_pln == 75.0
        assert s.total_due_pln == 455.0


def test_settlements_with_no_tenants():
    manager = Manager(Parameters())
    manager.tenants.clear()
    apartment_settlement = manager.create_apartment_settlement('apart-polanka', 2025, 1)
    assert manager.create_tenant_settlements(apartment_settlement) == []