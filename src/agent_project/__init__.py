import os

from dotenv import load_dotenv

ROOTPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(ROOTPATH, '.env')

#获取env中的参数
load_dotenv(env_path)

model_name = os.getenv('ModelName')
model_url = os.getenv('ModelURL')
model_api_key = os.getenv('ModelAPIKey')

dashscope_model_name = os.getenv('DashScopeModelName')
dashscope_api_key = os.getenv('DashScopeAPIKey')

google_api_url = os.getenv('GoogleApiURL')
google_api_key = os.getenv('GoogleApiKey')


amap_api_key = os.getenv('GAODE_API_KEY')


def create_model_and_formatter(provider: str = "openai"):
    """根据 provider 创建对应的 model 和 formatter。

    Args:
        provider: "openai" 使用 OpenAI 兼容接口，"dashscope" 使用 DashScope 接口。

    Returns:
        (model, formatter) 元组。
    """
    if provider == "dashscope":
        from agentscope.formatter import DashScopeChatFormatter
        from agentscope.model import DashScopeChatModel

        model = DashScopeChatModel(
            model_name=dashscope_model_name,
            api_key=dashscope_api_key,
        )
        formatter = DashScopeChatFormatter()
    else:
        from agentscope.formatter import OpenAIChatFormatter
        from agentscope.model import OpenAIChatModel

        model = OpenAIChatModel(
            model_name=model_name,
            api_key=model_api_key,
            client_kwargs={"base_url": model_url},
        )
        formatter = OpenAIChatFormatter()

    return model, formatter


def main() -> None:
    print("agent-project")








