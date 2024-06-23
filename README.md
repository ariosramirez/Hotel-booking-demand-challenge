# Hotel booking demand challenge

## To run docker
```Bash
docker build . -t jupyter 
```
```Bash
docker run -it  -p 8888:8888 -v $(pwd):/app jupyter
```
Open Jupyter on browser and **Enjoy Jupyter with widgets** ᕙ(`▿´)ᕗ

***
### Key Insights, Findings, and Conclusions

#### Insights
- **Insight:** Families with children tend to book certain room types and have higher special requests, which indicates a preference for more spacious and accommodating environments. This suggests that hotel management should consider these preferences in their service offerings to better cater to families.
- **Insight:** There is a consistent pattern of room type changes for families with children, highlighting the need for hotels to potentially revise their room assignment strategies to better meet the needs of these bookings.

#### Findings
- **Finding:** Across all models, the most influential features in predicting whether a booking includes children were `total_guests`, `total_nights`, and `average_daily_rate`. This emphasizes the importance of these features in understanding family bookings.
- **Finding:** Feature importance analysis from the RandomForest model highlighted that the most significant predictors for bookings with children are `total_guests`, `total_nights`, and `average_daily_rate`.

#### Conclusions
- **Conclusion:** The XGBClassifier model emerged as the best performing model, slightly outperforming others in terms of AUC-ROC score. This makes it a suitable choice for predicting bookings with children, providing a reliable tool for hotel management to anticipate and cater to the needs of families.
- **Conclusion:** Families with children tend to book certain room types and have higher special requests, which are important factors for hotel management to consider in their service offerings.

#### Future Work
- **Future Work:** Further improvement can be achieved by exploring additional features, tuning model hyperparameters, and possibly integrating external data sources to enhance predictive performance. Future research could also investigate other factors influencing family bookings, such as seasonal trends or promotional impacts, to provide even deeper insights.
