import abc

class ProviderInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_summary') and 
                callable(subclass.get_summary) and 
                hasattr(subclass, 'get_blocks') and 
                callable(subclass.get_blocks) and 
                hasattr(subclass, 'get_block_by_id') and 
                callable(subclass.get_block_by_id) and
                hasattr(subclass, 'get_transactions') and 
                callable(subclass.get_transactions) and 
                hasattr(subclass, 'get_transaction_by_id') and 
                callable(subclass.get_transaction_by_id)and 
                callable(subclass.get_address_by_id) and 
                hasattr(subclass, 'get_address_by_id') or 
                NotImplemented)

    @abc.abstractmethod
    def get_summary(self):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_blocks(self, num_blocks: int):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_block_by_id(self, block_id: str):
        """Extract text from the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_transactions(self, num_tx: int):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_transaction_by_id(self, tx_id: str):
        """Extract text from the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_address_details_by_id(self, address_id):
        """Extract text from the data set"""
        raise NotImplementedError