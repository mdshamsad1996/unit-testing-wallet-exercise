"""Testing of wallet Module"""

import pytest
from wallet import Wallet, InsufficientAmount, NegativeAmount


@pytest.fixture
def my_wallet_instance():
    """creating wallet object with empty values"""
    return Wallet()


@pytest.fixture
def my_wallet_instance():
    """creating wallet object with  values"""
    return Wallet()


def test_intitial_amount(my_wallet_instance):
    """Test for intial amount"""
    assert my_wallet_instance.value == 0


@pytest.mark.parametrize("pay_out_amt", [190])
def test_wallet_spend_raises_exception_on_insufficient_amount(my_wallet_instance, pay_out_amt):
    """Test for insuffiecient amount exception"""
    with pytest.raises(InsufficientAmount):
        my_wallet_instance.spend(pay_out_amt)


@pytest.mark.parametrize("negative_amt", [-190])
def test_wallet_add_raises_exception_on_negative_amount(my_wallet_instance, negative_amt):
    """Test for adding negative amount"""
    with pytest.raises(NegativeAmount):
        my_wallet_instance.add(negative_amt)


@pytest.mark.parametrize("add_cash, expected",[(10,10),(120, 120)])
def test_add_method(my_wallet_instance, add_cash, expected):
    """Test for add method"""
    my_wallet_instance.add(add_cash)
    assert my_wallet_instance.value == expected


@pytest.mark.parametrize("expected_wallet",[{'Wallet value': 0, 'Currency':'GBP'}])
def test_show_wallet_method(my_wallet_instance, expected_wallet):
    """Test for show wallet method"""
    actual_wallet = my_wallet_instance.show_wallet()
    assert actual_wallet == expected_wallet


@pytest.mark.parametrize("add_cash, pay_out, expected",[(10, 5, 5),(50, 20, 30)])
def test_spend(my_wallet_instance, add_cash, pay_out, expected):
    """Test for transaction"""
    my_wallet_instance.add(add_cash)
    my_wallet_instance.spend(pay_out)
    assert my_wallet_instance.value == expected


@pytest.mark.parametrize("add_cash, pay_out, expected",[(10, 5, 5),(50, 20, 30)])
def test_transaction(my_wallet_instance, add_cash, pay_out, expected):
    """Test for transaction"""
    my_wallet_instance.add(add_cash)
    my_wallet_instance.spend(pay_out)
    assert my_wallet_instance.value == expected
