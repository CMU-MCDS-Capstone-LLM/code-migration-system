
class CodeAnalysisAgent:
    def __init__(self):
        '''
        Initialize agents. Can look at how Langchain agent implementation is done.
        https://python.langchain.com/docs/tutorials/agents/
        Research more into suitable tools that can be used or how we can integrate the tool.
        '''
        self.agent = None

    def analyze_code(self, migration_task, ast_graph):
        '''
        1. Define the prompt that uses the ast_graph/repo_graph. Need to think of ways to include the ast graph/repo graph
        into the prompt. Beware of the context length when combining AST graph
        2. Generate the output after analysis
        3. Output should be in JSON format

        https://python.langchain.com/v0.1/docs/modules/model_io/output_parsers/types/json/
        Potential Json Format
        {
            "line_number": 5,
            "original_code": "old_function()",
            "reason": "API call should be using a different function name",
        }
        '''

        prompt = None
        
        response = self.agent.predict(prompt)

        '''
        If the confidence score is not high, query the knowledge DB. Leave to next iterations
        '''

        return response
