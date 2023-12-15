import pytest
from swarms.prompts.swarm_daddy import (AGENT_CONFIGURATION_AGENT_PROMPT,
                                        AGENT_ROLE_IDENTIFICATION_AGENT_PROMPT,
                                        SWARM_ASSEMBLY_AGENT_PROMPT,
                                        TESTING_OPTIMIZATION_AGENT_PROMPT)


def test_agent_role_identification_agent_prompt():
    user_idea = "screenplay writing"
    output = AGENT_ROLE_IDENTIFICATION_AGENT_PROMPT.format(user_idea=user_idea)
    assert isinstance(output, str)

def test_agent_configuration_agent_prompt():
    agent_roles = ["Role1", "Role2"]
    output = AGENT_CONFIGURATION_AGENT_PROMPT.format(agent_roles=agent_roles)
    assert isinstance(output, str)

def test_swarm_assembly_agent_prompt():
    agent_sops = ["SOP1", "SOP2"]
    output = SWARM_ASSEMBLY_AGENT_PROMPT.format(agent_sops=agent_sops)
    assert isinstance(output, str)

def test_testing_optimization_agent_prompt():
    swarm_script = "Swarm script"
    output = TESTING_OPTIMIZATION_AGENT_PROMPT.format(swarm_script=swarm_script)
    assert isinstance(output, str)
