# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import imp
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .products import fetchProducts


class ActionSearchForProducts(Action):

    def name(self) -> Text:
        return "action_search_for_products"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        results = fetchProducts(tracker.get_slot("product"));

        buttons = []
        if(len(results)==0):
            dispatcher.utter_message("Sorry, no mathcing products found");
            return [];
        
        for product in results:
            payload = ""
            buttons.append({"title": "{}".format(product.name),"payload":payload});

        dispatcher.utter_button_message("Click on the product to add to cart",buttons)

        return []


