# -*- coding: utf-8 -*-

from .common import currency, Accounts, c, isolation

from brownie import cccur, accounts, reverts


def test_pledge_overflow(Accounts, c):

    owner = Accounts[0]
    john = Accounts[1]

    owner.setAccountParams(john, True, 1, 3000, -1000)

    maximum = int("0x7" + "f" * 63, 16)
    owner.pledge(john, maximum)
    with reverts("dev: overflow or negative pledge"):
        owner.pledge(john, 1)
