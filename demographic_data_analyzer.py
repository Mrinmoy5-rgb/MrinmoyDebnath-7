import pandas as pd

def demographic_data_analyzer():
    df = pd.read_csv(r"C:\Users\nandi\Downloads\ALL 007\vs code\python\Pandas\adult.data.csv")  # Replace with actual path

    # How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Advanced education
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    # Percentage with advanced education earning >50K
    higher_education = df[advanced_education]
    lower_education = df[~advanced_education]
    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)

    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of people working min hours earn >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage_min_workers = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # Country with highest % earning >50K
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()['>50K'] * 100
    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(country_salary.max(), 1)

    # Most popular occupation for those earning >50K in India
    india_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_occupation['occupation'].mode()[0]

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_workers': rich_percentage_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

print(demographic_data_analyzer())