# Itc-python-hw-code

## Team members
- 王苡涵、陳奕瑄、蔡旻諺

## School ids
- B08902037, B08902057, B08902103

## Brief introduction:
- This is a crawler which can turn [NTU CSIE news](https://www.csie.ntu.edu.tw/news/news.php?class=101) into a csv file.
- When calling main.py by using the command below:
```
python3 main.py --start-date [start date] --end-date [end date] --output [out filename]
```
- The program will create a file called "[out filename].csv" which includes dates, titles and contents in the period([start date] ~ [end date]).

## Environment
- Python 3.7.2
- Lxml 4.4.2
