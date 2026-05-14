# tests/test_query_expansion.py


from src.query_expander import MockQueryExpander


def test_query_expansion():

    expander = MockQueryExpander()

    query = "How does the system handle peak load?"

    expanded_query = expander.expand_query(query)

    assert expanded_query != query