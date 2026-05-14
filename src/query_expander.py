# src/query_expander.py

class MockQueryExpander:
    """
    Mocked GenerativeModel for query expansion.
    """

    def expand_query(self, query):
        query_mappings = {
            "How does the system handle peak load?":
                "How does the system manage traffic spikes, autoscaling, load balancing, and high concurrent requests?",

            "How are services protected from too many requests?":
                "How does the platform implement rate limiting and backend protection against excessive traffic?",

            "How does the system recover from failures?":
                "How are backups, disaster recovery, and infrastructure restoration handled in distributed systems?"
        }
        return query_mappings.get(query, query)