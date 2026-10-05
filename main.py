from src.tools.tools import web_search, scrape_url
from src.pipeline.pipeline import run_research_pipeline

#result = web_search.invoke("latest news on AI")
#print(result)

#result = scrape_url.invoke("https://www.reddit.com/r/ArtificialInteligence/")
#print(result)

topic = "the impact of AI on the job market in 2026 and 2O27"

run_research_pipeline(topic)
