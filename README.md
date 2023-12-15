### Azure AI Search

Azure AI Search is an Azure resource used for adding a full text search experience.

**Search Service** : search-query-csv

**Resource Group** : Search_CSV_Data

**Index name** : azureblob-index

**Document_Key** : AzureSearch_DocumentKey 

**Searchable Fields** : Department, Gender, JobRole

<br>

### Project Setup
```python
pip install -r requirements.txt
```

### Configure Azure Client 
```python
SERVICE_NAME=<AZURE_AI_SEARCH_SERVICE_NAME>
```
Name of the Azure AI Search Service.

```python
INDEX_NAME=<AZURE_AI_INDEX_NAME>
```
Name of the Azure AI Search Service Index after importing the data.

```python
ADMIN_KEY=<PRIMARY_ADMIN_KEY>
```
Primary Admin Key value 

_**Replace** all 3 values in with **original values** in **env.py** file._

### Run Project
```python
python main.py
```

When you run the above command, it will task you to enter a text to be searched. The results will be provided on the basis of text you enter.

<br>

**_NOTE_** : _Here **[IBM-Dataset.csv](https://www.kaggle.com/datasets/rohitsahoo/employee)** test data file is used as reference for seraching the data._
