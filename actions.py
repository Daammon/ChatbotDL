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
from scrapingFunctions import *

class action_find_actor_movies(Action):

    def name(self) -> Text:
        print("got name")
        return "action_find_actor_movies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("gonna dispatch!!!!")
        actor = tracker.get_slot("actor")
        movie = Find_all_movies_of_actor(actor[0])

        dispatcher.utter_message("This is the movie:{}".format(movie))

        return [SlotSet("movie", movie)]

class action_find_movie_release_date(Action):

    def name(self) -> Text:
        print("got name")
        return "action_find_movie_release_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        movie = tracker.get_slot("movie")
        releaseDate = Find_year_from_movie(movie)
        dispatcher.utter_message("This is the release date:{}".format(releaseDate))

        return [SlotSet("releaseDate", releaseDate)]

class action_find_actors_coincidence_in_movies(Action):

    def name(self) -> Text:
        print("got name")
        return "action_find_actors_coincidence_in_movies"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        actorsList = tracker.get_slot("actor")
        movie = Find_common_movie_of_actors([actorsList[0], actorsList[1]])
        dispatcher.utter_message("This is the movie where{} and {} coincide: {}".format(actorsList[0], actorsList[1], movie))

        return [SlotSet("movie", movie)]

class action_find_movie_rankings_by_genre(Action):

    def name(self) -> Text:
        print("got name")
        return "action_find_movie_rankings_by_genre"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        genre = tracker.get_slot("genre")
        rankingByGenre = Find_best_movie_by_genre(genre)
        dispatcher.utter_message("This is the ranking of the top {} movies: {}".format(genre, rankingByGenre))

        return [SlotSet("ranking", rankingByGenre)]

class action_find_movie_rankings_by_actor(Action):

    def name(self) -> Text:
        print("got name")
        return "action_find_movie_rankings_by_actor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        actor = tracker.get_slot("actor")
        rankingByActor = Find_best_movies_actor(actor[0])
        dispatcher.utter_message("This is the ranking of the top {} movies: {}".format(actor, rankingByActor))

        return [SlotSet("ranking", rankingByActor)]