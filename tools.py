from crewai_tools import ScrapeWebsiteTool

url = input("Include URL here: ")
scrape_tool = ScrapeWebsiteTool(website_url= url)