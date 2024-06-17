
# ==== Free Response State ====

import dataclasses
from solara import Reactive
from hubbleds.decorators import computed_property

from typing import Union, Dict


@dataclasses.dataclass
class FreeResponse:
    tag: str = dataclasses.field(init=True)
    _response: str = dataclasses.field(default = "")
    _initialized: bool = dataclasses.field(default = True)
    
    def update(self, response: str = ''):
        # self._response.set(response)
        self._response = response
    
    def toJsonSerializable(self):
        """Convert FreeResponse to a JSON-serializable dictionary."""
        return {
            'tag': self.tag,
            'response': self._response,
            'initialized': self._initialized
        }
    
    def __repr__(self):
        return f"FreeResponse({self.toJsonSerializable()})"
    
    @computed_property
    def completed(self):
        return self._response != ""
    
    
@dataclasses.dataclass
class FreeResponseDict:
    responses: Dict[str, FreeResponse] = dataclasses.field(default_factory = dict)
    
    def __repr__(self) -> str:
        formatted_responses = {tag: response.toJsonSerializable() for tag, response in self.responses.items()}
        return f"FreeResponseDict({formatted_responses})"
    
    def add_free_response_question(self, tag):
        """Add a new free response question with the given tag."""
        if tag in self.responses:
            raise ValueError(f"Question with tag {tag} already exists")
        
        print(f"Adding free response question with tag {tag}")
        old_responses = self.responses
        old_responses[tag] = FreeResponse(tag)
        # self.responses.set(old_responses)

            
    
    def update_free_response_question(self, tag: str, response: str):
        if tag not in self.responses:
            raise ValueError(f"Question with tag {tag} does not exist")
        else:
            old_responses = self.responses
            # calling update should cause a render as it sets a new value
            old_responses[tag].update(response = response)
            
            # We don't actually need to set the responses, as the FreeResponse contained
            # is updated in place & we don't need to trigger anything
            # self.responses.set(old_responses)


# Free Response Action Handlers  

def initialize_free_response(free_responses: Union[FreeResponseDict, Reactive[FreeResponseDict]], tag: str):
    """
    Initializes the free response feature by adding a free response question to the given `free_responses` object.
    """
    print("initializing free response", tag)
    if isinstance(free_responses, Reactive):
        free_responses = free_responses.value
    free_responses.add_free_response_question(tag)


def get_free_response(free_responses: Union[FreeResponseDict, Reactive[FreeResponseDict]], tag: str) -> Dict[str, Union[str, bool]]:
    """
    `get_free_response` 
    Retrieves the free response associated with the given tag from the free_responses dictionary.
    Will create the corresponding free response question if it does not exist.

    Parameters
    ----------
    free_responses : FreeResponseDict | Reactive[FreeResponseDict]
        The free response dictionary or its reactive wrapper.
    tag : str
        The tag associated with the free response question.

    Returns
    -------
    dictionary
        {'tag': str, 'response': str, 'initialized': bool}
    """    

    print("getting free response", tag)
    if isinstance(free_responses, Reactive):
        free_responses = free_responses.value
    
    if tag not in free_responses.responses:
        print("Need to create it now!")
        free_responses.add_free_response_question(tag)
        
    return free_responses.responses[tag].toJsonSerializable()
    
    
def update_free_response(free_responses: Union[FreeResponseDict, Reactive[FreeResponseDict]], tag: str, response: str):
    """
    Update the free response for a given tag.

    Parameters
    ----------
    free_responses : FreeResponseDict | Reactive[FreeResponseDict]
        The free response dictionary or its reactive wrapper.
    tag : str
        The tag of the free response question to update.
    response : str
        The new response to set.
    """
    
    print("updating free response", tag, response)
    if isinstance(free_responses, Reactive):
        free_responses = free_responses.value
    
    if tag not in free_responses.responses:
        raise ValueError(f"Free response question with tag {tag} does not exist")
    
    # this will trigger a render from within the FreeResponse class
    free_responses.update_free_response_question(tag, response)

        
    
