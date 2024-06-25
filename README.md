Please run the Generator first, ensure that the entries are correct

Nextly, check data.csv rows for the correct amount of entries

Then, run processor.py . No extra steps or verification required.

Success!

EXCEL CELL FILLING PROCEDURE

Select the Column (Most commonly Column $J)
Then, open the home tab and select conditional formatting.
Select New rule,
Change the style to Classic,
Then select "Format only cells that contain",
Select "Cell Value" and then "between",
Ensure the ranges are correct, 
0-8 = Red,
9-19 = Yellow,
and 20-23 Green.

OPTIONAL
To prevent filling the label cell,
Change the red cell rule "Applies to" field to $J$2:$J$x,
(x is any amount of rows that are generated, ensure that x + 1 to ensure ideal cell formatting.)