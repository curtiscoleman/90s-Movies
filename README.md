# 90s-Movies
This project is very simple to run and follow along with. It is structured in a notebook using Python (see version in 'requirements.txt') and essentially goes step by step.

## Project description:
    In this project I set out to determine what the most popular Genre of film was for the decade I was born in, The 90s. While initially, this was for fun, in the midst of exploring, I started to wonder if there might be any correlation between what was most liked at the time and what my generation likes now. I was interested to see how much the results differed based on public opinion vs. dollars spent. My findings based on average gross sales were not surprising. My generation LOVES animation. Even as adults a lot of my peers still actively consume Animated media in some way. 

## Features of this project include:
    - Read data in from a local csv file
    - Cleaned data with built-in functions (i.e. pandas/numpy)
    - Analyzed data to determine number of entries (7,668 rows before cleaning and 7,479 after)
    - Sliced original dataframe and created a new dataframe for the 90s decade
    - Calculated the mean IMDB score AND mean gross box office sales (in millions)
    - Data visualizations for various calculations
    - Markdown language used through out notebook



Instructions:

1. Clone the repository from GitHub to your local environment (or peruse through at your leisure on GitHub's website).
2. cd into the correct folder (the folder you just cloned from GitHub). 'cd' refers to the command used in a shell environment to 'change directories'. This is a fancy way of saying that your are moving through different folders, but instead of pointing and clicking with a mouse you are using file paths.
3. Once you have moved to the correct directory, do a quick "ls -la" command in your shell just to make sure all the folders cloned properly. If you see the same files listed as are on GitHub, you're in the right place. If the files are not listed, try cloning the repository or making sure you've switched to the correct directory.
4. Activate your virtual environment (your 'venv' folder). On Windows, in GitBash shell, the command is                  ". venv/Scripts/activate". You'll know it worked if you see 'venv' in parenthesis on your shell window.
5. Install the requirements listed in the requirements.txt file so that your local environment can run the cells properly. In your shell window the command 'pip install > requirements.txt' should do just that.
6. Once all of that is complete, open the .ipynb file and enjoy!

## Should you want to play around with the caluclations or graphs please feel free! You could see how many times your favorite actors/actresses appear on the list!