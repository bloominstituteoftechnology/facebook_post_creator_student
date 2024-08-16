from crewai import Agent
from dotenv import load_dotenv
from tools import scrape_tool

load_dotenv()

social_media_researcher = Agent(
    role="Social Media Researcher",
    goal="Read the scraped content from a website and provide a summary of the article, identifying the theaters involved in the review.",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in reading scraped content to deliver to the Social Media Content Creator."
    ),
    tools=[scrape_tool],
    allow_delegation=True,
)


social_media_content_creator = Agent(
    role="Social Media Content Creator",
    goal="Create blurbs that can be posted on Facebook about the article researched by the Social Media Researcher.",
    verbose=True,
    memory=True,
    backstory=("Creates excellent content for social media."),
    tools=[scrape_tool],
    allow_delegation=True,
)

tag_developer = Agent(
    role="Social Media User and Tag",
    goal="Using the content from the article, creates appropriate tags and names which users should be tagged.",
    verbose=True,
    memory=True,
    backstory=("Great knowing which users need to be tagged to increase visibility."),
    tools=[scrape_tool],
    allow_delegation=True,
)

manager = Agent(
    role="Project Manager",
    goal="Manage the crew to create social content that includes facebook blurb and user tags.",
    backstory="You're an experienced project manager who has worked extensivley in social media. ",
)
