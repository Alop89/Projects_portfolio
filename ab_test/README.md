# A-B_test

## Introduction
The present analysis focuses on understanding user behavior and evaluating the effectiveness of the conversion funnel on a specific platform. The dataset analyzed contains information about user events, divided into three groups: two control groups and one test group. By examining the behavior of these groups, the study aimed to uncover insights into user experience and engagement. To ensure accuracy, the dataset was loaded using the `sep = "\t"` argument for precise value separation, and column names were reformatted to follow the "snake_case" standard for improved readability and consistency. After verifying data integrity, the dataset contained 244,126 records with no null values. Following the removal of 413 duplicate entries, the final dataset comprised 243,713 clean records. Additionally, the timestamp column was processed to generate two new columns for full date-time and date-only formats, enabling more detailed temporal analysis.

## Objective
The primary objectives of the analysis were to examine the user conversion funnel and determine the sequence of key events in the purchasing process, evaluate user retention rates, and identify areas with significant drop-offs. Another objective was to investigate differences between groups using statistical hypothesis testing while applying corrections for multiple comparisons. Lastly, the study sought to assess temporal trends in user events and explore patterns over time.

## Highlights of the analysis
The conversion funnel analysis revealed the final sequence of key events as follows: MainScreenAppear, OffersScreenAppear, CartScreenAppear, PaymentScreenSuccessful, and Tutorial. The "Tutorial" event was identified as an assistance feature for users experiencing challenges in earlier steps of the process. Retention rates were high in the latter stages of the funnel, with 81% of users advancing from OffersScreenAppear to CartScreenAppear and 94.7% proceeding to PaymentScreenSuccessful. However, the most significant drop-off occurred between MainScreenAppear and OffersScreenAppear, where only 62% of users advanced. This suggests that improvements to the main screen and the initial offer presentation could enhance user engagement and progression through the funnel.

![event_per_user](https://github.com/Alop89/A-B_test/blob/main/images/event_per_user.png)
![data_time](https://github.com/Alop89/A-B_test/blob/main/images/data_time.png)

The analysis of temporal trends revealed a significant increase in user events starting on July 31, 2019, serving as a critical point for further investigation. Statistical hypothesis testing showed no significant differences between the control groups or between the control and test groups. To ensure robust findings, the Bonferroni correction was applied, adjusting the significance level to 0.0083 to minimize Type I errors. 

An additional finding was that only 4.2% of users utilized the tutorial. This low usage rate may indicate that the tutorial is either underutilized or poorly positioned. It could also reflect that users find the platform intuitive and do not require further assistance, or that the tutorial's design and accessibility need improvements.

![a_b_test](https://github.com/Alop89/A-B_test/blob/main/images/a_b_test.png)

In conclusion, the analysis highlights the platform's strengths in retaining users during the latter stages of the funnel while identifying areas for improvement in the initial engagement phase. By addressing these insights, the platform can enhance user experience and optimize conversion rates effectively.
