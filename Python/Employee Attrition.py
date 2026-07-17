import pandas as pd
hr = pd.read_csv(r"C:\Users\HomePC\Documents\python folder\week8\WA_Fn-UseC_-HR-Employee-Attrition.csv")
lookup_data = {
    'JobRole': ['Healthcare Representative', 'Human Resources', 'Laboratory Technician',
                'Manager', 'Manufacturing Director', 'Research Director',
                'Research Scientist', 'Sales Executive', 'Sales Representative'],
    'JobFamily': ['Healthcare', 'Human Resources', 'Research',
                  'Management', 'Operations', 'Research',
                  'Research', 'Sales', 'Sales']
}
lookup = pd.DataFrame(lookup_data)
merge_df = pd.merge(hr, lookup, how='left', on='JobRole')
print(merge_df.shape)
# inspect the shape of your dataframe before proceeding running analysis using pd.shape.
#define attrition
is_leaver = merge_df['Attrition'] == 'Yes'
# Build your columns using that variable

total_employees = merge_df.groupby('JobFamily').size()
number_leavers = is_leaver.groupby(merge_df['JobFamily']).sum()
attrition_rate = (number_leavers/total_employees).round(2)
estimated_cost = (
    (merge_df.loc[is_leaver, 'MonthlyIncome'] * 12 * 1.5)
    .groupby(merge_df.loc[is_leaver, 'JobFamily'])
    .sum()
)
report = pd.DataFrame({
    'TotalEmployees': total_employees,
    'NumberLeavers': number_leavers,
    'AttritionRate': attrition_rate,
    'EstimatedCost': estimated_cost
}).sort_values('AttritionRate', ascending=False)

print(report)
report.to_csv(r"C:\Users\HomePC\Documents\python folder\week8\attrition_report.csv")