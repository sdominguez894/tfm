import abc

class ValidatorInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'is_block') and 
                callable(subclass.is_block) and 
                hasattr(subclass, 'is_address') and 
                callable(subclass.is_address) or
                hasattr(subclass, 'is_transaction') and 
                callable(subclass.is_transaction) and  
                NotImplemented)

    @abc.abstractmethod
    def is_block(self, text: str) -> bool:
        """Checks whether the text matches a block number signature"""
        raise NotImplementedError

    @abc.abstractmethod
    def is_address(self, text: str) -> bool:
        """Checks whether the text matches an address signature"""
        raise NotImplementedError

    @abc.abstractmethod
    def is_transaction(self, text: str) -> bool:
        """Checks whether the text matches a transaction signature"""
        raise NotImplementedError