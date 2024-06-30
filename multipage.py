import streamlit as st

class MultiPage: 
    def __init__(self) -> None:
        """Constructor class to store variables."""

        self.pages = []
    
    def add_page(self, title, func) -> None: 
        """Class Method to Add pages to the project
        Args:
            title ([str]): The title of page which we are adding to the list of apps 
            func: Python