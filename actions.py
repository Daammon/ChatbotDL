# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class action_find_actor_movies(Action):

    def name(self) -> Text:
        print("got name")
        return "action_find_actor_movies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("gonna dispatch!!!!")
        facility = tracker.get_slot("actor")
        movie = "Die Hard"#Mock para ver si funciona
        #AQUÍ VA LA FUNCIÓN PARA ENCONTRAR LA PELÍCULA
        dispatcher.utter_message("This is the movie:{}".format(movie))

        return [SlotSet("movie", movie)]
