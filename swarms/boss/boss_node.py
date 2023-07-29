import logging
import os
from typing import Optional

import faiss
from langchain import LLMChain, OpenAI, PromptTemplate
from langchain.agents import AgentExecutor, Tool, ZeroShotAgent
from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings
from langchain.experimental import BabyAGI
from langchain.vectorstores import FAISS
from pydantic import ValidationError



logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ---------- Boss Node ----------
class BossNodeInitializer:
    """
    The BossNode class is responsible for creating and executing tasks using the BabyAGI model.
    It takes a language model (llm), a vectorstore for memory, an agent_executor for task execution, and a maximum number of iterations for the BabyAGI model.
    """
    def __init__(self, llm, vectorstore, agent_executor, max_iterations, human_in_the_loop, embedding_size):
        if not llm or not vectorstore or not agent_executor or not max_iterations:
            logging.error("llm, vectorstore, agent_executor, and max_iterations cannot be None.")
            raise ValueError("llm, vectorstore, agent_executor, and max_iterations cannot be None.")
        self.llm = llm
        self.vectorstore = vectorstore
        self.agent_executor = agent_executor
        self.max_iterations = max_iterations
        self.human_in_the_loop = human_in_the_loop
        self.embedding_size = embedding_size

        try:
            self.baby_agi = BabyAGI.from_llm(
                llm=self.llm,
                vectorstore=self.vectorstore,
                task_execution_chain=self.agent_executor,
                max_iterations=self.max_iterations,
                human_in_the_loop=self.human_in_the_loop
            )
        except ValidationError as e:
            logging.error(f"Validation Error while initializing BabyAGI: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected Error while initializing BabyAGI: {e}")
            raise

    def initialize_vectorstore(self):
        """
        Init vector store
        """
        try:     
            embeddings_model = OpenAIEmbeddings(openai_api_key=self.openai_api_key)
            embedding_size = self.embedding_size
            index = faiss.IndexFlatL2(embedding_size)
            return FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})
        except Exception as e:
            logging.error(f"Failed to initialize vector store: {e}")
            return None
        
    def initialize_llm(self, llm_class, temperature=0.5):
        """
        Init LLM 

        Params:
            llm_class(class): The Language model class. Default is OpenAI.
            temperature (float): The Temperature for the language model. Default is 0.5
        """
        try: 
            # Initialize language model
            return llm_class(openai_api_key=self.openai_api_key, temperature=temperature)
        except Exception as e:
            logging.error(f"Failed to initialize language model: {e}")



    def create_task(self, objective):
        """
        Creates a task with the given objective.
        """
        if not objective:
            logging.error("Objective cannot be empty.")
            raise ValueError("Objective cannot be empty.")
        return {"objective": objective}

    def run(self, task):
        """
        Executes a task using the BabyAGI model.
        """
        if not task:
            logging.error("Task cannot be empty.")
            raise ValueError("Task cannot be empty.")
        try:
            self.baby_agi(task)
        except Exception as e:
            logging.error(f"Error while executing task: {e}")
            raise





class BossNode:
    #the bossNode is responsible for creating and executing tasks using the BABYAGI model
    #it takes a lm a vectorstore for memory and agent_executor for task exeuction, and a maximum number of iterations, for the babyagi model
    def __init__(self,
                objective,
                vectorstore,
                boss_system_prompt: Optional[str] = "You are a boss planer in a swarm who is an expert at coming up with a todo list for a given objective and then creating a worker to help you accomplish your task. Rate every task on the importance of it's probability to complete the main objective on a scale from 0 to 1, an integer. Come up with a todo list for this objective: {objective} and then spawn a worker agent to complete the task for you. Always spawn a worker agent after creating a plan and pass the objective and plan to the worker agent.",
                api_key=None,
                worker_node=None, 
                llm_class=OpenAI, 
                max_iterations=5, 
                verbose=False
                ):
        
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.vectorstore = vectorstore
        self.worker_node = worker_node

        self.boss_system_prompt = boss_system_prompt
        
        self.llm_class = llm_class
        self.max_iterations = max_iterations
        self.verbose = verbose

        if not self.api_key:
            raise ValueError("[BossNode][ValueError][API KEY must be provided either as an argument or as an environment variable API_KEY]")
        
        self.llm = self.initialize_llm(self.llm_class)

        todo_prompt = PromptTemplate.from_template(boss_system_prompt)
        todo_chain = LLMChain(llm=self.llm, prompt=todo_prompt)

        tools = [
            Tool(name="TODO", func=todo_chain.run, description="useful for when you need to come up with todo lists. Input: an objective to create a todo list for your objective. Note create a todo list then assign a ranking from 0.0 to 1.0 to each task, then sort the tasks based on the tasks most likely to achieve the objective. The Output: a todo list for that objective with rankings for each step from 0.1 Please be very clear what the objective is!"),
            self.worker_node
        ]
        suffix = """Question: {task}\n{agent_scratchpad}"""
        prefix = """You are an Boss in a swarm who performs one task based on the following objective: {objective}. Take into account these previously completed tasks: {context}.\n """
        
        prompt = ZeroShotAgent.create_prompt(tools, prefix=prefix, suffix=suffix, input_variables=["objective", "task", "context", "agent_scratchpad"],)
        llm_chain = LLMChain(llm=self.llm, prompt=prompt)
        agent = ZeroShotAgent(llm_chain=llm_chain, allowed_tools=[tool.name for tool in tools])

        self.agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=self.verbose)

        self.boss = BossNodeInitializer(self.llm, self.vectorstore, self.agent_executor, self.max_iterations)
        self.task = self.boss.create_task(objective)

    def run(self):
        self.boss.run(self.task)