# utils/priority_rules.py

HIGH_KEYWORDS = [
    "payment failed",
    "payment deducted",
    "charged twice",
    "duplicate payment",
    "refund",
    "money deducted",
    "fraud",
    "unauthorized",
    "security",
    "breach",
    "hacked",
    "database",
    "server down",
    "outage",
    "crash",
    "critical",
    "urgent",
    "account locked",
    "cannot login",
    "can't login",
    "login failed"
]

MEDIUM_KEYWORDS = [
    "slow",
    "delay",
    "installation",
    "upgrade",
    "vpn",
    "printer",
    "software",
    "configuration"
]

LOW_KEYWORDS = [
    "feature request",
    "feedback",
    "documentation",
    "information",
    "general inquiry",
    "question"
]


def get_priority_from_rules(ticket: str, historical_priority: str) -> str:
    """
    Apply business rules to determine the final priority.
    Falls back to the historical priority if no rule matches.
    """

    text = ticket.lower()

    for keyword in HIGH_KEYWORDS:
        if keyword in text:
            return "high"

    for keyword in MEDIUM_KEYWORDS:
        if keyword in text:
            return "medium"

    for keyword in LOW_KEYWORDS:
        if keyword in text:
            return "low"

    return historical_priority