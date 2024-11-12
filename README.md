# Martech
Use case objective is to transform the bank’s marketing efforts, improving engagement and conversion rates through precise, personalized interactions.
Key Solution Elements:
Data Utilization: Synthetic data incorporating demographic (age, gender, location), behavioral (transaction history, online behavior), and psychographic (interests, values, lifestyle) markers.
Personalized Messaging: Crafting messages tailored to the interests and motivations of each persona.
Visual Creatives: Designing visuals that appeal to the aesthetic preferences of each persona.
Channel Optimization: Selecting the most effective communication channels for each persona.
The AI-generated content ensured alignment with the bank’s brand voice and standards, evaluated based on deployable solutions, code quality, campaign quality, model accuracy, and speed.

Below are the steps (preferably in VS Code IDE):
Step 1:
Fork the code to local machine and ensure all the following files & folders saved:
CBA Case study_NatarajanR.pdf
data
--> synthetic_bank_customers.csv

notebooks
--> campaign_optimized.ipynb
README.md
requirements.txt
scripts
--> 	app.py
	email_templates.py
	model.py
	utils.py
templates
	index.html
	static

Step 2:
Run the following 2 commands:
python -m venv env
.\env\Scripts\activate

Install all the necessary libraries from requirements.txt
pip install -r requirements.txt

Step 3:
Run each cells in the notebook (campaign_optimized.ipynb) to get the trained model pickle file. Validate the model accuracy is 73%

Step 4:
Confirm the necessary pkl files are created in the right folder for Model Inferencing and Label encoding

Step 5:
Open terminal and run the command Python scripts/app.py



