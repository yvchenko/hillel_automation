import pytest

from script_0 import OurBilling


@pytest.mark.parametrize("order_1, order_2", [(1, 2), (2, 3), (4, 4), (1, 5)])
def test_init(order_1, order_2):
    a = OurBilling(order_1, 3, 150.0)
    b = OurBilling(order_2, 4, 160)
    assert a.order_number != b.order_number


def test_price():
    c = OurBilling(33, 4, 50)
    assert c.price_per_item() == 12.5



