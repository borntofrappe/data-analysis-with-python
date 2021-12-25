# Medical Data Visualizer

Visualize and make calculations from medical examination data with matplotlib, seaborn, and pandas.

_Please note:_ to test the code locally I copied the first and last 200 observations of the entire dataset in `medical_examination.csv`.

## Links

- [Assignment](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer)

- [REPL](https://replit.com/@borntofrappe/boilerplate-medical-data-visualizer)

## Data

The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices.

|                    Feature                    |    Variable Type    |  Variable   |                    Value Type                    |
| :-------------------------------------------: | :-----------------: | :---------: | :----------------------------------------------: |
|                      Age                      |  Objective Feature  |     age     |                    int (days)                    |
|                    Height                     |  Objective Feature  |   height    |                     int (cm)                     |
|                    Weight                     |  Objective Feature  |   weight    |                    float (kg)                    |
|                    Gender                     |  Objective Feature  |   gender    |                 categorical code                 |
|            Systolic blood pressure            | Examination Feature |    ap_hi    |                       int                        |
|           Diastolic blood pressure            | Examination Feature |    ap_lo    |                       int                        |
|                  Cholesterol                  | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |
|                    Glucose                    | Examination Feature |    gluc     | 1: normal, 2: above normal, 3: well above normal |
|                    Smoking                    | Subjective Feature  |    smoke    |                      binary                      |
|                Alcohol intake                 | Subjective Feature  |    alco     |                      binary                      |
|               Physical activity               | Subjective Feature  |   active    |                      binary                      |
| Presence or absence of cardiovascular disease |   Target Variable   |   cardio    |                      binary                      |

## Assignment

Create two charts:

- [a bar plot](https://replit.com/@freecodecamp/boilerplate-medical-data-visualizer#examples/Figure_1.png) to count the number of instances for several binary variables (for instance `active`, `alco`, `cholesterol`). Create two panels to differentiate the counts according to the `cardio` variable (`0` or `1`)

- [a correlation matrix](https://replit.com/@freecodecamp/boilerplate-medical-data-visualizer#examples/Figure_2.png) evaluating the relationship between several variables (for instance `age`, `gender`, `height`, `weight`)

In detail use the data to complete the following tasks:

- add an `overweight` column

  To determine if a person is overweight first calculate their _BMI_ by dividing the weight in kilograms by the square of their height in meters. If the value exceeds 25 then the person is overweight.

  Use the value 0 for **NOT** overweight and the value 1 for overweight

- normalize the data by making 0 always good and 1 always bad

  If the value of `cholesterol` or `gluc` is 1 make the value 0. If the value is more than 1 make the value 1.

- convert the data into long format and create the bar plot with seaborn's `catplot()` function

- clean the data by filtering out the following patient segments, assumed to represent incorrect data:

  - diastolic pressure is higher than systolic

  - height is less than the 2.5th percentile

  - height is more than the 97.5th percentile

  - weight is less than the 2.5th percentile

  - weight is more than the 97.5th percentile

- create the correlation matrix with seaborn's `heatmap()` function, making sure to mask the upper portion and show only the lower left triangle

<!-- ## Solution -->
