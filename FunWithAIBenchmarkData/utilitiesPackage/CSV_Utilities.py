# CSV_Utilities.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import csv

class MMLU_CSV_Processor:
    '''
    CSV Processor for questions in the MMLU Benchmark
    '''
    def __init__(self, question_path, input_files):
        '''
        Constructor
        @param question_path string: the path to the files in the input_files list
        @param List input_files: a list of files to process
        '''
        self.question_path = question_path
        self.input_files = input_files
        print("TruthfulQA_CSV_Processor.__init__:", "self.question_path:", self.question_path, "self.input_files:", self.input_files)
    def read_data(self):
      """
      Reads a CSV Lines (.csv) file into one string.
      @param filename string: The path to the csv Lines file.
      @param lines_to_process int: number of lines in filename to consider. Use 0 for all lines. Default is  0
      @verbose verbose bool: True if the method should print some intermediate data. Default is False
      @return List: A list of dictionaries, one dictionary per line of the csv file
      """
      questions = []
      for input_file in self.input_files:
          print("CSV file path:", self.question_path + input_file)
          with open(self.question_path + input_file, 'r', encoding='utf-8') as csv_file:
            #csv_reader = csv.DictReader(csv_file) # There's no header row, so this has no value
            csv_reader = csv.reader(csv_file)
            question_id = 1
            for line in csv_reader:
                #*************************************
                # map the questions/answers into our dictionary format
                #print(line)
                question = dict()
                question["question id"] = str(question_id)
                question["prompt"] = line[0]
                possible_answers = [line[1], line[2], line[3], line[4]]
                question["possible answers"] = possible_answers
                question["correct answer"] = line[5]
                questions.append(question)
                question_id += 1
      return questions
