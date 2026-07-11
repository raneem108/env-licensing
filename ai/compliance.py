



def check_compliance(activity_type: str, distance: int) -> dict:
    # 1. Define standard rules for different activity types
    rules = {
    "dairy factory": {"category": "Category 3 - Limited Risk", "min_distance": 250},
    "slaughterhouse": {"category": "Category 1 - High Risk", "min_distance": 2000},
    "asphalt mixer": {"category": "Category 2 - Medium Risk", "min_distance": 2000},
    "plastic factory": {"category": "Category 3 - Limited Risk", "min_distance": 250},
    "sponge factory": {"category": "Category 2 - Medium Risk", "min_distance": 500},
}
    
    # 2. Handle unknown activity types safely
    if activity_type not in rules:
        return {
            "approved": False,
            "error": f"Unknown activity type: '{activity_type}'"
        }
        
    activity_rules = rules[activity_type]
    required_distance = activity_rules["min_distance"]
    
    # 3. Evaluate compliance dynamically
    is_approved = distance >= required_distance
    reason = "Compliant with local zoning laws." if is_approved else "Insufficient distance from residential area."
    
    return {
        "approved": is_approved,
        "category": activity_rules["category"],
        "required_distance": required_distance,
        "provided_distance": distance,
        "reason": reason
    }

