# File Name: viz.py
# Student Name: Cam Shinker
# email: shinkecj@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/27/2025
# Course #/Section: IS 4010-002
# Semester/Year: Spring 2025
# Brief Description of the assignment: Create a data viz using this AI data

# Brief Description of what this module does: Learning about how to work with different data types.
# Citations: 

# Anything else that's relevant:

# Start here
import matplotlib.pyplot as plt

def visualize_readability_indices(indices, dataset_name):
    """
    Creates a bar chart for the given readability indices.
    
    Parameters:
        indices (dict): A dictionary of readability index names to their values.
        dataset_name (str): The name of the dataset for the title.
    """
    keys = list(indices.keys())
    values = list(indices.values())
    plt.figure(figsize=(10, 6))
    plt.bar(keys, values, color='skyblue', edgecolor='black')
    plt.title(f"Readability Indices for {dataset_name}")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()

def visualize_prompt_length_distribution(questions):
    """
    Creates a histogram to show the distribution of word counts in the question prompts.
    
    Parameters:
        questions (list): A list of question dictionaries with a 'prompt' key.
    """
    # Compute the word count for each prompt
    lengths = [len(q["prompt"].split()) for q in questions if "prompt" in q]
    plt.figure(figsize=(10, 6))
    plt.hist(lengths, bins=20, edgecolor='black')
    plt.title("Distribution of Question Prompt Lengths")
    plt.xlabel("Word Count")
    plt.ylabel("Frequency")
    plt.show()
