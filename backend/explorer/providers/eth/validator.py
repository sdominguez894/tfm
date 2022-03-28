from explorer.providers.validator import ValidatorInterface
import re

class EthValidator(ValidatorInterface):

    blockRegex = r"^[0-9]{1,20}$"
    addressRegex = r"^0x[a-zA-Z0-9]{40}$"
    transactionRegex = r"^0x[a-z0-9]{64}$"


    def is_block(self, text: str) -> bool:
        """Checks whether the text matches an ETH block number signature"""
        return re.match(self.blockRegex, text)

    def is_address(self, text: str) -> bool:
        """Checks whether the text matches an ETH address signature"""
        return re.match(self.addressRegex, text)

    def is_transaction(self, text: str) -> bool:
        """Checks whether the text matches an ETH block transaction signature"""        
        return re.match(self.transactionRegex, text)
