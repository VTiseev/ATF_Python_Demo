import os
import ast


def test_pages_do_not_import_tests():
    """
    Архитектурный тест: проверяем, что Page Objects (папка pages)
    не зависят от тестов (папка tests).
    """
    # 1. Находим корневую папку проекта и папку pages
    current_dir = os.path.dirname(__file__)
    project_root = os.path.dirname(os.path.dirname(current_dir))
    pages_dir = os.path.join(project_root, 'pages')

    # 2. Перебираем все файлы в папке pages
    for root, _, files in os.walk(pages_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)

                # 3. Читаем код файла и превращаем его в дерево (AST)
                with open(file_path, 'r', encoding='utf-8') as f:
                    tree = ast.parse(f.read(), filename=file)

                # 4. Ищем все строки, где есть import
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            assert not alias.name.startswith('tests'), \
                                f"Архитектурная ошибка: {file} импортирует {alias.name}!"

                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            assert not node.module.startswith('tests'), \
                                f"Архитектурная ошибка: {file} импортирует из {node.module}!"

#final check

