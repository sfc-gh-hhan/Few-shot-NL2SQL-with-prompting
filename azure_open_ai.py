# from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import AzureChatOpenAI
import os

AZURE_OPENAI_MODEL_LIST = ["gpt-4o", "gpt-4-turbo-2024-04-09", "gpt-4-0613", "gpt-4o-mini", "gpt-35-turbo-0613", "gpt-35-turbo-instruct-0914"]

def load_api(path: str):
    api_keys = []
    with open(path, 'r') as f:
        for line in f:
            key = line.strip()
            api_keys.append(key)
    return api_keys

def get_azure_name(model_name):
    if model_name == "gpt-4o":
        # Model version: 2024-05-13
        return "sfc-cortex-analyst-dev"
    elif model_name == "gpt-4-turbo-2024-04-09":
        # Model version: turbo-2024-04-09
        return "sfc-ml-gpt4-turbo"
    elif model_name == "gpt-4-0613":
        # Model version: 0613
        return "sfc-ml-sweden-gpt4-managed"
    elif model_name == "gpt-4o-mini":
        # Model version: 2024-07-18
        return "cortex-analyst-gpt-4o-mini-dev"
    elif model_name == "gpt-35-turbo-0613":
        return "sfc-ml-sweden-gpt35-chat-deployment"
    elif model_name == "gpt-35-turbo-instruct-0914":
        return "sfc-ml-sweden-gpt35-deployment"
    else:
        raise NotImplementedError(f"Model {model_name} not implemented")

def get_azure_lm(_model_name, DEBUG=False):
    model_name = get_azure_name(_model_name)
    keys = load_api(".api_key")
    api_version = '2023-03-15-preview'
    url = f"https://sfc-ml-sweden.openai.azure.com/openai/deployments/{model_name}/chat/completions?api-version={api_version}"

    os.environ["OPENAI_API_VERSION"] = api_version
    os.environ["AZURE_OPENAI_ENDPOINT"] = url
    os.environ["AZURE_OPENAI_API_KEY"] = keys[0]


    # Set up the LM.
    # lm = dspy.AzureOpenAI(api_base=url, api_key=keys[0],1
    #                       api_version=api_version, model=model_name, max_tokens=2048, stop=["\n\n---\n\n"])
    # CHAT = AzureOpenAI(deployment_name=model_name, openai_api_key=keys[0], openai_api_base=url, openai_api_version=api_version, temperature=0, max_tokens=2000)
    CHAT = AzureChatOpenAI(azure_deployment=model_name,  api_version=api_version,
                           temperature=0, max_tokens=2000)
    if DEBUG:
        print(CHAT.invoke("Tell me a joke"))
    return CHAT

def get_openai_lm(model_name, DEBUG=False):
    keys = load_api(".api_key")
    CHAT = ChatOpenAI(model=model_name, openai_api_key=keys[0], temperature=0, max_tokens=2000)

    if DEBUG:
        print(CHAT.invoke("Tell me a joke"))

    return CHAT
