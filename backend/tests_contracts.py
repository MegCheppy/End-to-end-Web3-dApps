# This code tests the implementation of buildNFTcerts.py smart contract using pytest module.

from helpers import call_sandbox_command

def setup_module(module):
    """Ensure Algorand Sandbox is up prior to running tests from this module."""
    call_sandbox_command("up")


    from contracts import setup_bank_contract, setup_split_contract
from helpers import add_standalone_account


class TestSplitContract:
    """Class for testing the split smart contract."""

    def setup_method(self):
        """Create owner and receivers accounts before each test."""
        _, self.owner = add_standalone_account()
        _, self.receiver_1 = add_standalone_account()
        _, self.receiver_2 = add_standalone_account()

    def _create_split_contract(self, **kwargs):
        """Helper method for creating a split contract from pre-existing accounts

        and provided named arguments.
        """
        return setup_split_contract(
            owner=self.owner,
            receiver_1=self.receiver_1,
            receiver_2=self.receiver_2,
            **kwargs,
        )


class TestBankContract:
    """Class for testing the bank for account smart contract."""

    def setup_method(self):
        """Create receiver account before each test."""
        _, self.receiver = add_standalone_account()

    def _create_bank_contract(self, **kwargs):
        """Helper method for creating bank contract from pre-existing receiver

        and provided named arguments.
        """
        return setup_bank_contract(receiver=self.receiver, **kwargs)


class TestSplitContract:
    #
    def test_split_contract_uses_existing_accounts_when_they_are_provided(self):
        """Provided accounts should be used in the smart contract."""
        contract = self._create_split_contract()
        assert contract.owner == self.owner
        assert contract.receiver_1 == self.receiver_1
        assert contract.receiver_2 == self.receiver_2


class TestSplitContract:
    #
    def test_split_contract_creates_new_accounts(self):
        """Contract creation function `setup_split_contract` should create new accounts

        if existing are not provided to it.
        """
        contract = setup_split_contract()
        assert contract.owner != self.owner
        assert contract.receiver_1 != self.receiver_1
        assert contract.receiver_2 != self.receiver_2


class TestBankContract:
    #
    def test_bank_contract_creates_new_receiver(self):
        """Contract creation function `setup_bank_contract` should create new receiver

        if existing is not provided to it.
        """
        _, _, receiver = setup_bank_contract()
        assert receiver != self.receiver

    def test_bank_contract_uses_existing_receiver_when_it_is_provided(self):
        """Provided receiver should be used in the smart contract."""
        _, _, receiver = self._create_bank_contract()
        assert receiver == self.receiver


