# File Name: main.py
# Student Name: Cam Shinker,  Ryan Jacob
# email: shinkecj@mail.uc.edu,   Jacobry@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/27/2025
# Course #/Section: IS 4010-002
# Semester/Year: Spring 2025
# Brief Description of the assignment: Create a data viz using this AI data

# Brief Description of what this module does: Learning about how to work with different data types.
# Citations: Ryan used ChatGPT o3-mini-high: https://chatgpt.com/

# Anything else that's relevant:

from readingLevelPackage.readingLevel import Reading_Level
from utilitiesPackage.utilities import *
from utilitiesPackage.CSV_Utilities import *
from PDFPackage.PDFUtilities import *


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

if __name__ == "__main__":

    CSV_Processor = MMLU_CSV_Processor("dataPackage/MMLU/data/", ["management_test.csv"])
    questions = CSV_Processor.read_data()
    print(len(questions), "questions read")

 
    # Start from here


    #Add logic (modularly!) to perform some interesting data visualization. You are ‘weapons free’ on
    #this effort: use any AI tool you wish. Be sure cite your sources* so I can get a feel for what everyone is
    #up to.

    #0. Append all the prompts into a big string - See utilities.convert_dictionaries_to_string()
    text = convert_dictionaries_to_string(questions, ["prompt", "possible answers"])
    #1. Perform reading level analysis on the big string and print the results to the console.
    reading_indices = Reading_Level.compute_readability_indices("MMLU", text)

    if reading_indices is None:
        print("Error: Reading level analysis did not return any values. Please check the compute_readability_indices function.")
    else:
        print("Readability Indices:", reading_indices)
        
        # Visualize the readability indices as a bar chart.
        visualize_readability_indices(reading_indices, "MMLU")
        
        # Visualize the distribution of question prompt lengths.
        visualize_prompt_length_distribution(questions)


    



    #myPDF = PDFUtilities()
    #myPDF.create_question_PDF("Management Test", "MMLU", questions)
   
    #print("The first question:")
    #print(questions[0])
    
    text = convert_dictionaries_to_string(questions, ["prompt", "possible answers"])
    #print("\ntext from dictionaries:", text[0:500])

    
    
    

  
    questions_written = write_questions_to_text_files("MMLU", questions)
    print(questions_written, "questions written to the file.")
    
    
    """
    # This code is commented out
    #Reading_Level.test01()

    text = "This is a sentence that we can use to test the reading level computations. "
    reading_level_indices = Reading_Level.compute_readability_indices("Dummy Benchmark", text)
    for key in reading_level_indices.keys():
        print(key, ":", reading_level_indices[key])
            
    # A test with text at a higher reading level
    text = "Birds, employing a combination of aerodynamic principles and specialized anatomical adaptations, achieve flight through the generation of lift, which counteracts the force of gravity."
    reading_level_indices = Reading_Level.compute_readability_indices("Dummy Benchmark", text)
    for key in reading_level_indices.keys():
        print(key, ":", reading_level_indices[key])
    """
