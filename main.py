import os

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from dotenv import load_dotenv

load_dotenv()
service_name: str = os.environ.get("SERVICE_NAME")
index_name: str = os.environ.get("INDEX_NAME")
key: str = os.environ.get("ADMIN_KEY")
# Generate the Endpoint based on service name
endpoint: str = f"https://{service_name}.search.windows.net/"


class QueryResults:
    """
    Class to interact with the Azure SearchClient and query on attached documents and index definition.
    """
    def __init__(self, search_text: str):
        """
        :param search_text: Text to be seached.
        """
        # SearchClient instance
        self.search_client = SearchClient(endpoint, index_name, AzureKeyCredential(key))
        self.search_text = search_text

    def get_search_results(self):
        """
        Searches for the given query and provides the results accordingly.
        include_total_count is used to get the query count using .get_count method.
        :return: Query Results
        """
        try:
            query: str = self.search_text
            return self.search_client.search(query, include_total_count=True)
        except Exception as error:
            print(f"Exception has occurred. {error}")

    def get_dataset_length(self):
        """
        Get the length of dataset
        :return: Length
        """
        return self.search_client.get_document_count()


if __name__ == "__main__":
    # Get the text from user
    if text_to_be_searched := input("Enter a value to be searched based on Department/Gender/JobRole : "):
        query_results_obj = QueryResults(search_text=text_to_be_searched)
        print(f"The length of dataset is {query_results_obj.get_dataset_length()}")
        query_results = query_results_obj.get_search_results()
        # Get the length of whole dataset
        query_results_length: int = query_results.get_count()
        if query_results_length > 0:
            # Get the length of search results
            print(f"Found {query_results_length} results for {text_to_be_searched}.")
            for result in query_results:
                print(f"JobRole : {result['JobRole']}, "
                      f"Department : {result['Department']}, "
                      f"Age : {result['Age']}, "
                      f"Gender : {result['Gender']}")
        else:
            print(f"No results found for {text_to_be_searched}")
    else:
        print("Please provide a value to be searched.")
