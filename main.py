from dotenv import load_dotenv
from langchain import hub
from langchain_experimental.agents import create_csv_agent
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_experimental.tools import PythonREPLTool

load_dotenv()

def main():
    print("Start")

    ## Python Agent

    # instruction = """You are an agent designed to write and execute python code to answer questions.
    # You have access to a python REPL, which you can use to execute python code.
    # If you get an error, debug your code and try again.
    # Only use the output of your code to answer the question.
    # You might know the answer without running any code, but you should still run the code to get the answer.
    # If it does not seem like you can write code to answer the question, just return "I don't know" as the answer.
    # """
    #
    # base_prompt = hub.pull("langchain-ai/react-agent-template")
    # prompt = base_prompt.partial(instructions=instruction)
    # tools = [PythonREPLTool()]
    # agent = create_react_agent(
    #     prompt = prompt,
    #     llm = ChatOpenAI(temperature=0, model="gpt-4o-mini"),
    #     tools = tools
    # )
    #
    # agent_executor = AgentExecutor(agent = agent, tools = tools, verbose=True)
    # agent_executor.invoke(
    #     input={
    #         "input":"""generate and save in current working directory 15 QRcodes
    #         that point to https://www.linkedin.com/in/haseebahmed49/, you have qrcode package install already"""
    #     }
    # )

    csv_agent = create_csv_agent(
        llm = ChatOpenAI(temperature=0, model="gpt-4o"),
        path = "episode_info.csv",
        verbose=True,
        allow_dangerous_code=True  # Opt-in to run code
    )

    # csv_agent.invoke(
    #     input={"input":"How many columns are there in file episode_info.csv"}
    # )
    #
    # csv_agent.invoke(
    #     input={"input":"in the episode_info, which write wrote the most episodes? How many episodes did he write"}
    # )

    csv_agent.invoke(
        input={"input":"which season has the most episodes?"}
    )


if __name__ == '__main__':
    main()