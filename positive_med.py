from termcolor import colored
from swarms import OpenAIChat
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAIChat(openai_api_key=openai_api_key)


"""
Flow

Topic selection agent -> draft agent -> review agent -> distribution agent

Topic Selection Agent:
- Generate 10 topics on gaining mental clarity using Taosim and Christian meditation

Draft Agent:
- Write a 100% unique, creative and in human-like style article of a minimum of 5,000 words using headings and sub-headings.

Review Agent:
- Refine the article to meet PositiveMed’s stringent publication standards.

Distribution Agent:
- 

"""


TOPIC_GENERATOR = f"""
Generate topics for PositiveMed.com:
Generate topics for PositiveMed.com:

Monitor Health Trends: Scan Google Alerts, authoritative health websites, and social media for emerging health, wellness, and medical discussions.
Keyword Research: Utilize tools like SEMrush to identify keywords with moderate to high search volume and low competition. Focus on long-tail, conversational keywords.
Analyze Site Data: Review PositiveMed's analytics to pinpoint popular articles and areas lacking recent content.
Crowdsourcing: Gather topic suggestions from the brand's audience and internal team, ensuring alignment with PositiveMed's mission.
Topic Evaluation: Assess topics for audience relevance, uniqueness, brand fit, current relevance, and SEO potential.
Tone and Style: Ensure topics can be approached with an educational, empowering, and ethical tone, in line with the brand's voice.
Use this framework to generate a list of potential topics that cater to PositiveMed's audience while staying true to its brand ethos.
"""


REVIEW_PROMPT = """
You are responsible for refining an article to meet PositiveMed’s stringent publication standards. 
Your role involves content analysis, editorial precision, expert validation, legal verification, and overall quality assurance. 

# ContentReview:
- Provide constructive feedback on outline and drafts content 
- Collect input on strengths to leverage and areas needing improvement.

# Editor Review:  
- Evaluate initial drafts for errors, gaps that require additional research.
- Provide guidance on better organizing structure and flow.
- Assess tone, voice and brand alignment.

# Expert Review:
- Ask medical experts related to article topic to validate accuracy of information.
- Verify advice follows ethical guidelines accepted by the medical community.   
- Request quotes that lend credibility and reinforce key points.

# Legal Review:  
- Confirm content meets regulatory standards for health claims and liability risks.
- Address any recommended edits to mitigate brand reputation risk.

# Quality Checklist:  Scrutinize final draft against PositiveMed's standards:
- Medical accuracy - error-free facts/statistics, supported claims 
- Logical flow - smooth transitions, complementary sections  
- Reader value - insightful analysis beyond fluffy content
- Brand alignment - uplifting tone, inclusive messaging
- Strong conclusion - memorable takeaways, relevant next steps/resources for readers
 

# ARTICLE TO REVIEW:
{{ARTICLE}}

# OUTPUT:
!!IMPORTANT 
Please go into as much detail as possible and return as much content as possible by reaching your max ouput token length 
Re-Write the article, taking into account all review instructions and standards
Return your maxium token length worth of blog content 
"""


SOCIAL_MEDIA_SYSTEM_PROMPT_AGENT = """
You're the Social Media System Agent. Your job is to create social media posts for the article below.

Your responsibilities are:
Publishing and Distribution:
    •    Publishing AI Agent:
    •    Automated publishing to designated platforms.
    •    Formatting checks for platform compatibility.
    •    Distribution:
    •    Automated sharing to social media channels.
    •    Email distribution to subscriber list.

Create high converting posts for each social media instagram, facebook, twitter, linkedin, and pinterest optimizing for {{GOAL}} using the article below.

Denote the social media's by using the social media name in HTML like tags

<FACEBOOK> POST CONTENT </FACEBOOK>
<TWITTER> POST CONTENT </TWITTER>
<INSTAGRAM> POST CONTENT </INSTAGRAM>

######### ARTICLE #######
{{ARTICLE}}
"""


def get_draft_prompt(topic, theme):
    prompt = DRAFT_PROMPT.replace(
        "{{TOPIC}}", topic).replace("{{THEME}}", theme)
    return prompt


def get_review_prompt(article):
    prompt = REVIEW_PROMPT.replace("{{ARTICLE}}", article)
    return prompt


def social_media_prompt(article: str, goal: str = "Clicks and engagement"):
    prompt = SOCIAL_MEDIA_SYSTEM_PROMPT_AGENT.replace("{{ARTICLE}}", article).replace(
        "{{GOAL}}", goal
    )
    return prompt


# Agent that generates topics
topic_selection_task = (
    "Generate 10 topics on gaining mental clarity using ancient Taosim practices"
)
topics = llm(
    f"Your System Instructions: {TOPIC_GENERATOR}, Your current task: {topic_selection_task}"
)

dashboard = print(
    colored(
        f"""
    Topic Selection Agent
    -----------------------------

    Topics:
    ------------------------
    {topics}
    
    """,
        "blue",
    )
)

# Agent that generates blogs
DRAFT_AGENT_SYSTEM_PROMPT = f"""
Write a 5,000 word + narrative essay on a 100% unique, creative and in human-like style article of a minimum of 5,000 words using headings and sub-headings.
Ensure your tone is Professional and casual while focusing on presenting information and analysis without excessive embellishment.

Here is a list of topics, write the narrative on the first one: {topics}

"""


draft_blog = llm(DRAFT_AGENT_SYSTEM_PROMPT)
draft_out = print(
    colored(
        f"""
    
    ------------------------------------
    Drafter Writer Agent
    -----------------------------

    Draft:
    ------------------------
    {draft_blog}
    
    """,
        "red",
    )
)


# Agent that reviews the draft
review_agent = llm(get_review_prompt(draft_blog))
reviewed_draft = print(
    colored(
        f"""
    
    ------------------------------------
    Quality Assurance Writer Agent
    -----------------------------

    Complete Narrative:
    ------------------------
    {draft_blog}
    
    """,
        "blue",
    )
)


# Agent that publishes on social media
distribution_agent = llm(social_media_prompt(
    draft_blog, goal="Clicks and engagement"))
distribution_agent_out = print(
    colored(
        f"""
        --------------------------------
        Distribution Agent
        -------------------

        Social Media Posts
        -------------------
        {distribution_agent}

        """,
        "magenta",
    )
)
print(distribution_agent_out)
