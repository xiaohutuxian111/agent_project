from openai import OpenAI
from typing import List, Dict, Tuple


class BaseModel:
    def __init__(self, api_key: str = '') -> None:
        self.api_key = api_key

    def chat(self, prompt: str, history: List[Dict[str, str]], system_prompt: str = "") -> Tuple[str, List[Dict[str, str]]]:
        """
        基础聊天接口
        
        Args:
            prompt: 用户输入
            history: 对话历史
            system_prompt: 系统提示
            
        Returns:
            (模型响应, 更新后的对话历史)
        """
        pass

class Siliconflow(BaseModel):
    def __init__(self, model_api_key: str, model_url:str='',model_name: str = "siliconflow-3.5",):
        self.api_key = model_api_key
        self.client = OpenAI(api_key=self.api_key, base_url=model_url)
        self.model_name = model_name
        
    def chat(self, prompt: str, history: List[Dict[str, str]], system_prompt: str = "") -> Tuple[str, List[Dict[str, str]]]:
        
        messages =   [
            {'role': 'system', 'content': system_prompt},
        ]
        if history:
            messages.extend(history)

        # 添加当前用户信息
        messages.append({'role':'user', 'content': prompt})
        
        # 调用api
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=0.5,
            max_tokens=2028,
        )

        model_response =   response.choices[0].message.content

        # 更新历史对话
        updated_history = messages.copy()
        updated_history.append({'role':'assistant', 'content': model_response})
        
        return model_response,updated_history

if __name__ == "__main__":
    from  agent_project import model_name, model_url, model_api_key
    llm = Siliconflow(model_api_key, model_url, model_name)
    response, history = llm.chat("你好", [])
    print(response)
  
