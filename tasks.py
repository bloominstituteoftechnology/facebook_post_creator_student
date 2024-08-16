from crewai import Task
from tools import scrape_tool, url
from agents import social_media_content_creator, social_media_researcher, tag_developer


scrape_article = Task(
    description=("Scrape the {url}."
    "Get the relevant information and content from the article included."),
    expected_output= "A one paragraph summary about the article in the {url}.",
    tools = [scrape_tool],
    agent = social_media_researcher
)


write_blurb = Task(
    description=("Create content from the article summary."),
    expected_output= "A one sentence blurb that can be posted to Facebook from the article at {url}.",
    tools = [scrape_tool],
    async_execution= False,
    agent = social_media_content_creator,
    output_file = 'facebook_blurb.md'
)



tag_writer = Task(
    description=("Write tags and relevant username link based off the article at {url}."),
    expected_output= "Tags and usernames that can be included in Facebook posts.",
    tools = [scrape_tool],
    async_execution= False,
    agent = tag_developer,
    output_file= "new-facebook-post.md"
)