from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor
from langgraph.checkpoint.memory import InMemorySaver
from tools import *

prompt_=(
    "You are an AI Team Supervisor, managing two specialized agents:a data_loader_agent and a research_agent."
    "Your primary goal is to accurately and efficiently answer user queries by leveraging the strengths of these agents and your own general knowledge."
    "Agent Capabilities:"
    "data_loader_agent:"
    "Loads Content: youtube_transcripts, web_page_loader, load_file, load_directory"
    "File & Directory Management: get_file_info, list_directory_contents, list_directory_recursive, search_files_by_pattern"
    "research_agent:"
    "Web Search:search_tool(topic),deep_search(topic) (returns search results including title and URL for relevant webpages)"
    "Your Operational Protocol:"
    "Analyze the User Query: Carefully understand the user's request and identify the core task(s)."
    "Determine Required Resources: Based on the query, decide which agent(s) or your internal knowledge are best suited to provide the necessary information."
   " Data Loading/Access: Use data_loader_agent for tasks involving local files, directories, web pages, or YouTube transcripts."
    "Information Gathering/Web Search: Use research_agent for general web searches and retrieving information from the internet."
    "Basic Math/General Questions: Use your own knowledge for straightforward calculations or common information."
   " Execute Actions: Deploy the appropriate agent(s) with precise instructions or answer directly using your knowledge."
   "Synthesize and Structure: Combine all gathered information into a comprehensive, well-organized, and clear final response." 
    "Include relevant URLs from the research_agent when applicable."
    )

checkpointer=InMemorySaver()

data_loader_agent=create_react_agent(llm,tools=[youtube_transcript,web_page_loader,data_loader],name='data_loader',prompt="your are data_loader_agent can load youtube transcripts,get_file_info,list_directory_recursive,list_directory_contents,load_file,load_directory,search_files_by_pattern and load web page content")
research_agent=create_react_agent(llm,tools=[search_tool,deep_search],name='researcher',prompt="your are a research agent that can search querys using duckduckgo")

app=create_supervisor([data_loader_agent,research_agent],
                      model=llm,
                      prompt=prompt_,
                      output_mode="last_message"
                      )

super_visor=app.compile(checkpointer=checkpointer)