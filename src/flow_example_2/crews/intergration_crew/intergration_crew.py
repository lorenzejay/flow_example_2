from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class IntergrationCrew:
    """Intergration Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def google_sheets_agent(self) -> Agent:
        # enterprise_action_tool = CrewaiEnterpriseTools(
        #     enterprise_token="eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIzX29yZ19pZDooMykiLCJpYXQiOjE3NDg1NDg2NTIsImV4cCI6MTc1MzczMjY1Mn0.ZeVBpWS4tn-eS9PFvspfiCO-Ni4ualaP2z4u7SOb_NPIu6n2dn7h98C3dJkTNeHxJOPyVjCABeqc44p3xoAE3kmA5JT_SMU9ffl0RIewGHah6k-NNK17Qcvs2SiCJd9SSM9PfainI-Q8f9Gn2aPVMRMWaMi4aP7JO4aVUZxU8epGXuC6Sd1vX0epab6KHCqG2BL9dgua_-liI7dUTcaORpPIGWxt9nlkLPATMqkzvh4i7EwOa3EQcO5HnUCwEubZH6BNuQ7j3TOQzzwIhAbS3fGw-dAFKmx5fbtmDv86-y7cV34bDHN0BiMfLoImHjZWy0CBUQc7rJNIItfA95RPOSL8NdRSMW4e0OtR7PP9a1a2amKOcvIbO3L5Ob7WkCM8Twv7XhJ9-p21ihEhHiy9l-LTC-EuHWziGSkE_FAhT05Fub2w3gx9uFr3SRGUxKq2j1qH_jbWwNEpQEIdXAWcDVETaJwK4tCkRthTtcQ0AcTj9UdyQurptQ0hbL4YfV63IZn6emZ-jALH6UBnF4lEEq-X4CMqpzd2UCO55yDlRmh2ENbr0iio2YvruxZRk9Qo-1WO-nUNMCvQG3cDZAcTLJw_V4RY4vv-NUh3Xm4kAMxO8S7CfvhW9l_dRYp5URXD11tqwVMC6l9zgyZq7bCzSlWI1QPxpOj96wF0OEAlqfY",
        #     # enterprise_action_kit_project_id="23eed969-061e-45bb-a56a-ef392d984adb",
        # )
        return Agent(
            config=self.agents_config["google_sheets_agent"],
            # tools=enterprise_action_tool,
        )

    @task
    def write_poem(self) -> Task:
        return Task(
            config=self.tasks_config["write_poem"],
        )

    @crew
    def crew(self):
        return Crew(
            name="intergration_crew",
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )
