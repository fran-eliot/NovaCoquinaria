SEMANTIC_RULES = {
    "receta": {
        "expected_outgoing_types": {
            "base",
            "tecnica",
            "ingrediente",
            "plantilla",
            "tabla",
        },
    },
    "plantilla": {
        "expected_outgoing_types": {
            "base",
            "tecnica",
            "ingrediente",
            "tabla",
        },
    },
    "tecnica": {
        "expected_outgoing_types": {
            "base",
            "ingrediente",
            "tabla",
        },
    },
}