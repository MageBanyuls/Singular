This is my project for singular.

I want to justify my actions in every part of the process

First of all I decided after my research to use Medallion Architecture because its the best to organize layers for data proccessing.

For the data output I used a Sqlite Database but it can be changed in production to postgreSQL, but if we want a file output i think that .parquet extension is really good because it doesnt have the problems of the comas.

1. Data Cleaning and Preprocessing

-Handle Missing Data

Justification:

Missing data can make huge bias in the analysis and take to incorrect results, identify this missing data and treat it makes data more reliable.
When you have continuous values you can use the media or mean. for categoric values the mode. If the amount of missing data is not significant we can proceed to the elimination.

- Data types

Justification:

The correct data type for the data is esential for precise calculation, for example just in the item_price or quantity securing that they are a number allows to perform mathematical calculations without mistakes.

- Outliers detection

justification:

Atipic values can distort metrics like media and afect preddictive models, I used a method called range inter quarthylic (IQR) or standar deviation to identify them, we erase them when are sample errors or we treat them if they are valid information but from outside

3. Customer segmentation

I decided to divide in three percentiles

low_spenders : for example if the percentile 33 of the total amount expended is 50 and the user has less than 50 the useer will go to that category

medium spenders: users that expended more than the percentil 33 and less than the percentil 66.

High spenders: users that expended fro the percentile 67 and up.

Using thirds in the percentile makes that the segmentation is proportional and based on the real distribution of the data.

Identifying low spenders is usefull to apply strategies of upselling or promotion to increase their purchases.

medium spenders can become in high value customers or maybe clients with the right initiative.

High spenders are really valuable and identifying them allows to desgin strategies to increase the retention.
