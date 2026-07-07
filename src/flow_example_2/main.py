#!/usr/bin/env python
from pydantic import BaseModel

from crewai.flow import Flow, listen, start
from crewai.flow.human_feedback import human_feedback


class PoemState(BaseModel):
    sentence_count: int = 1
    poem: str = ""
    approved: bool = False


class PoemFlow(Flow[PoemState]):
    name = "poem_flow_hitl_failure_repro"

    @start()
    def generate_sentence_count(self) -> str:
        self.state.sentence_count = 2
        self.state.poem = "roses are red\nviolets are blue"
        return self.state.poem

    @listen(generate_sentence_count)
    @human_feedback(message="Review this poem before the failure step:")
    def review_poem(self, poem: str) -> str:
        self.state.approved = True
        return poem

    @listen(review_poem)
    def after_human_feedback(self, poem: str) -> str:
        print("POEM AFTER HUMAN FEEDBACK", poem)
        return poem


def kickoff():
    poem_flow = PoemFlow(tracing=True)
    res = poem_flow.kickoff(inputs={"sentence_count": 2})
    print("POEM FLOW RESULT", res)
    return res


def plot():
    poem_flow = PoemFlow()
    poem_flow.plot()


if __name__ == "__main__":
    kickoff()
