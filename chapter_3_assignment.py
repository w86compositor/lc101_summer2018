# You have a thermostat that allows you to set the room to any temperature between 40 and 89 degrees.<br>

# The thermostat can be adjusted by turning a circular dial. For instance, if the temperature is set to 50 degrees and you turn the dial 10 clicks toward the left, you will set the temperature to 40 degrees. But if you keep turning 1 click to the left (represented as -1) it will circle back around to 89 degrees. If you are at 40 degrees and turn to the right by one click, you will get 41 degrees. As you continue to turn to the right, the temperature goes up, and the temperature gets closer and closer to 89 degrees. But as soon as you complete one full rotation (50 clicks), the temperature cycles back around to 40 degrees.<br>

# Write a program that calculates the temperature based on how much the dial has been turned. The number of clicks is contained in a variable (from the starting point of 40 degrees). You should print the current temperature for each given click variable so that your output is as follows:<br>

# The temperature is 40<br>
# The temperature is 89<br>
# The temperature is 64<br>
# The temperature is 41<br>
# The temperature is 89<br>
# The temperature is 40</body>


# For each click variable, calculate the temperature and print it as shown in the instructions

click_1 = 0
click_2 = 49
click_3 = 74
click_4 = 51
click_5 = -1
click_6 = 200


list_of_clicks = [click_1, click_2, click_3,
                  click_4, click_5, click_6]


for click in list_of_clicks:
    total_click = click % 50
    final_temp = total_click + 40
    print("The temperature is", final_temp)
