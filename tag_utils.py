from typing import Any, Dict, List

def mock_google_sheets_query(query: str) -> List[Dict[str, Any]]:
    """Mocks data retrieval from Google Sheets."""
    print(f"Mocking Google Sheets query: {query}")
    # Simulate different responses based on query or just return a default
    if "sales" in query.lower():
        return [{'id': 1, 'name': 'Product A', 'sales': 100}, {'id': 2, 'name': 'Product B', 'sales': 150}]
    return [{'column1': 'sheet_data1', 'column2': 'sheet_data2'}]

def mock_notion_query(query: str) -> List[Dict[str, Any]]:
    """Mocks data retrieval from Notion."""
    print(f"Mocking Notion query: {query}")
    if "task" in query.lower():
        return [{'task': 'Design UI', 'status': 'In Progress'}, {'task': 'Implement Backend', 'status': 'To Do'}]
    return [{'page_title': 'notion_page1', 'content': 'notion_content1'}]

def mock_crm_query(query: str) -> List[Dict[str, Any]]:
    """Mocks data retrieval from a CRM system."""
    print(f"Mocking CRM query: {query}")
    if "lead" in query.lower() or "customer" in query.lower():
        return [{'contact': 'John Doe', 'company': 'ABC Corp', 'status': 'Lead'}, {'contact': 'Jane Smith', 'company': 'XYZ Inc', 'status': 'Opportunity'}]
    return [{'crm_field': 'crm_value'}]

def mock_send_email(recipient: str, subject: str, body: str) -> str:
    """Mocks sending an email."""
    print(f"Mocking email send: To={recipient}, Subject={subject}, Body snippet={body[:50]}...")
    return f"Email sent to {recipient} with subject '{subject}'"

def process_tag_query(tool_name: str, query: str, **kwargs) -> Any:
    """Dispatches queries to appropriate mock external tools based on tool_name."""
    if tool_name.lower() == 'google_sheets':
        return mock_google_sheets_query(query)
    elif tool_name.lower() == 'notion':
        return mock_notion_query(query)
    elif tool_name.lower() == 'crm':
        return mock_crm_query(query)
    elif tool_name.lower() == 'email':
        return mock_send_email(query, kwargs.get('subject', 'No Subject'), kwargs.get('body', ''))
    else:
        return f"Unknown TAG tool: {tool_name}"

print(f"Created {project_root}/utils/tag_utils.py")
