# Map products and offers to target audiences
def get_product_details(target_audience):
    print("Inside get_product_details and target_audience is:", target_audience)
    products = {
        'Young clients': ("Youth Savings Account", "No monthly fees for the first year"),
        'Family': ("Family Package Account", "Lower interest rates on family loans"),
        'High Networth Individuals': ("Premium Credit Card", "Exclusive rewards and travel benefits"),
        'Small business': ("Business Checking Account", "Free transactions for the first six months"),
        'Students': ("Student Banking Account", "Cashback on all purchases"),
        'Tech savvy customer': ("Tech Savvy Account", "High interest on digital transactions"),
        'Frequent traveller': ("Travel Credit Card", "Double points on travel expenses")
    }
    return products.get(target_audience, ("General Banking Account", "Competitive interest rates"))
