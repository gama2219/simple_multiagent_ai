from langchain_core.tools import tool
from langchain_community.document_loaders import YoutubeLoader,WikipediaLoader
from ai_data_science_team.agents import DataLoaderToolsAgent
from langchain_community.tools import DuckDuckGoSearchRun,DuckDuckGoSearchResults
from langchain_unstructured import UnstructuredLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os


load_dotenv()
google_api_key=os.getenv("GOOGLE_API_KEY")


llm =ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=0,google_api_key=google_api_key)


#Add your own agentic  tools
@tool
def data_loader(instruction:str)->dict:
  """performs data loading task by taking instruction as argument :
  Loads all recognized tabular files in a directory.
  loads a file based on its extension.
  Lists all files and folders in the specified directory.
  Recursively lists all files and folders within the specified directory.
  Retrieves metadata (size, modification time, etc.) about a file.
  Searches for files that match a given wildcard pattern, optionally in subdirectories
  """

  data_loader_agent = DataLoaderToolsAgent(
    llm,
    invoke_react_agent_kwargs={"recursion_limit": 10}
)
  ai_res=data_loader_agent.invoke({'user_instructions':instruction})
  arti_fact=data_loader_agent.get_artifacts()
  #create response
  response={
      "ai_response":ai_res,
      "ai_artifact":arti_fact
  }

  return response


@tool
def youtube_transcript(url: str) -> str:
  """take a youtube url and return the transcript as a string"""
  loader=YoutubeLoader.from_youtube_url(url,add_video_info=False,)
  transcript=loader.load()
  return transcript[0].page_content

@tool
def search_tool(topic:str)->str:
  """perform search using duckduckgo and return response"""
  search = DuckDuckGoSearchRun()
  response=search.invoke(topic)
  return response

@tool
def deep_search(topic:str)->list:
  """perform deep search using duckduckgo and return response in list of dictionary
      Args:
        topic: The search topic.
        Returns:
        A list of dictionaries containing the search results including the url link of the webpage and the title of the webpage.
  argument
  """
  search = DuckDuckGoSearchResults(output_format="list")
  response=search.invoke(topic)
  return response

@tool
def web_page_loader(url:str)->str:
  """loads web pages from url and returns the content of the web page in string format
  Args:
    url: The URL of the web page to load.
    Returns:
    The content of the web page as a string.
  """
  main_doc=[]
  loader = UnstructuredLoader(web_url=url)
  doc=loader.load()
 
  for doc_ in doc:
    main_doc.append(doc_.page_content)

  result = " \n".join(main_doc)
  return result
