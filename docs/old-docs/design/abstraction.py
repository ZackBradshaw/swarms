from swarms import Model, Agent, vectorstore, tools, orchestrator

# 1 model
Model(openai)

# 2 agent level
Agent(model, vectorstore, tools)

# 3 worker infrastructure level
from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def method1(self):
        pass

class Agent(ABC):
    @abstractmethod
    def method2(self):
        pass

class worker_node(ABC):
    @abstractmethod
    def method3(self):
        pass

class Orchestrator(ABC):
    @abstractmethod
    def method4(self):
        pass

class Hivemind(ABC):
    @abstractmethod
    def method5(self):
        pass

# 1 model
model = Model()

# 2 agent level
agent = Agent(model)

# 3 worker infrastructure level
worker = worker_node(agent)

# 4 swarm level basically handling infrastructure for multiple worker node
swarm = Orchestrator()

# 5
hivemind = Hivemind(swarm)

# 4 swarm level basically handling infrastructure for multiple worker node
swarm = orchestrator(worker_node, 100)  # nodes

# 5
hivemind = Hivemind(swarm * 100)


# a market different pre built worker or boss agent that have access to different tools and memory, proompts
