from agents.code_analysis_agent import CodeAnalysisAgent
from agents.code_refactoring_agent import CodeRefactoringAgent
from parsers.ast_parser import ASTParser

MAX_RETRIES = 3


def simulate_code_changes(
    code_analysis_agent,
    code_refactoring_agent,
    codebase,
    developer_task,
    original_ast,
    retries=0,
):
    """Simulates code changes and tests the AST & unit tests."""

    code_sections = code_analysis_agent.analyze_code(developer_task, original_ast)

    code_changes = code_refactoring_agent.derive_code_changes(code_sections)
    simulated_refactored_code = code_refactoring_agent.refactor_code(
        code_sections, code_changes, simulation=True
    )

    unit_test_result = code_refactoring_agent.run_tests(simulated_refactored_code)
    ast_test_result = code_refactoring_agent.compare_asts(original_ast)

    if unit_test_result and ast_test_result:
        print(f"Simulation successful on attempt {retries + 1}")
        return code_sections, code_changes

    if retries < MAX_RETRIES:
        print(
            f"Simulation failed (Attempt {retries + 1})... Retrying"
        )
        return simulate_code_changes(
            codebase, developer_task, original_ast, retries + 1
        )

    print("Simulation failed after maximum retries.")
    return None, None


def main():
    '''
    1. Think of ways we can take codebase as an input. We could have to parse entire codebase file by file (Refer to repo graph paper?)
    2. Get human input (This will be the developer task)
    3. Pass the input to CodeAnalysis agent
    '''

    codebase = None
    developer_task = None

    ast_parser = ASTParser()
    code_analysis_agent = CodeAnalysisAgent()
    code_refactoring_agent = CodeRefactoringAgent()

    original_ast = ast_parser.generate_ast_graph(codebase)

    code_sections, code_changes = simulate_code_changes(
        code_analysis_agent,
        code_refactoring_agent, 
        codebase,
        developer_task,
        original_ast,
    )

    if code_changes:
        print("Refactoring is happening")
        code_refactoring_agent.refactor_code(
            code_sections, code_changes, False
        )
    else:
        print("Migration failed after multiple attempts. No changes were applied.")


if __name__ == "__main__":
    main()
