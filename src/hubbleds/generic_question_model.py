from solara import Reactive
from pydantic import BaseModel, computed_field, Field
from typing import Union, Dict

from typing import Dict, Generic, TypeVar, Union, Type, ClassVar, cast, Dict, Any
from pydantic import BaseModel, Field
from abc import ABC, abstractmethod

from cosmicds.state import BaseState



# Type variable for generic models
T = TypeVar('T', bound='GenericQuestion')

class GenericQuestion(BaseState):
    """
    A generic base model for individual questions.
    """
    tag: str = ""
    
    def __getitem__(self, key):
        if hasattr(self, key):
            return getattr(self, key)
        else:
            raise KeyError(f"Question does not have attribute {key}")
    
    def update(self, **kwargs):
        """
        Update the attributes of the question with provided keyword arguments.
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise KeyError(f"Question does not have attribute {key}")

class GenericContainer(BaseState, Generic[T], ABC):
    """
    A generic container for managing a collection of questions.
    An abstract base class. Cannot be instantiated directly.
    """
    _item_attribute_name: str = "items" # the user must set this in the child class
    
    @property
    def items(self) -> Dict[str, T]:
        return getattr(self, self._item_attribute_name)
    
    
    def __getitem__(self, key) -> T:
        """ all accessing items via subscript: Container[tag] """
        item = self.items.get(key)
        if item is None:
            raise KeyError(f"__getitem__ Question with tag {key} does not exist")
        return item
    
    def __contains__(self, key) -> bool:
        """ implementing the 'in' operator: tag in Container"""
        return key in self.items
    
    def get(self, key, default = None) -> Union[T, None]:
        """ get the item with the given tag, if it exists """
        return self.items.get(key, default)

    
    def get_model_dump(self, key, default = None):
        item = self.items.get(key, None)
        if item is not None:
            return item.model_dump()
        return default
    
    
    def add_item(self, tag: str, item_class: Type[T]) -> T:
        """
        Add a new question to the container.
        Returns the newly created question.
        If question already exists, returns the question.
        """
        
        if tag in self.items:
            print(f"add_item:: Item with tag {tag} already exists")
            return self.items[tag]
        
        print(f"add_item:: Adding item with tag {tag}")
        self.items[tag] = item_class(tag = tag)
        return self.items[tag]
    
    def get_or_create_item(self, key, item_class: Type[T]) -> T:
        "  "
        item = self.items.get(key)
        if item is None:
            print(f"Creating item with tag {key} using get_or_create_item")
            return self.add_item(key, item_class)

        return item
    
    def update_item(self, tag: str, **kwargs):
        """
        Update an existing question in the container.
        """
        item = self.items.get(tag)
        if item is None:
            raise ValueError(f"Cannot update: Question with tag {tag} does not exist")
        
        print(f"Updating item with tag {tag}")
        item.update(**kwargs)
            
    @abstractmethod
    def add(self, tag: str) -> T:
        """"
        The child class should implement this method to add a new question with the given tag.
        
        Example::
        
        class MyContainer(GenericContainer[MyQuestion]):
            def add(self, tag: str):
                self.add_item(tag, MyQuestion)
        """
        return NotImplemented
    
    @abstractmethod
    def get_or_create(self, tag: str) -> T:
        """"
        The child class should implement this method to get or create a question with the given tag.
        
        Example::
        
        class MyContainer(GenericContainer[MyQuestion]):
            def get_or_create(self, tag: str):
                self.get_or_create_item(tag, MyQuestion)
        """
        return NotImplemented