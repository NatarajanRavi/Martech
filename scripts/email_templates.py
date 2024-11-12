import numpy as np
import openai
import re
from utils import get_product_details

# Set your Azure OpenAI endpoint and API key
openai.api_type = "azure"
openai.api_base = "https://nat-instance.openai.azure.com/"
openai.api_version = "2024-05-01-preview"
openai.api_key = 'your_openai_api_key'

def family_email_template():
    return f"""
    As a General Manager of Australian bank send an marketing campaign email for a family.
    The email should only include:
    - The subject line
    - No additional text, Python code, or print statements
    - The body of the email, starting with a greeting and ending with a closing statement
      
    Subject: Discover Family Package Account with Lower interest rates on family loans

    Email Body:
    
    Dear Family,

    Family means everything, and we want to support yours. Discover our:
    > Product: Family Package Account
    > Offer: Lower interest rates on family loans
    
    We're here to help you secure your family's future.

    Sign up now on our website and unlock the potential of our family-friendly products.

    Warm regards,
    General Manager, Australian Bank.
    """

def young_clients_email_template():
    return f"""
    Following are the guidelines for response:
    No need to generate python code
    Avoid any print statement and characted like #
    Create a simple and professional email in English 
    Strictly follow response only by the below format

    As a General Manager of Australian bank send an marketing campaign email to an young customer.

    Subject: Get Started with Our Youth Savings Account

    Email Body:
    
    Dear Young Clients,

    Starting your financial journey? Discover our:
    > Product: Youth Savings Account
    > Offer: No monthly fees for the first year

    Build your savings with confidence and ease.

    Open your account now on our website and take the first step towards financial independence.

    Warm regards,
    General Manager, Australian Bank.
    """

def high_networth_individuals_email_template():
    return f"""
    Following are the guidelines for response:
    No need to generate python code
    Avoid any print statement and characted like #
    Create a simple and professional email in English 
    Strictly follow response only by the below format
    
    As a General Manager of Australian bank send an marketing campaign email to High Networth Individual.

    Subject: Exclusive Benefits with Our Premium Credit Card

    Email Body:
    
    Dear High Networth Individuals,

    Elevate your financial experience with:
    > Product: Premium Credit Card
    > Offer: Exclusive rewards and travel benefits

    Enjoy the prestige and advantages of our premium services.

    Apply now on our website and access a world of exclusive benefits.

    Warm regards,
    General Manager, Australian Bank.
    """

def small_business_email_template():
    return f"""
    Following are the guidelines for response:
    No need to generate python code
    Avoid any print statement and characted like #
    Create a simple and professional email in English 
    Strictly follow response only by the below format
    
    As a General Manager of Australian bank send an marketing campaign email to Small business owner.

    Subject: Boost Your Business with Our Business Checking Account

    Email Body:
    
    Dear Small Business Owners,

    Empower your business with:
    > Product: Business Checking Account
    > Offer: Free transactions for the first six months

    Simplify your business banking with our tailored solutions.

    Open your account now on our website and give your business the support it deserves.

    Warm regards,
    General Manager, Australian Bank.
    """
def students_email_template():
    return f"""
    As a General Manager of Australian bank send an marketing campaign email to student
    The email should only include:
    - The subject line
    - No additional text, Python code, or print statements
    - The body of the email, starting with a greeting and ending with a closing statement
    
    Subject: Student Banking Made Easy

    Email Body:
    
    Dear Students,

    Manage your finances effortlessly with:
    > Product: Student Banking Account
    > Offer: Cashback on all purchases

    Focus on your studies while we take care of your banking needs.

    Open your account now on our website and enjoy student-friendly benefits.

    Warm regards,
    General Manager, Australian Bank.
    """
def tech_savvy_customer_email_template():
    return f"""
    Following are the guidelines for response:
    No need to generate python code
    Avoid any print statement and characted like #
    Create a simple and professional email in English 
    Strictly follow response only by the below format
    
    As a General Manager of Australian bank send an marketing campaign email to Tech savy customer

    Subject: Maximize Your Savings with Our Tech Savvy Account

    Email Body:
    
    Dear Tech Savvy Customers,

    Harness the power of digital banking with:
    > Product: Tech Savvy Account
    > Offer: High interest on digital transactions

    Enjoy seamless and rewarding digital banking experiences.

    Sign up now on our website and elevate your digital banking.

    Warm regards,
    General Manager, Australian Bank.
    """
def frequent_traveller_email_template():
    return f"""
    Following are the guidelines for response generation:
    No need to generate python code
    Avoid any print statement and characted like #
    Create a simple and professional email in English 
    Strictly follow response only by the below format
    
    As a General Manager of Australian bank send an marketing campaign email to Frequent traveller

    Subject: Travel in Style with Our Travel Credit Card

    Email Body:
    
    Dear Frequent Travellers,

    Enhance your travels with:
    > Product: Travel Credit Card
    > Offer: Double points on travel expenses

    Enjoy the convenience and rewards of our travel credit card.

    Apply now on our website and make the most of your journeys.

    Warm regards,
    General Manager, Australian Bank.
    """
def generate_campaign_email(target_audience):
    # Ensure target_audience is decoded if it's numeric
    if isinstance(target_audience, (int, np.integer)):
        target_audience = label_encoders_new['Target'].inverse_transform([target_audience])[0]
    print(f"Target Audience after decoding: {target_audience}")
    product_name, offer_details = get_product_details(target_audience)
    print(f"Product: {product_name}, Offer: {offer_details}")  # Debugging statement

    benefits = [
        f"Product: {product_name}",
        f"Offer: {offer_details}"
        ]
    benefit_string = "\n".join([f"> {benefit}" for benefit in benefits])
    # Email template selection
    if target_audience == 'Family':
        prompt = family_email_template()
    elif target_audience == 'Young clients':
        prompt = young_clients_email_template()
    elif target_audience == 'High Networth Individuals':
        prompt = high_networth_individuals_email_template()
    elif target_audience == 'Small business':
        prompt = small_business_email_template()
    elif target_audience == 'Students':
        prompt = students_email_template()
    elif target_audience == 'Tech savvy customer':
        prompt = tech_savvy_customer_email_template()
    elif target_audience == 'Frequent traveller':
        prompt = frequent_traveller_email_template()
    else:
        return "Invalid target audience"

    response = openai.Completion.create(
        engine="gpt-35-turbo",
        prompt=prompt,
        max_tokens=300,
        temperature=0.7,
        n=1,
        stop=None,
        top_p=0.9,
        frequency_penalty=0.2,
        presence_penalty=0.3
    )

    if response.choices:
        email_content = response.choices[0].text.strip()
        clean_content = re.sub('<[^<]+?>', '', email_content)  # Remove any HTML tags if present
        print("Email content:", clean_content)  # Debugging statement
        return clean_content
    else:
        print("No response generated by OpenAI")
        return "There was an error generating the email content."

