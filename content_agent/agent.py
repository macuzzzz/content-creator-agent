from google.adk.agents.llm_agent import Agent

producer_agent = Agent(
    model='gemini-2.5-flash',
    name='podcast_support_agent',
    description='A helpful content producer that searches for viral topics online or create new topics based on sponsored products.',
    instruction="""You are a professional content producer. 
    
    When helping User:
    1. Be straightforward and direct
    2. Find viral content online based on genre, views, interactions, subscribers gained.
    3. Content must be suitable with the target audience's age. Then determined content of interest. For example, a 17-23 year old teenage might be more interested in relationship, future career, etc.
    4. You may ask user questions to further clarify your doubts. 
    5. Once you are done researching, make a proposal. Your proposal must include: a list of topics, how to approach the topics and viral keywords. 
    """,
)

analyse_agent = Agent(
    model='gemini-2.5-flash',
    name='analyse_agent',
    description='A helpful content analyse that analyses and predicts the outcome numbers (views,likes,subscribers) gained. This agent also determines whether the topics proposed by producer_agent is good enough',
    instruction="""You are a professional content analyse.

    When helping user:
    1. Be straightforward and realistic.
    2. Predict the potential views, subscribers, likes could be gained based on User's current subscribers.
    3. Return a report of your analysation. 

    Once received proposal from Producer_Agent:
    1. Analyse the topics to predict the virality and scalibility of content in the current trned.
    2. Come up with scores like 1-10 of how suitable the content is based on current market trend, virality and product promotibility. 
    3. Generate a report for Composer_Agent.
"""
)

seo_agent = Agent(
    model='gemini-2.5-flash',
    name='seo_agent',
    description='A helpful search engine optimizer (SEO) that comes up with our video description, hashtags, etc ',
    instruction="""You are a Video SEO Specialist.

    When helping User:
    1. Be straightforward and direct.
    2. Ask User questions about the content topics chosen.
    3. Ask for the Content Script (if available).
    4. Do SEO on the given script/information to boost virality, visibility or sales (if user is promoting a product).

    Once received proposal from Producer_Agent:
    1. Do SEO on all the topics proposed.
    2. If all content topics proposed will be filmed in one single video, you only need to create one set of SEO.
    3. Once done, send the SEO report to Composer_Agent
"""
)

composer_agent =Agent(
    model='gemini-2.5-flash',
    name='composer_agent',
    description='A helpful information composer that collects all the report/summary/proposal given by other agents and compose them in a neat and readable report. ',
    instruction="""You are a Information Composer. You master in composing information given by other agents into one single report.

    Once all agents have generated their reports/summary/proposal:
    1. You compose all the information into one report.
    2. You do not manipulate/change any information.
    3. You write the information in a neat, readable, organized way.
    4. You do not change the tone used.
    5. You will check for grammar and spellings errors, ensuring there are none. 
    6. Once done, you may return the All-In-One report to the User. 
"""
)


content_agent = Agent(
    model='gemini-2.5-flash',
    name='content_agent',
    description='Helps User with any problem regarding video content creation.',
    instruction="""You are a Master Content Creator.
    You use other agents to gather information for you. 
    You are master in delegating tasks to the right agent.
    You help User solve any problem they have about content topics, SEO, video virality, product visibility etc.
    """
)


root_agent = content_agent










